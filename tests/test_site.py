import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("vareleira_site", ROOT / "scripts" / "site.py")
site = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(site)


class SiteTests(unittest.TestCase):
    def test_source_is_valid(self):
        self.assertEqual(site.validate(ROOT)[0], 7)

    def test_duplicate_id_is_reported(self):
        page = site.Page('<main id="x"><p id="x">Text</p></main>')
        self.assertIn("Duplicate id: x", page.errors)

    def test_unbalanced_tags_are_reported(self):
        self.assertTrue(site.Page("<main><p>Text</main>").errors)

    def test_image_needs_alt(self):
        self.assertIn("Image without alt attribute", site.Page('<img src="x">').errors)

    def test_project_links_stay_relative(self):
        for href in ("/empresa.html", "../outside.html", "javascript:alert(1)"):
            with self.subTest(href=href), self.assertRaises(ValueError):
                site.local_target(ROOT, ROOT / "index.html", href)

    def test_build_is_complete_and_excludes_internal_files(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "site"
            site.build(ROOT, output)
            self.assertEqual(
                site.validate(output, rendered=True)[0],
                7 + len(site.document_sources(output)),
            )
            self.assertFalse((output / "scripts").exists())
            self.assertFalse((output / ".github").exists())
            self.assertFalse((output / "tests").exists())
            self.assertEqual((output / site.ARTICLE).read_bytes(), (ROOT / site.ARTICLE).read_bytes())
            self.assertEqual((output / "index.html").read_bytes(), (ROOT / "index.html").read_bytes())
            with self.assertRaises(ValueError):
                site.build(ROOT, output)

    def test_missing_fragment_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "site"
            site.build(ROOT, output)
            path = output / "index.html"
            path.write_text(path.read_text(encoding="utf-8").replace(
                'href="#conteudo"', 'href="#missing-fragment"'
            ), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "missing fragment"):
                site.validate(output, rendered=True)

    def test_preserved_article_is_required(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "site"
            site.build(ROOT, output)
            (output / site.ARTICLE).unlink()
            with self.assertRaisesRegex(ValueError, "Missing preserved article"):
                site.validate(output, rendered=True)

    def test_preserved_article_changes_require_review(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "site"
            site.build(ROOT, output)
            (output / site.ARTICLE).write_text("changed", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Preserved article changed"):
                site.validate(output, rendered=True)

    def test_historical_numbers_are_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "site"
            site.build(ROOT, output)
            path = output / "dados" / "contexto-v0.1.0.json"
            path.write_text(path.read_text(encoding="utf-8").replace(
                '"nivel_final": 2', '"nivel_final": 3'
            ), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Historical assessment changed"):
                site.validate(output, rendered=True)

    def test_documents_are_formatted_and_linked(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "site"
            site.build(ROOT, output)
            for source in site.document_sources(output):
                self.assertTrue(source.with_suffix(".html").is_file())
                original = ROOT / source.relative_to(output)
                self.assertEqual(source.read_bytes(), original.read_bytes())
            support = (output / "SUPPORT.html").read_text(encoding="utf-8")
            self.assertIn("<h1", support)
            self.assertIn('href="CONTRIBUTING.html"', support)
            self.assertIn('href="SUPPORT.md" download', support)
            acervo = (output / "acervo.html").read_text(encoding="utf-8")
            self.assertIn('href="SUPPORT.html"', acervo)
            self.assertIn('href="LICENSE.html"', acervo)
            publication = (output / "docs" / "publicacao.html").read_text(encoding="utf-8")
            self.assertIn('href="../assets/site.css"', publication)
            self.assertIn('href="../CODE_OF_CONDUCT.html"', publication)
            self.assertIn("<pre><code", publication)
            self.assertIn('class="table-scroll"', publication)

    def test_document_link_conversion_preserves_url_parts(self):
        source = ROOT / "index.html"
        documents = {(ROOT / "SUPPORT.md").resolve(): ROOT / "SUPPORT.html"}
        for href in (
            "SUPPORT.md?view=1#limites",
            "https://github.com/EdneiMonteiro/vareleira/blob/main/SUPPORT.md?view=1#limites",
            "https://vareleira.com/SUPPORT.md?view=1#limites",
        ):
            with self.subTest(href=href):
                self.assertEqual(site.document_url(ROOT, source, href, documents),
                                 "SUPPORT.html?view=1#limites")
        external = "https://github.com/EdneiMonteiro/ai-coe-playbook/blob/main/README.md"
        self.assertEqual(site.document_url(ROOT, source, external, documents), external)


if __name__ == "__main__":
    unittest.main()
