"""Validate the static site and assemble its public Pages artifact."""

import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
PAGES = (
    "index.html", "empresa.html", "seguros.html", "labs.html",
    "rag.html", "coe.html", "acervo.html",
)
PUBLIC_FILES = PAGES + (
    ".nojekyll", "LICENSE", "NOTICE.md", "DISCLAIMER.md", "SUPPORT.md",
    "SECURITY.md", "CONTRIBUTING.md", "CONTRIBUTORS.md", "README.md", "CITATION.cff",
)
PUBLIC_DIRS = ("assets", "dados", "LICENSES", "docs")
VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.tags = Counter()
        self.stack = []
        self.errors = []
        self.language = None
        self.feed(text)
        self.close()
        if self.stack:
            self.errors.append(f"Unclosed tags: {self.stack}")

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        self.tags[tag] += 1
        if tag not in VOID_TAGS:
            self.stack.append(tag)
        if tag == "html":
            self.language = attributes.get("lang")
        identifier = attributes.get("id")
        if identifier:
            if identifier in self.ids:
                self.errors.append(f"Duplicate id: {identifier}")
            self.ids.add(identifier)
        for key in ("href", "src"):
            if key in attributes:
                self.links.append(attributes[key])
        if tag == "img" and "alt" not in attributes:
            self.errors.append("Image without alt attribute")

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"Unexpected closing tag: {tag}")
        else:
            self.stack.pop()


def local_target(root, source, href):
    url = urlsplit(href)
    if url.scheme or url.netloc:
        if url.scheme and url.scheme not in ("https", "http", "mailto"):
            raise ValueError(f"Unsupported URL scheme: {href}")
        return None
    if url.path.startswith("/"):
        raise ValueError(f"Root-relative link breaks project Pages: {href}")
    target = (source.parent / unquote(url.path)).resolve() if url.path else source
    if not target.is_relative_to(root):
        raise ValueError(f"Link leaves site directory: {href}")
    if not target.exists():
        raise ValueError(f"Missing local target: {href}")
    return target, unquote(url.fragment)


def validate(root):
    root = root.resolve()
    errors = []
    parsed = {}
    references = []
    for name in PUBLIC_FILES:
        if not (root / name).is_file():
            errors.append(f"Missing public file: {name}")
    for name in PUBLIC_DIRS:
        if not (root / name).is_dir():
            errors.append(f"Missing public directory: {name}")
    if (root / "CNAME").exists():
        errors.append("Custom domain requires a separate migration; remove CNAME")
    for path in root.glob("*.html"):
        text = path.read_text(encoding="utf-8")
        page = Page(text)
        parsed[path.resolve()] = page
        errors.extend(f"{path.name}: {error}" for error in page.errors)
        if page.language != "pt-BR":
            errors.append(f"{path.name}: expected lang=pt-BR")
        if page.tags["h1"] != 1 or page.tags["main"] != 1:
            errors.append(f"{path.name}: expected one h1 and one main")
        if page.tags["form"] or page.tags["script"] or page.tags["iframe"]:
            errors.append(f"{path.name}: active integrations are outside current scope")
        if "Empresa fictícia" not in text:
            errors.append(f"{path.name}: missing fictional-company notice")
        references.extend((path, href) for href in page.links)
    if {p.name for p in parsed} != set(PAGES):
        errors.append("Update the public page list before adding or removing pages")
    documents = list(root.glob("*.md")) + [root / "LICENSE"]
    for directory in (root / "docs", root / ".github"):
        if directory.exists():
            documents.extend(directory.rglob("*.md"))
    for path in documents:
        if path.is_file():
            references.extend(
                (path, href) for href in MARKDOWN_LINK.findall(
                    path.read_text(encoding="utf-8")
                )
            )
    for source, href in references:
        try:
            result = local_target(root, source.resolve(), href)
            if result:
                target, fragment = result
                if fragment and target in parsed and fragment not in parsed[target].ids:
                    errors.append(f"{source.name}: missing fragment in {href}")
        except ValueError as error:
            errors.append(f"{source.name}: {error}")
    for path in (root / "assets").glob("*.svg"):
        try:
            ET.parse(path)
        except ET.ParseError as error:
            errors.append(f"{path.name}: {error}")
    data_path = root / "dados" / "contexto-v0.1.0.json"
    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
        assessment = data["assessment_preservado"]
        expected = {
            "pontuacao_geral_bruta": 2.52, "nivel_bruto": 3, "nivel_final": 2,
            "contencoes": 5, "vetos_operacionais": 2,
            "pedido_investimento_brl": 1200000, "horizonte_remediacao_dias": 90,
            "prazo_kill_switch_testado_dias": 45,
        }
        for key, value in expected.items():
            if assessment.get(key) != value:
                errors.append(f"Historical assessment changed: {key}")
        if data["data_referencia_cenario"] != "2026-08":
            errors.append("Historical scenario date changed")
        if "CC BY 4.0" not in data["licenca_novos_conteudos"]:
            errors.append("Content license missing from context data")
    except (OSError, ValueError, KeyError, TypeError) as error:
        errors.append(f"Invalid context data: {error}")
    for name in ("MIT.txt", "CC-BY-4.0.txt"):
        if not (root / "LICENSES" / name).is_file():
            errors.append(f"Missing license text: {name}")
    if errors:
        raise ValueError("\n".join(errors))
    return len(parsed), len(references)


def build(root, destination):
    root, destination = root.resolve(), destination.resolve()
    validate(root)
    if destination.exists():
        raise ValueError(f"Output already exists; choose a new directory: {destination}")
    if destination == root or destination in root.parents:
        raise ValueError("Output cannot contain the source directory")
    for name in PUBLIC_DIRS:
        if destination.is_relative_to(root / name):
            raise ValueError("Output cannot be inside a published directory")
    destination.mkdir(parents=True)
    for name in PUBLIC_FILES:
        shutil.copy2(root / name, destination / name)
    for name in PUBLIC_DIRS:
        shutil.copytree(root / name, destination / name)
    validate(destination)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "build"))
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    args = parser.parse_args()
    try:
        if args.command == "check":
            pages, references = validate(ROOT)
            print(f"PASS: {pages} pages, {references} references, context and licenses")
        else:
            build(ROOT, args.output)
            print(f"Built: {args.output.resolve()}")
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
