import re


def extract_markdown_links(text):
    markdown_links_regex = r"(?<!!)\[(.*?)\]\((.*?)\)"
    non_capturing_regex = r"(?<!!)\[(?:.*?)\]\((?:.*?)\)"
    return re.findall(markdown_links_regex, text), re.split(non_capturing_regex, text)
