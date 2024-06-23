from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        text_segments = text.split(delimiter)

        if len(text_segments) == 1:
            new_nodes.append(node)
            continue

        if len(text_segments) % 2 == 0:
            raise ValueError(
                f'No closing delimiter found in "{text}" with delimiter "{delimiter}"'
            )

        for segment_num in range(len(text_segments)):
            if text_segments[segment_num] == "":
                continue
            if segment_num % 2 == 0:
                new_nodes.append(
                    TextNode(text=text_segments[segment_num], text_type=TextType.TEXT)
                )
            else:
                new_nodes.append(
                    TextNode(text=text_segments[segment_num], text_type=text_type)
                )

    return new_nodes
