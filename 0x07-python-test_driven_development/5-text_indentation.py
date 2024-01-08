#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', "?", ":"]
    lines = []
    start = 0

    for i, char in enumerate(text):
        if char in separators:
            lines.append(text[start:i+1].strip())
            start = i + 1

    if start < len(text):
        lines.append(text[start:].strip())

    for line in lines:
        print(line)
