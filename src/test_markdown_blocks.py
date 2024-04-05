import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_types,
    block_type_code,
    block_type_quote,
    block_type_paragraph,
    block_type_heading,
    block_type_ordered_list,
    block_type_unordered_list
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.
This is the same paragraph on a new line.

* This is a list item
* This is another list item
"""

        result = [
            '# This is a heading',

            'This is a paragraph of text. It has some **bold** and *italic* words inside '
            'of it.\n'
            'This is the same paragraph on a new line.',
            '* This is a list item\n* This is another list item'
        ]
        self.assertEqual(markdown_to_blocks(markdown), result)

    def test_markdown_to_blocks_newlines(self):
        markdown = """
# This is a heading



This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item
"""

        result = [
            '# This is a heading',

            'This is a paragraph of text. It has some **bold** and *italic* words inside '
            'of it.',

            '* This is a list item\n* This is another list item'
        ]
        self.assertEqual(markdown_to_blocks(markdown), result)

    def test_markdown_to_heading(self):
        block = "### This is a test heading."
        block_type = block_to_block_types(block)
        self.assertEqual(block_type, block_type_heading)

    def test_markdown_to_not_heading(self):
        block = "##4 This is a fake test heading"
        block_type = block_to_block_types(block)
        self.assertEqual(block_type, block_type_paragraph)
        pass

    def test_markdown_to_code_block(self):
        block = '```This is a test code block```'
        block_type = block_to_block_types(block)
        self.assertEqual(block_type, block_type_code)

    def test_markdown_to_not_code_block(self):
        block = '```This is a test code block``'
        block_type = block_to_block_types(block)
        self.assertEqual(block_type, block_type_paragraph)

    def test_markdown_to_quote_block(self):
        block = '> Test line 1\n> Test line 2\n> Test line 3'
        block_type = block_to_block_types(block)
        self.assertEqual(block_type, block_type_quote)

    def test_markdown_to_not_quote_block(self):
        block = '> Test line 1\n> Test line 2\nTest line 3'
        block_type = block_to_block_types(block)
        self.assertEqual(block_type, block_type_paragraph)

    def test_markdown_to_unordered_list(self):
        block = '- Test line 1\n- Test line 2\n- Test line 3'
        block_type = block_to_block_types(block)
        self.assertEqual(block_type, block_type_unordered_list)

    def test_markdown_to_unordered_list2(self):
        block = '* Test line 1\n* Test line 2\n* Test line 3'
        block_type = block_to_block_types(block)
        self.assertEqual(block_type, block_type_unordered_list)

    def test_markdown_to_unordered_list3(self):
        block = '- Test line 1\n- Test line 2\n* Test line 3'
        block_type = block_to_block_types(block)
        self.assertEqual(block_type, block_type_paragraph)

    def test_markdown_to_not_unordered_list(self):
        block = '- Test line 1\n- Test line 2\n Test line 3'
        block_type = block_to_block_types(block)
        self.assertEqual(block_type, block_type_paragraph)

    def test_markdown_to_ordered_list(self):
        block = '1. Test line 1\n2. Test line 2\n3. Test line 3'
        block_type = block_to_block_types(block)
        self.assertEqual(block_type, block_type_ordered_list)

    def test_markdown_to_not_ordered_list(self):
        block = '1. Test line 1\n2. Test line 2\n3 Test line 3'
        block_type = block_to_block_types(block)
        self.assertEqual(block_type, block_type_paragraph)


if __name__ == "__main__":
    unittest.main()
