from markdowntoblocks import markdown_to_blocks
from blocktohtmlnode import block_to_html_node
from parentnode import ParentNode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_html_nodes = list(map(lambda block: block_to_html_node(block), blocks))
    markdown_html_node = ParentNode(tag="div", children=block_html_nodes)
    return markdown_html_node
