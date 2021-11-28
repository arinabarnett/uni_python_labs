# -*- coding: utf-8 -*-
'''
Module for text statistics calculation.
'''

import sys
from collections import defaultdict


def get_char_frequencies(text):
    result = defaultdict(dict)
    length = len(text)
    for i in range(0, length):
        letter = text[i]
        counted = text.count(letter)
        result[letter] = counted
    return result

def get_unique_words(text):
    words = text.split()
    return set(words)

def main():
    print(get_char_frequencies(u"abc"))
    print(get_unique_words("to be or not to be"))
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
