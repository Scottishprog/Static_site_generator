import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props1(self):
        node = HTMLNode("LoL", None, None, {"href": "https://www.nowhere.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.nowhere.com" target="_blank"')

    def test_props2(self):
        node = HTMLNode("ROFL", "Yeaaaaaah", None, {"href": "https://www.obscure.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.obscure.com" target="_blank"')

    def test_html_no_tag(self):
        node = LeafNode(None, "This is a Test")
        self.assertEqual(node.to_html(), "This is a Test")

    def test_html_no_children(self):
        node = LeafNode("a", "This is a Test")
        self.assertEqual(node.to_html(), '<a>This is a Test</a>')

    def test_html_tag_props(self):
        node = LeafNode("p", "This is a Test", {"href": "https://www.nowhere.com"})
        self.assertEqual(node.to_html(), '<p href="https://www.nowhere.com">This is a Test</p>')

    def test_parent_node_no_recursion(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_parent_node_recursion(self):
        node = ParentNode(
            "p",
            [
                ParentNode("p2", [ParentNode("p3", [LeafNode("i", "italic text")])]),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), '<p><p2><p3><i>italic text</i></p3></p2>Normal text</p>')

    def test_parent_node_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), '<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>')


if __name__ == "__main__":
    unittest.main()
