import os

from markdown_blocks import markdown_to_blocks
from markdown_html import markdown_to_html_node


def extract_title(markdown):
    md_blocks = markdown_to_blocks(markdown)
    for block in md_blocks:
        if block.startswith('# '):
            return block[2:]
    raise Exception("Markdown file does not have a h1 level header.")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path}, to {dest_path}, using {template_path}")
    with open(from_path) as markdown_file:
        markdown_value = markdown_file.read()
    with open(template_path) as template_file:
        template_value = template_file.read()

    content_html = markdown_to_html_node(markdown_value).to_html()
    title_text = extract_title(markdown_value)
    template_value = template_value.replace('{{ Title }}', title_text)
    template_value = template_value.replace('{{ Content }}', content_html)
    dest_dirname = os.path.dirname(from_path)
    if not os.path.exists(dest_dirname):
        os.makedirs(dest_dirname)
    with open(dest_path, 'w') as write_file:
        write_file.write(template_value)
