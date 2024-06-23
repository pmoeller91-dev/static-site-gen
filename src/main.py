from textnode import TextNode
from shutil import rmtree
import os
from recursivecopy import recursive_copy
from generatepagesrecursive import generate_pages_recursive


def main():
    in_path = "./static"
    out_path = "./public"

    content_path = "./content/"
    template_path = "./template.html"

    print(f'Checking if output directory "{out_path}" exists...')
    if os.path.exists(out_path):
        print("Output directory exists, removing...")
        rmtree(out_path)
    else:
        print("OK, output directory does not exist.")

    print(f'Creating output directory "{out_path}"')
    os.mkdir(out_path)

    print(f'Beginning recursive copy from "{in_path}"...')
    recursive_copy(in_path, out_path)

    print("Beginning content generation...")
    generate_pages_recursive(content_path, template_path, out_path)


main()
