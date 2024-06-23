from textnode import TextNode, TextType
from extractmarkdownimages import extract_markdown_images


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        if text == "":
            continue
        image_tuples, text_segments = extract_markdown_images(node.text)
        if len(image_tuples) == 0:
            new_nodes.append(node)
            continue

        image_nodes = list(
            map(
                lambda image_tuple: TextNode(
                    text=image_tuple[0], url=image_tuple[1], text_type=TextType.IMAGE
                ),
                image_tuples,
            )
        )
        text_nodes = list(
            map(
                lambda text: TextNode(text=text, text_type=TextType.TEXT), text_segments
            )
        )

        for i in range(len(image_nodes)):
            if text_nodes[i].text != "":
                new_nodes.append(text_nodes[i])
            new_nodes.append(image_nodes[i])
        if text_nodes[-1].text != "":
            new_nodes.append(text_nodes[-1])

    return new_nodes
