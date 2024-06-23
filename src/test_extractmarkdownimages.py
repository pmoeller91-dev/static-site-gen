import unittest

from extractmarkdownimages import extract_markdown_images


class TestExtractMarkdownImages(unittest.TestCase):
    def test_no_image(self):
        text = "no images here"
        image_tuples = extract_markdown_images(text)[0]
        self.assertEqual(image_tuples, [])

    def test_one_image(self):
        text = "this text contains one image: ![alt-text](https://images.img/image.jpg)"
        expected_tuples = [("alt-text", "https://images.img/image.jpg")]
        image_tuples = extract_markdown_images(text)[0]
        self.assertEqual(image_tuples, expected_tuples)

    def test_multiple_images(self):
        text = "this text contains two images: ![alt-text](https://images.img/image.jpg) here's the second one: ![more-alt-text](https://images.img/image2.jpg)."
        expected_tuples = [
            ("alt-text", "https://images.img/image.jpg"),
            ("more-alt-text", "https://images.img/image2.jpg"),
        ]
        image_tuples = extract_markdown_images(text)[0]
        self.assertEqual(image_tuples, expected_tuples)

    def test_link(self):
        text = "this text contains a [link](https://google.com)"
        expected_tuples = []
        image_tuples = extract_markdown_images(text)[0]
        self.assertEqual(image_tuples, expected_tuples)

    def test_link_and_image(self):
        text = "this text contains a [link](https://google.com) and an image ![alt-text](https://images.img/image.jpg)"
        expected_tuples = [("alt-text", "https://images.img/image.jpg")]
        image_tuples = extract_markdown_images(text)[0]
        self.assertEqual(image_tuples, expected_tuples)


if __name__ == "__main__":
    unittest.main()
