#!/usr/bin/python3
"""Text indentation module."""


def text_indentation(text):
    """
    Indents two newlines after any . ? or :
    text must be a string, otherwise TypeError
    There should be no space at the beg. or end of each printed line

    Args:
        text: text to be indented
        """
    if text is None:
        raise TypeError("text must be a string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    newtext = None

    for i in range(len(text)):
        if text[i - 1] == '.' or text[i - 1] == '?' or text[i - 1] == ':':
            if text[i] == ' ':
                continue
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
            continue
        else:
            if text[i - 1] != ':':
                print(text[i], end='')
            else:
                continue
