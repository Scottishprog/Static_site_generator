import unittest

from markdown_html import (
    block_quote_to_html_node,
    markdown_to_html_node
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_block_quote_to_html(self):
        block = """
> Test
> **block**
> quote"""
        parent_node = markdown_to_html_node(block)
        expected_result = '<div><blockquote>Test <b>block</b> quote</blockquote></div>'
        self.assertEqual(expected_result, parent_node.to_html())

    def test_block_quote_invalid(self):
        block = """
> Test
 **block**
> quote"""
        with self.assertRaises(ValueError):
            block_quote_to_html_node(block)

    def test_unordered_list_to_html(self):
        block = """
- Test
- Unordered
- List with a **bold** entry
"""
        parent_node = markdown_to_html_node(block)
        expected_result = '<div><ul><li>Test</li><li>Unordered</li><li>List with a <b>bold</b> entry</li></ul></div>'
        self.assertEqual(expected_result, parent_node.to_html())

    def test_ordered_list_to_html(self):
        block = """
1. Test
2. block
3. quote with a **bold** entry
"""
        parent_node = markdown_to_html_node(block)
        expected_result = '<div><ol><li>Test</li><li>block</li><li>quote with a <b>bold</b> entry</li></ol></div>'
        self.assertEqual(expected_result, parent_node.to_html())

    def test_code_block_to_html(self):
        block = """
```
Test block code
And a bit more code
```     
"""
        parent_node = markdown_to_html_node(block)
        expected_result = """<div><pre><code>
Test block code
And a bit more code
</code></pre></div>"""
        self.assertEqual(expected_result, parent_node.to_html())

    def test_heading_to_html(self):
        block = """
# Test Heading(h1)

Paragraph

### Smaller **Heading** (h3)
"""
        parent_node = markdown_to_html_node(block)
        expected_result = '<div><h1>Test Heading(h1)</h1><p>Paragraph</p><h3>Smaller <b>Heading</b> (h3)</h3></div>'
        self.assertEqual(expected_result, parent_node.to_html())

    def test_paragraph_to_html(self):
        block = "A generic paragraph\nsupposedly containing information."
        parent_node = markdown_to_html_node(block)
        expected_result = '<div><p>A generic paragraph supposedly containing information.</p></div>'
        self.assertEqual(expected_result, parent_node.to_html())
