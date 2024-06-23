import re


def extract_markdown_images(text):
    markdown_images_regex = r"!\[(.*?)\]\((.*?)\)"
    non_capturing_regex = r"!\[(?:.*?)\]\((?:.*?)\)"
    return re.findall(markdown_images_regex, text), re.split(non_capturing_regex, text)
