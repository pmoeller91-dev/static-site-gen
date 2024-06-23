import unittest

from textnode import TextNode, TextType
from splitnodeslink import split_nodes_link


class TestSplitNodesLink(unittest.TestCase):
    def test_only_link(self):
        node = TextNode(
            text="[link text](https://google.com/)",
            text_type=TextType.TEXT,
        )
        expected_nodes = [
            TextNode(
                text="link text",
                url="https://google.com/",
                text_type=TextType.LINK,
            ),
        ]
        split_nodes = split_nodes_link([node])
        self.assertEqual(split_nodes, expected_nodes)

    def test_one_link(self):
        node = TextNode(
            text="contains one link: [link text](https://google.com/)",
            text_type=TextType.TEXT,
        )
        expected_nodes = [
            TextNode(text="contains one link: ", text_type=TextType.TEXT),
            TextNode(
                text="link text",
                url="https://google.com/",
                text_type=TextType.LINK,
            ),
        ]
        split_nodes = split_nodes_link([node])
        self.assertEqual(split_nodes, expected_nodes)

    def test_no_link(self):
        node = TextNode(text="Contains no links at all", text_type=TextType.TEXT)
        expected_nodes = [node]
        split_nodes = split_nodes_link([node])
        self.assertEqual(split_nodes, expected_nodes)

    def test_not_text(self):
        node = TextNode(
            text="contains one link: [link text](https://google.com/)",
            text_type=TextType.BOLD,
        )
        expected_nodes = [node]
        split_nodes = split_nodes_link([node])
        self.assertEqual(split_nodes, expected_nodes)

    def test_image(self):
        node = TextNode(
            text="contains one image: ![alt-text](https://img.img/img.jpg)",
            text_type=TextType.TEXT,
        )
        expected_nodes = [node]
        split_nodes = split_nodes_link([node])
        self.assertEqual(split_nodes, expected_nodes)

    def test_multiple_links(self):
        node = TextNode(
            text="contains [one link](https://google.com/) and [another link](https://yahoo.com/).",
            text_type=TextType.TEXT,
        )
        expected_nodes = [
            TextNode(text="contains ", text_type=TextType.TEXT),
            TextNode(
                text="one link",
                url="https://google.com/",
                text_type=TextType.LINK,
            ),
            TextNode(text=" and ", text_type=TextType.TEXT),
            TextNode(
                text="another link",
                url="https://yahoo.com/",
                text_type=TextType.LINK,
            ),
            TextNode(text=".", text_type=TextType.TEXT),
        ]
        split_nodes = split_nodes_link([node])
        self.assertEqual(split_nodes, expected_nodes)

    def test_link_and_image(self):
        node = TextNode(
            text="contains [one link](https://google.com/) and one image: ![alt-text](https://img.img/img.jpg)",
            text_type=TextType.TEXT,
        )
        expected_nodes = [
            TextNode(text="contains ", text_type=TextType.TEXT),
            TextNode(
                text="one link", url="https://google.com/", text_type=TextType.LINK
            ),
            TextNode(
                text=" and one image: ![alt-text](https://img.img/img.jpg)",
                text_type=TextType.TEXT,
            ),
        ]
        split_nodes = split_nodes_link([node])
        self.assertEqual(split_nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()
