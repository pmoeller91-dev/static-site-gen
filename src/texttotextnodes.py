from splitnodesdelimiter import split_nodes_delimiter
from splitnodesimage import split_nodes_image
from splitnodeslink import split_nodes_link
from textnode import TextNode, TextType


def text_to_text_nodes(text):
    text_node = TextNode(text=text, text_type=TextType.TEXT)
    nodes = [text_node]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes
