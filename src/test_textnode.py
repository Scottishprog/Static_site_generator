import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_w_url_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text path", "bold")
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", "bold", "https://www.none.com")
        node2 = TextNode("This is a text node", "bold", "https://www.none.com")
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://www.none.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
