import unittest
from inspect import cleandoc
from markdowntohtmlnode import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_single_block(self):
        markdown = cleandoc(
            """
        > hello
        > single block
        """
        )
        expected_html = "<div><blockquote>hello\nsingle block</blockquote></div>"
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        self.assertEqual(html, expected_html)

    def test_multiple_block(self):
        markdown = cleandoc(
            """
        > hello
        > single block
        
        ```
        code block
        with *code*
        ```
        """
        )
        expected_html = "<div><blockquote>hello\nsingle block</blockquote><pre><code>\ncode block\nwith <i>code</i>\n</code></pre></div>"
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        self.assertEqual(html, expected_html)


if __name__ == "__main__":
    unittest.main()
