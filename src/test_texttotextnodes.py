import unittest

from textnode import TextNode, TextType
from texttotextnodes import text_to_text_nodes


class TestTextToTextNodes(unittest.TestCase):
    def test_simple(self):
        text = ""
        expected_nodes = []
        text_nodes = text_to_text_nodes(text)
        self.assertEqual(text_nodes, expected_nodes)

    def test_complex(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected_nodes = [
            TextNode(text="This is ", text_type=TextType.TEXT),
            TextNode(text="text", text_type=TextType.BOLD),
            TextNode(text=" with an ", text_type=TextType.TEXT),
            TextNode(text="italic", text_type=TextType.ITALIC),
            TextNode(text=" word and a ", text_type=TextType.TEXT),
            TextNode(text="code block", text_type=TextType.CODE),
            TextNode(text=" and an ", text_type=TextType.TEXT),
            TextNode(
                text="image",
                url="https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                text_type=TextType.IMAGE,
            ),
            TextNode(text=" and a ", text_type=TextType.TEXT),
            TextNode(text="link", url="https://boot.dev", text_type=TextType.LINK),
        ]
        text_nodes = text_to_text_nodes(text)
        self.assertEqual(text_nodes, expected_nodes)

    def test_adjacent(self):
        text = "This is **text**`with`*adjacent* tags"
        expected_nodes = [
            TextNode(text="This is ", text_type=TextType.TEXT),
            TextNode(text="text", text_type=TextType.BOLD),
            TextNode(text="with", text_type=TextType.CODE),
            TextNode(text="adjacent", text_type=TextType.ITALIC),
            TextNode(text=" tags", text_type=TextType.TEXT),
        ]
        text_nodes = text_to_text_nodes(text)
        self.assertEqual(text_nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()
