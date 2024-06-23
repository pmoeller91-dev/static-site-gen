import unittest
from extracttitle import extract_title
from inspect import cleandoc


class TestExtractTitle(unittest.TestCase):
    def test_with_title(self):
        markdown = cleandoc(
            """
            this
            markdown
            has a title
            
            # line
            
            
            """
        )
        expected_title = "line"
        title = extract_title(markdown)
        self.assertEqual(title, expected_title)

    def test_without_title(self):
        markdown = cleandoc(
            """
            this
            markdown
            has no title
            """
        )
        self.assertRaises(ValueError, extract_title, markdown)


if __name__ == "__main__":
    unittest.main()
