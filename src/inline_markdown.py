from textnode import (
    TextNode,
    text_type_text,
    text_type_code,
    text_type_bold,
    text_type_italic,
    text_type_image,
    text_type_link
)
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not text_type_text:
            new_nodes.append(node)
            continue
        new_text = node.text.split(delimiter)
        if len(new_text) % 2 == 0:
            raise Exception(f"Need even numbers of:{delimiter}, {text_type}, note: nested text types not allowed")
        for i in range(0, len(new_text)):
            if new_text[i] == '':
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(new_text[i], text_type_text))
            else:
                new_nodes.append(TextNode(new_text[i], text_type))

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        original_text = node.text
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        split_node = []
        for image_tup in images:
            split_node = original_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            if len(split_node) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if split_node[0] != "":
                new_nodes.append(TextNode(split_node[0], node.text_type))
            new_nodes.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
            original_text = split_node[1]
        if split_node[1] != "":
            new_nodes.append(TextNode(split_node[1], text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        original_text = node.text
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        split_node = []
        for link_tup in links:
            split_node = original_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if len(split_node) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if split_node[0] != "":
                new_nodes.append(TextNode(split_node[0], node.text_type))
            new_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
            original_text = split_node[1]
        if split_node[1] != "":
            new_nodes.append(TextNode(split_node[1], text_type_text))
    return new_nodes


def text_to_textnodes(text):
    new_text_node = TextNode(text, text_type_text)
    new_textnodes = split_nodes_delimiter([new_text_node], "**", text_type_bold)
    new_textnodes = split_nodes_delimiter(new_textnodes, "*", text_type_italic)
    new_textnodes = split_nodes_delimiter(new_textnodes, "`", text_type_code)
    new_textnodes = split_nodes_image(new_textnodes)
    new_textnodes = split_nodes_link(new_textnodes)
    return new_textnodes
