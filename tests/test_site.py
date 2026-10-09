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
            self.assertEqual(site.validate(output)[0], 7)
            self.assertFalse((output / "scripts").exists())
            self.assertFalse((output / ".github").exists())
            self.assertFalse((output / "tests").exists())
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
                site.validate(output)

    def test_historical_numbers_are_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "site"
            site.build(ROOT, output)
            path = output / "dados" / "contexto-v0.1.0.json"
            path.write_text(path.read_text(encoding="utf-8").replace(
                '"nivel_final": 2', '"nivel_final": 3'
            ), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Historical assessment changed"):
                site.validate(output)


if __name__ == "__main__":
    unittest.main()
