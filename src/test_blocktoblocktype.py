import unittest

from blocktoblocktype import block_to_block_type
from blocktype import BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "### This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code(self):
        block = "```This is a\ncode block```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_quote(self):
        block = "> this is\n> a quote\n> with three lines."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_quote_missing_one_line(self):
        block = "> this is\nnot a quote\n> with three lines."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_unordered_list_dash(self):
        block = "- this is\n- an unordered\n- list"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_unordered_list_star(self):
        block = "* this is\n* an unordered\n* list"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_unordered_list_mixed(self):
        block = "* this is\n- not an unordered\n* list"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list(self):
        block = "1. this\n2. is an\n3. ordered list"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_starting(self):
        block = "2. this\n3. is not an\n4. ordered list"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list_bad_sequence(self):
        block = "1. this\n3. is not an\n4. ordered list"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_paragraph(self):
        block = "This is a normal paragraph with nothing special"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
