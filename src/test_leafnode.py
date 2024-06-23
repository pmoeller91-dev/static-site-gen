import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        node = LeafNode(value="Hi")
        expected_html = "Hi"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_tag(self):
        node = LeafNode(value="Hi", tag="b")
        expected_html = "<b>Hi</b>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_props(self):
        node = LeafNode(value="Hi", tag="a", props={"href": "https://google.com/"})
        expected_html = '<a href="https://google.com/">Hi</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_props_no_tag(self):
        node = LeafNode(value="Hi", props={"href": "https://google.com/"})
        expected_html = "Hi"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_multiple_props(self):
        node = LeafNode(
            value="Hi",
            tag="a",
            props={"href": "https://google.com/", "rel": "noreferer"},
        )
        expected_html = '<a href="https://google.com/" rel="noreferer">Hi</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_no_value(self):
        node = LeafNode(value=None)
        self.assertRaises(ValueError, node.to_html)


if __name__ == "__main__":
    unittest.main()
