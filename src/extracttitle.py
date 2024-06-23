import re


def extract_title(markdown):
    title_regex = r"^\s*# (.+)$"
    matched_title = re.search(title_regex, markdown, flags=re.MULTILINE)
    if not matched_title:
        raise ValueError("Markdown does not contain a title")
    return matched_title.group(1)
