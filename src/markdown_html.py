from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_types,
    block_type_quote,
    block_type_code,
    block_type_unordered_list,
    block_type_ordered_list,
    block_type_paragraph,
    block_type_heading
)

from textnode import text_node_to_html_node
from htmlnode import ParentNode

from inline_markdown import text_to_textnodes


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children_html_nodes = []
    for text_node in text_nodes:
        children_html_nodes.append(text_node_to_html_node(text_node))
    return children_html_nodes


def block_quote_to_html_node(block):
    split_block = block.split('\n')
    block_list = []
    for line in split_block:
        if line == '':
            continue
        if not line.startswith("> "):
            raise ValueError("Invalid quote block")
        block_list.append(line.lstrip('> ').strip())
    list_block = ' '.join(block_list)
    children = text_to_children(list_block)
    return ParentNode('blockquote', children)


def unordered_list_to_html_node(block):
    split_block = block.split('\n')
    list_items = []
    for line in split_block:
        if line == '':
            continue
        children = text_to_children(line[2:])
        list_items.append(ParentNode('li', children))
    return ParentNode('ul', list_items)


def ordered_list_to_html_node(block):
    split_block = block.split('\n')
    list_items = []
    for line in split_block:
        if line == '':
            continue
        children = text_to_children(line[3:])
        list_items.append(ParentNode('li', children))
    return ParentNode('ol', list_items)


def code_block_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    children = text_to_children(block.strip('` '))
    return ParentNode('pre', [ParentNode('code', children)])


def heading_to_html_node(block):
    heading_level = block.count('#', 0, 7)
    children = text_to_children(block.lstrip('# '))
    return ParentNode(f'h{heading_level}', children)


def paragraph_to_html_node(block):
    lines = block.split('\n')
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode('p', children)


def block_to_html_node(block):
    block_type = block_to_block_types(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_block_to_html_node(block)
    if block_type == block_type_quote:
        return block_quote_to_html_node(block)
    if block_type == block_type_unordered_list:
        return unordered_list_to_html_node(block)
    if block_type == block_type_ordered_list:
        return ordered_list_to_html_node(block)
    raise ValueError("Invalid block type")


def markdown_to_html_node(markdown):
    mk_blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in mk_blocks:
        html_nodes.append(block_to_html_node(block))
    return ParentNode('div', html_nodes, None)
