import re


def markdown_to_blocks(markdown):
    block_split_regex = r"\n{2,}"
    blocks = re.split(block_split_regex, markdown)
    blocks = list(map(lambda block: block.strip(), blocks))
    return blocks
