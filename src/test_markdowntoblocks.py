import unittest
from inspect import cleandoc

from markdowntoblocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_empty(self):
        markdown = ""
        expected_blocks = [""]
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, expected_blocks)

    def test_one_block(self):
        markdown = "hello"
        expected_blocks = ["hello"]
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, expected_blocks)

    def test_block_with_whitespace(self):
        markdown = "  \nhello "
        expected_blocks = ["hello"]
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, expected_blocks)

    def test_multiline_block(self):
        markdown = cleandoc(
            """
                            block
                            one
                            
                            block
                            two
                            
                            block
                            three
                            """
        )
        expected_blocks = ["block\none", "block\ntwo", "block\nthree"]
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, expected_blocks)

    def test_multiple_blocks(self):
        markdown = cleandoc(
            """
        one block
        
        two block
        
        three block
        """
        )
        expected_blocks = ["one block", "two block", "three block"]
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, expected_blocks)

    def test_extra_newlines(self):
        markdown = cleandoc(
            """
            one block
            
            
            two block
            
            
            
            
            three block
            """
        )
        expected_blocks = ["one block", "two block", "three block"]
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, expected_blocks)


if __name__ == "__main__":
    unittest.main()
