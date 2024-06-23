import os
from shutil import copy


def recursive_copy(source_path, target_path):
    if not os.path.exists(source_path):
        raise ValueError(f"Source path does not exist: {source_path}")
    if not os.path.exists(target_path):
        raise ValueError(f"Target path does not exist: {target_path}")

    if not os.path.isdir(source_path):
        raise ValueError(f"Source path is not a directory: {source_path}")
    if not os.path.isdir(target_path):
        raise ValueError(f"Target path is not a directory: {target_path}")

    source_file_names = os.listdir(source_path)

    for source_file_name in source_file_names:
        source_file_path = os.path.join(source_path, source_file_name)
        target_file_path = os.path.join(target_path, source_file_name)
        if os.path.isfile(source_file_path):
            print(f'Copying file "{source_file_path}" to "{target_file_path}"')
            copy(source_file_path, target_file_path)
        elif os.path.isdir(source_file_path):
            print(f'Creating new directory "{target_file_path}"')
            os.mkdir(target_file_path)
            recursive_copy(source_file_path, target_file_path)
