import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_no_children(self):
        node = ParentNode(tag="b", children=None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_tag(self):
        node = ParentNode(tag=None, children=[LeafNode(value="Hi")])
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_one_text_child(self):
        node = ParentNode(tag="b", children=[LeafNode(value="Hi")])
        expected_html = "<b>Hi</b>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_multiple_text_children(self):
        children = [
            LeafNode(value="Hi"),
            LeafNode(value="Hello"),
            LeafNode(value="Hey"),
        ]
        node = ParentNode(tag="b", children=children)
        expected_html = "<b>HiHelloHey</b>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_one_child(self):
        node = ParentNode(tag="p", children=[LeafNode(value="Hi", tag="b")])
        expected_html = "<p><b>Hi</b></p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_multiple_children(self):
        children = [
            LeafNode(value="Hello there, "),
            LeafNode(value="Firstname Lastname", tag="b"),
            LeafNode(value="."),
        ]
        node = ParentNode(tag="p", children=children)
        expected_html = "<p>Hello there, <b>Firstname Lastname</b>.</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_nested(self):
        nested_children = [
            LeafNode(value="Item one", tag="li"),
            LeafNode(value="Item two", tag="li"),
            LeafNode(value="Item three", tag="li"),
        ]
        children = [
            LeafNode(value="My arguments are as follows: ", tag="p"),
            ParentNode(tag="ol", children=nested_children),
            LeafNode(value="Thank you for your time.", tag="p"),
        ]
        node = ParentNode(tag="div", children=children)
        expected_html = "<div><p>My arguments are as follows: </p><ol><li>Item one</li><li>Item two</li><li>Item three</li></ol><p>Thank you for your time.</p></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_props(self):
        children = [LeafNode(value="Hi")]
        node = ParentNode(tag="p", children=children, props={"className": "class"})
        expected_html = '<p className="class">Hi</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_nested_deep(self):
        nested_nested_children = [
            ParentNode(tag="div", children=[LeafNode(value="Hi")]),
        ]
        nested_children = [
            ParentNode(tag="div", children=nested_nested_children),
        ]
        children = [
            ParentNode(tag="div", children=nested_children),
        ]
        node = ParentNode(tag="div", children=children)
        expected_html = "<div><div><div><div>Hi</div></div></div></div>"
        self.assertEqual(node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
