#!/usr/bin/python3

"""
File That contains a function called
append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that appends substring inside a string in txt
    """
    with open(filename, mode="r+", encoding="utf-8") as file:
        content: str = file.read()
        new_string: str = new_string.replace("\n", "")
        contents: list[str] = content.split("\n")
        positions: list[int] = [
                i + 1
                for i, text in enumerate(contents)
                if search_string in text
        ]

        for position in positions:
            contents.insert(position, new_string)

        new_text: str = "\n".join(contents)
        file.write(new_text)
