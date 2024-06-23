from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, children, tag, props=None):
        super().__init__(children=children, tag=tag, props=props, value=None)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag specified")
        if self.children == None:
            raise ValueError("ParentNode must have children specified")

        child_html = "".join(map(lambda child: child.to_html(), self.children))

        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
