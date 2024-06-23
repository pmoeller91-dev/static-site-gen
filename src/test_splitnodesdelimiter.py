import unittest

from textnode import TextNode, TextType
from splitnodesdelimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_no_delimiter(self):
        node = TextNode(text="no delimiter!", text_type=TextType.TEXT)
        split_nodes = split_nodes_delimiter(
            old_nodes=[node], delimiter="*", text_type=TextType.BOLD
        )
        self.assertEqual(len(split_nodes), 1)
        self.assertEqual(split_nodes[0], node)

    def test_non_text(self):
        node = TextNode(text="_Bold text_", text_type=TextType.BOLD)
        split_nodes = split_nodes_delimiter(
            old_nodes=[node], delimiter="_", text_type=TextType.ITALIC
        )
        self.assertEqual(len(split_nodes), 1)
        self.assertEqual(split_nodes[0], node)

    def test_non_matching(self):
        node = TextNode(text="_italic text", text_type=TextType.TEXT)
        self.assertRaises(
            ValueError,
            split_nodes_delimiter,
            old_nodes=[node],
            delimiter="_",
            text_type=TextType.ITALIC,
        )

    def test_non_matching_multiple(self):
        node = TextNode(
            text="this _one_ has a matching closer, but _this one doesn't",
            text_type=TextType.TEXT,
        )
        self.assertRaises(
            ValueError,
            split_nodes_delimiter,
            old_nodes=[node],
            delimiter="_",
            text_type=TextType.ITALIC,
        )

    def test_simple(self):
        node = TextNode(text="**bold text**", text_type=TextType.TEXT)
        expected_node = TextNode(text="bold text", text_type=TextType.BOLD)
        split_nodes = split_nodes_delimiter(
            old_nodes=[node], delimiter="**", text_type=TextType.BOLD
        )
        self.assertEqual(len(split_nodes), 1)
        self.assertEqual(split_nodes[0], expected_node)

    def test_complex(self):
        node = TextNode(
            text="This text contains **bold text** in the middle",
            text_type=TextType.TEXT,
        )
        expected_nodes = [
            TextNode(text="This text contains ", text_type=TextType.TEXT),
            TextNode(text="bold text", text_type=TextType.BOLD),
            TextNode(text=" in the middle", text_type=TextType.TEXT),
        ]
        split_nodes = split_nodes_delimiter(
            old_nodes=[node], delimiter="**", text_type=TextType.BOLD
        )
        self.assertEqual(len(split_nodes), len(expected_nodes))
        self.assertEqual(split_nodes[0], expected_nodes[0])

    def test_multiple(self):
        node = TextNode(
            text="This text contains **multiple** sets of **bold text** in the middle",
            text_type=TextType.TEXT,
        )
        expected_nodes = [
            TextNode(text="This text contains ", text_type=TextType.TEXT),
            TextNode(text="multiple", text_type=TextType.BOLD),
            TextNode(text=" sets of ", text_type=TextType.TEXT),
            TextNode(text="bold text", text_type=TextType.BOLD),
            TextNode(text=" in the middle", text_type=TextType.TEXT),
        ]
        split_nodes = split_nodes_delimiter(
            old_nodes=[node], delimiter="**", text_type=TextType.BOLD
        )
        self.assertEqual(len(split_nodes), len(expected_nodes))
        self.assertEqual(split_nodes[0], expected_nodes[0])
        

if __name__ == "__main__":
    unittest.main()
