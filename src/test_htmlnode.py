import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_one(self):
        props = {"prop1": "Hello"}
        expected_html = ' prop1="Hello"'
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), expected_html)

    def test_props_to_html_several(self):
        props = {"prop1": "Hello", "prop2": "Goodbye", "prop3": "Aloha"}
        expected_html = ' prop1="Hello" prop2="Goodbye" prop3="Aloha"'
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
