class HTMLNode:
    """A class representing an HTML node"""

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None:
            return ""
        return "".join([f' {k}="{v}"' for k, v in self.props.items()])

    def __repr__(self):
        return f'HTMLNode(tag = "{self.tag}", value = "{self.value}", children = "{self.children}", props = "{self.props}")'
