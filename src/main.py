import os
import shutil
from copystatic import copy_tree
from gencontent import generate_page_recursive


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    path_source = './static'
    path_dest = './public'
    path_content = './content'
    path_template = './template.html'

    print("Deleting public directory if necessary...")
    if os.path.exists(path_dest):
        shutil.rmtree(path_dest)
        os.mkdir(path_dest)

    print(f'Copying files from {path_source} to {path_dest}...')
    copy_tree(path_source, path_dest)

    # generate_page(os.path.join(path_content, 'index.md'), path_template, os.path.join(path_dest, 'index.html'))
    generate_page_recursive(path_content, path_template, path_dest)


main()
