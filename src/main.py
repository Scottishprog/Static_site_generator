import os
import shutil
from copystatic import copy_tree

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


path_source = './static'
path_dest = './public'


def main():
    print("Deleting public directory if necessary...")
    if os.path.exists(path_dest):
        shutil.rmtree(path_dest)
        os.mkdir(path_dest)

    print(f'Copying files from {path_source} to {path_dest}...')
    copy_tree(path_source, path_dest)


main()
