from textnode import TextNode, TextType
from extractmarkdownlinks import extract_markdown_links


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        if text == "":
            continue
        link_tuples, text_segments = extract_markdown_links(node.text)
        if len(link_tuples) == 0:
            new_nodes.append(node)
            continue

        link_nodes = list(
            map(
                lambda link_tuple: TextNode(
                    text=link_tuple[0], url=link_tuple[1], text_type=TextType.LINK
                ),
                link_tuples,
            )
        )
        text_nodes = list(
            map(
                lambda text: TextNode(text=text, text_type=TextType.TEXT),
                text_segments,
            )
        )

        for i in range(len(link_nodes)):
            if text_nodes[i].text != "":
                new_nodes.append(text_nodes[i])
            new_nodes.append(link_nodes[i])
        if text_nodes[-1].text != "":
            new_nodes.append(text_nodes[-1])

    return new_nodes
