import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes
)
from textnode import (
    TextNode,
    text_type_italic,
    text_type_text,
    text_type_code,
    text_type_bold,
    text_type_image,
    text_type_link
)


class TestInlineMarkdown(unittest.TestCase):
    def test_split_node_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, result)

    def test_split_node_italic(self):
        node = TextNode("This is text with a *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, result)

    def test_split_node_bold(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, result)

    def test_split_node_multiword(self):
        node = TextNode("This is text with one `code block` and another `code block`.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        result = [
            TextNode("This is text with one ", text_type_text, None),
            TextNode("code block", text_type_code, None),
            TextNode(" and another ", text_type_text, None),
            TextNode("code block", text_type_code, None),
            TextNode(".", text_type_text, None)
        ]
        self.assertEqual(new_nodes, result)

    def test_split_node_delimiter_at_front(self):
        node = TextNode("*This* is text with a early delimiter", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        result = [
            TextNode("This", text_type_italic),
            TextNode(" is text with a early delimiter", text_type_text)
        ]
        self.assertEqual(new_nodes, result)

    def test_split_node_odd_num_delimiters(self):
        node = TextNode("*This* is text with a *early delimiter", text_type_text)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "*", text_type_italic)

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
        )

    def test_extract_markdown_Links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(
            extract_markdown_links(text),
            [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        )

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        new_list = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertEqual(new_nodes, new_list)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            text_type_text
        )
        new_nodes = split_nodes_link([node])
        new_list = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.example.com"),
            TextNode(" and ", text_type_text),
            TextNode("another", text_type_link, "https://www.example.com/another"),
        ]
        self.assertEqual(new_nodes, new_list)

    def test_text_to_text_node(self):
        text = ("This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/" +
                "zjjcJKZ.png) and a [link](https://boot.dev)")

        new_nodes = text_to_textnodes(text)
        result = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        self.assertEqual(new_nodes, result)

    def test_text_to_print_2(self):
        text = ("This is a [link](https://boot.dev) and a **text** with an *italic* word and a `code block` and an !["
                "image](https://i.imgur.com/zjjcJKZ.png)")
        new_nodes = text_to_textnodes(text)
        result = [
            TextNode("This is a ", text_type_text, None),
            TextNode("link", text_type_link, "https://boot.dev"),
            TextNode(" and a ", text_type_text, None),
            TextNode("text", text_type_bold, None),
            TextNode(" with an ", text_type_text, None),
            TextNode("italic", text_type_italic, None),
            TextNode(" word and a ", text_type_text, None),
            TextNode("code block", text_type_code, None),
            TextNode(" and an ", text_type_text, None),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png")
        ]
        self.assertEqual(new_nodes, result)


if __name__ == "__main__":
    unittest.main()
