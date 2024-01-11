#!/usr/bin/python3
"""Module that prints a text with 2 new lines after special char"""


def text_indentation(text):
    """Function that prints and indentation of a string"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for wrd in text:
        if wrd == "":
            continue
        else:
            print(wrd, end="")
            if wrd in ('.', '?', ':'):
                print('\n')
    """ End the if statement"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    cha = 0
    while cha < len(text) and text[cha] == ' ':
        cha += 1

    while cha < len(text):
        print(text[cha], end="")
        if text[cha] == "\n" or text[cha] in ".?:":
            if text[cha] in ".?:":
                print("\n")
            cha += 1
            while cha < len(text) and text[cha] == ' ':
                cha += 1
            continue
        cha += 1
