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
    dest_dirname = os.path.dirname(dest_path)
    if not os.path.exists(dest_dirname):
        print(f'Making directory: {dest_dirname}')
        os.makedirs(dest_dirname)
    with open(dest_path, 'w') as write_file:
        write_file.write(template_value)


def generate_page_recursive(dir_path_content, template_path, dest_path):
    for path in os.listdir(dir_path_content):
        source_file_path = os.path.join(dir_path_content, path)
        if os.path.isfile(source_file_path):
            file_name = path.split('.')
            file_name = file_name[0]
            file_name = file_name + '.html'
            dest_file_path = os.path.join(dest_path, file_name)
            generate_page(source_file_path,
                          template_path,
                          dest_file_path)
        else:
            generate_page_recursive(os.path.join(dir_path_content, path),
                                    template_path,
                                    os.path.join(dest_path, path))
