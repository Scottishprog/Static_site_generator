class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children:{self.children}, {self.props}"

    def to_html(self):
        raise NotImplemented("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode.to_html requires a value")
        if self.tag is None:
            return f"{self.value}"
        elif self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, '{self.value}', {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode({self.tag, self.children, self.props})"

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode requires a tag.")
        if self.children is None:
            raise ValueError("ParentNode must have children.")
        val_string = ""
        for child in self.children:
            val_string += child.to_html()
        return LeafNode(self.tag, val_string, self.props).to_html()
