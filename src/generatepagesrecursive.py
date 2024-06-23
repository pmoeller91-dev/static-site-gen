import os
from generatepage import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise ValueError(f"Content path does not exist: {dir_path_content}")
    if not os.path.exists(template_path):
        raise ValueError(f"Template does not exist: {template_path}")

    content_file_names = os.listdir(dir_path_content)
    for content_file_name in content_file_names:
        content_file_path = os.path.join(dir_path_content, content_file_name)
        if os.path.isdir(content_file_path):
            new_dest_dir_path = os.path.join(dest_dir_path, content_file_name)
            os.makedirs(new_dest_dir_path)
            generate_pages_recursive(
                content_file_path, template_path, new_dest_dir_path
            )

        content_file_name_parts = os.path.splitext(content_file_name)
        content_file_basename = content_file_name_parts[0]
        content_file_ext = content_file_name_parts[1]

        if content_file_ext != ".md":
            continue

        dest_file_name = f"{content_file_basename}.html"
        dest_file_path = os.path.join(dest_dir_path, dest_file_name)

        generate_page(content_file_path, template_path, dest_file_path)
