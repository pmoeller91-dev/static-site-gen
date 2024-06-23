from blocktype import BlockType
import re


def block_to_block_type(block):
    heading_regex = r"^#{1,6} .+$"
    if re.fullmatch(heading_regex, block, re.DOTALL):
        return BlockType.HEADING

    code_regex = r"^```.+```$"
    if re.fullmatch(code_regex, block, re.DOTALL):
        return BlockType.CODE

    lines = block.split("\n")
    if all(line.startswith("> ") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("* ") for line in lines):
        return BlockType.UNORDERED_LIST

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if all(
        lines[linenum].startswith(f"{linenum + 1}. ") for linenum in range(len(lines))
    ):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
