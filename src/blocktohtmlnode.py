from leafnode import LeafNode
from parentnode import ParentNode
from blocktoblocktype import block_to_block_type
from blocktype import BlockType
from texttotextnodes import text_to_text_nodes
from textnodetohtmlnode import text_node_to_html_node
import re


def text_to_html_nodes(text):
    text_nodes = text_to_text_nodes(text)
    html_nodes = list(
        map(lambda text_node: text_node_to_html_node(text_node), text_nodes)
    )
    return html_nodes


def block_to_paragraph_html_node(block):
    html_nodes = text_to_html_nodes(block)
    paragraph_html_node = ParentNode(tag="p", children=html_nodes)
    return paragraph_html_node


def block_to_blockquote_html_node(block):
    stripped_block = re.sub(r"^> ", "", block, flags=re.MULTILINE)
    html_nodes = text_to_html_nodes(stripped_block)
    blockquote_html_node = ParentNode(tag="blockquote", children=html_nodes)
    return blockquote_html_node


def block_to_ul_html_node(block):
    stripped_block = re.sub(r"^[-*] ", "", block, flags=re.MULTILINE)
    lines = stripped_block.split("\n")
    lines_html_nodes = list(map(lambda line: text_to_html_nodes(line), lines))
    li_html_nodes = list(
        map(
            lambda line_html_nodes: ParentNode(tag="li", children=line_html_nodes),
            lines_html_nodes,
        )
    )
    ul_html_node = ParentNode(tag="ul", children=li_html_nodes)
    return ul_html_node


def block_to_ol_html_node(block):
    stripped_block = re.sub(r"^[\d]+. ", "", block, flags=re.MULTILINE)
    lines = stripped_block.split("\n")
    lines_html_nodes = list(map(lambda line: text_to_html_nodes(line), lines))
    li_html_nodes = list(
        map(
            lambda line_html_nodes: ParentNode(tag="li", children=line_html_nodes),
            lines_html_nodes,
        )
    )
    ol_html_node = ParentNode(tag="ol", children=li_html_nodes)
    return ol_html_node


def block_to_code_html_node(block):
    stripped_block = block[3:-3]
    html_nodes = text_to_html_nodes(stripped_block)
    code_html_node = ParentNode(
        tag="pre", children=[ParentNode(tag="code", children=html_nodes)]
    )
    return code_html_node


def block_to_heading_html_node(block):
    header_characters = re.match(r"^#{1,6}(?= )", block).group(0)
    tag = f"h{len(header_characters)}"
    stripped_block = re.sub(r"^#{1,6} ", "", block)
    html_nodes = text_to_html_nodes(stripped_block)
    header_html_node = ParentNode(tag=tag, children=html_nodes)
    return header_html_node


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            return block_to_paragraph_html_node(block)
        case BlockType.QUOTE:
            return block_to_blockquote_html_node(block)
        case BlockType.CODE:
            return block_to_code_html_node(block)
        case BlockType.HEADING:
            return block_to_heading_html_node(block)
        case BlockType.UNORDERED_LIST:
            return block_to_ul_html_node(block)
        case BlockType.ORDERED_LIST:
            return block_to_ol_html_node(block)
        case _:
            return block_to_paragraph_html_node(block)
