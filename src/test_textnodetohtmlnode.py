import unittest

from textnode import TextNode, TextType
from textnodetohtmlnode import text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        text_node = TextNode(text="Hello", text_type=TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        expected_html = "Hello"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_bold(self):
        text_node = TextNode(text="Hello", text_type=TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        expected_html = "<b>Hello</b>"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_italic(self):
        text_node = TextNode(text="Hello", text_type=TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        expected_html = "<i>Hello</i>"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_code(self):
        text_node = TextNode(text="Hello", text_type=TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        expected_html = "<code>Hello</code>"
        self.assertEqual(html_node.to_html(), expected_html)

    def test_link(self):
        text_node = TextNode(
            text="Hello", text_type=TextType.LINK, url="https://google.com/"
        )
        html_node = text_node_to_html_node(text_node)
        expected_html = '<a href="https://google.com/">Hello</a>'
        self.assertEqual(html_node.to_html(), expected_html)

    def test_image(self):
        img_src = "https://google.com/favicon.ico"
        alt_text = "Hello"
        text_node = TextNode(text=alt_text, text_type=TextType.IMAGE, url=img_src)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.props["alt"], alt_text)
        self.assertEqual(html_node.props["src"], img_src)
        self.assertEqual(html_node.tag, "img")

    def test_invalid(self):
        text_node = TextNode(text="hello", text_type="Invalid")
        self.assertRaises(ValueError, text_node_to_html_node, text_node)


if __name__ == "__main__":
    unittest.main()
