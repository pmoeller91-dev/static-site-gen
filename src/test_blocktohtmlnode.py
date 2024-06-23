import unittest
from blocktohtmlnode import block_to_html_node


class TestBlockToHTMLNode(unittest.TestCase):
    def test_paragraph(self):
        block = "hello *italic* **bold**"
        expected_html = "<p>hello <i>italic</i> <b>bold</b></p>"
        html_node = block_to_html_node(block)
        html = html_node.to_html()
        self.assertEqual(html, expected_html)

    def test_blockquote(self):
        block = "> test\n> hello *there*"
        expected_html = "<blockquote>test\nhello <i>there</i></blockquote>"
        html_node = block_to_html_node(block)
        html = html_node.to_html()
        self.assertEqual(html, expected_html)

    def test_code(self):
        block = "```\ncode\nblock\nhere\n```"
        expected_html = "<pre><code>\ncode\nblock\nhere\n</code></pre>"
        html_node = block_to_html_node(block)
        html = html_node.to_html()
        self.assertEqual(html, expected_html)

    def test_header_h1(self):
        block = "# header1"
        expected_html = "<h1>header1</h1>"
        html_node = block_to_html_node(block)
        html = html_node.to_html()
        self.assertEqual(html, expected_html)

    def test_header_h3(self):
        block = "### header3"
        expected_html = "<h3>header3</h3>"
        html_node = block_to_html_node(block)
        html = html_node.to_html()
        self.assertEqual(html, expected_html)

    def test_header_h6(self):
        block = "###### header6"
        expected_html = "<h6>header6</h6>"
        html_node = block_to_html_node(block)
        html = html_node.to_html()
        self.assertEqual(html, expected_html)

    def test_header_invalid(self):
        block = "####### header7"
        expected_html = "<p>####### header7</p>"
        html_node = block_to_html_node(block)
        html = html_node.to_html()
        self.assertEqual(html, expected_html)

    def test_unordered_list(self):
        block = "- item *one*\n- item **two**\n- item three"
        expected_html = "<ul><li>item <i>one</i></li><li>item <b>two</b></li><li>item three</li></ul>"
        html_node = block_to_html_node(block)
        html = html_node.to_html()
        self.assertEqual(html, expected_html)

    def test_unordered_list_alternate(self):
        block = "* item *one*\n* item **two**\n* item three"
        expected_html = "<ul><li>item <i>one</i></li><li>item <b>two</b></li><li>item three</li></ul>"
        html_node = block_to_html_node(block)
        html = html_node.to_html()
        self.assertEqual(html, expected_html)

    def test_ordered_list(self):
        block = "1. item *one*\n2. item **two**\n3. item three"
        expected_html = "<ol><li>item <i>one</i></li><li>item <b>two</b></li><li>item three</li></ol>"
        html_node = block_to_html_node(block)
        html = html_node.to_html()
        self.assertEqual(html, expected_html)


if __name__ == "__main__":
    unittest.main()
