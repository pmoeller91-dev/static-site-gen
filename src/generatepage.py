import os
from markdowntohtmlnode import markdown_to_html_node
from extracttitle import extract_title


def generate_page(from_path, template_path, dest_path):
    title_placeholder = "{{ Title }}"
    content_placeholder = "{{ Content }}"
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    template = ""
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()

    generated_html = markdown_to_html_node(markdown).to_html()
    extracted_title = extract_title(markdown)

    template_with_title = template.replace(title_placeholder, extracted_title)
    template_with_content = template_with_title.replace(
        content_placeholder, generated_html
    )

    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    
    with open(dest_path, 'w', encoding="utf-8") as f:
        f.write(template_with_content)
    