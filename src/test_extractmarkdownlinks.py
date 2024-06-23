import unittest

from extractmarkdownlinks import extract_markdown_links


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_no_link(self):
        text = "no links here"
        link_tuples = extract_markdown_links(text)[0]
        self.assertEqual(link_tuples, [])

    def test_one_link(self):
        text = "this text contains [one link](https://google.com/)"
        expected_tuples = [("one link", "https://google.com/")]
        link_tuples = extract_markdown_links(text)[0]
        self.assertEqual(link_tuples, expected_tuples)

    def test_multiple_links(self):
        text = "this text contains [one link](https://google.com/) and [another link](https://yahoo.com/)"
        expected_tuples = [
            ("one link", "https://google.com/"),
            ("another link", "https://yahoo.com/"),
        ]
        link_tuples = extract_markdown_links(text)[0]
        self.assertEqual(link_tuples, expected_tuples)

    def test_image(self):
        text = "this text contains an image: ![alt-text](https://images.img/img.jpg)"
        expected_tuples = []
        link_tuples = extract_markdown_links(text)[0]
        self.assertEqual(link_tuples, expected_tuples)

    def test_link_and_image(self):
        text = "this text contains a [link](https://google.com) and an image ![alt-text](https://images.img/image.jpg)"
        expected_tuples = [("link", "https://google.com")]
        link_tuples = extract_markdown_links(text)[0]
        self.assertEqual(link_tuples, expected_tuples)


if __name__ == "__main__":
    unittest.main()
