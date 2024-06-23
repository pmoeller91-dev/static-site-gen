import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("Text", TextType.BOLD, "https://google.com/")
        node2 = TextNode("Text", TextType.BOLD, "https://google.com/")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("Text", TextType.BOLD, "https://google.com/")
        node2 = TextNode("Different Text", TextType.BOLD, "https://google.com/")
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("Text", TextType.BOLD, "https://google.com/")
        node2 = TextNode("Text", TextType.ITALIC, "https://google.com/")
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("Text", TextType.BOLD, "https://google.com/")
        node2 = TextNode("Text", TextType.BOLD, "https://yahoo.com/")
        self.assertNotEqual(node, node2)

    def test_not_eq_url_none(self):
        node = TextNode("Text", TextType.BOLD, "https://google.com/")
        node2 = TextNode("Text", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
