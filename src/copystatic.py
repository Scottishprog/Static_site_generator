import os
import shutil


def copy_tree(source, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
    for file in os.listdir(source):
        source_path = os.path.join(source, file)
        dest_path = os.path.join(dest, file)
        if os.path.isfile(source_path):
            print(shutil.copy(source_path, dest))
        if os.path.isdir(source_path):
            copy_tree(source_path, dest_path)