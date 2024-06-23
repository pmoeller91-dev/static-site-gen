import unittest

from textnode import TextNode, TextType
from splitnodesimage import split_nodes_image


class TestSplitNodesImage(unittest.TestCase):
    def test_only_image(self):
        node = TextNode(
            text="![alt-text](https://imgs.img/img.jpg)",
            text_type=TextType.TEXT,
        )
        expected_nodes = [
            TextNode(
                text="alt-text",
                url="https://imgs.img/img.jpg",
                text_type=TextType.IMAGE,
            ),
        ]
        split_nodes = split_nodes_image([node])
        self.assertEqual(split_nodes, expected_nodes)

    def test_one_image(self):
        node = TextNode(
            text="contains one image: ![alt-text](https://imgs.img/img.jpg)",
            text_type=TextType.TEXT,
        )
        expected_nodes = [
            TextNode(text="contains one image: ", text_type=TextType.TEXT),
            TextNode(
                text="alt-text",
                url="https://imgs.img/img.jpg",
                text_type=TextType.IMAGE,
            ),
        ]
        split_nodes = split_nodes_image([node])
        self.assertEqual(split_nodes, expected_nodes)

    def test_no_image(self):
        node = TextNode(text="Contains no images at all", text_type=TextType.TEXT)
        expected_nodes = [node]
        split_nodes = split_nodes_image([node])
        self.assertEqual(split_nodes, expected_nodes)

    def test_not_text(self):
        node = TextNode(
            text="contains one image: ![alt-text](https://imgs.img/img.jpg)",
            text_type=TextType.BOLD,
        )
        expected_nodes = [node]
        split_nodes = split_nodes_image([node])
        self.assertEqual(split_nodes, expected_nodes)

    def test_link(self):
        node = TextNode(
            text="contains [one link](https://google.com/)", text_type=TextType.TEXT
        )
        expected_nodes = [node]
        split_nodes = split_nodes_image([node])
        self.assertEqual(split_nodes, expected_nodes)

    def test_multiple_images(self):
        node = TextNode(
            text="contains one image: ![alt-text](https://imgs.img/img.jpg) and another image: ![more-alt-text](https://imgs.img/img2.jpg).",
            text_type=TextType.TEXT,
        )
        expected_nodes = [
            TextNode(text="contains one image: ", text_type=TextType.TEXT),
            TextNode(
                text="alt-text",
                url="https://imgs.img/img.jpg",
                text_type=TextType.IMAGE,
            ),
            TextNode(text=" and another image: ", text_type=TextType.TEXT),
            TextNode(
                text="more-alt-text",
                url="https://imgs.img/img2.jpg",
                text_type=TextType.IMAGE,
            ),
            TextNode(text=".", text_type=TextType.TEXT),
        ]
        split_nodes = split_nodes_image([node])
        self.assertEqual(split_nodes, expected_nodes)

    def test_link_and_image(self):
        node = TextNode(
            text="contains [one link](https://google.com/) and one image: ![alt-text](https://img.img/img.jpg)",
            text_type=TextType.TEXT,
        )
        expected_nodes = [
            TextNode(
                text="contains [one link](https://google.com/) and one image: ",
                text_type=TextType.TEXT,
            ),
            TextNode(
                text="alt-text", url="https://img.img/img.jpg", text_type=TextType.IMAGE
            ),
        ]
        split_nodes = split_nodes_image([node])
        self.assertEqual(split_nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()
