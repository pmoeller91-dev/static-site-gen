from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "Paragraph"
    HEADING = "Heading"
    CODE = "Code"
    QUOTE = "Quote"
    UNORDERED_LIST = "UnorderedList"
    ORDERED_LIST = "OrderedList"
