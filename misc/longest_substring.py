#!/usr/bin/env python

from ipdb import set_trace


def length_of_longest_substring(string):
    longest = 0
    for i in range(string):
        j = substring(string, i)
        if j - i > longest:
            longest = j - i
    return longest


def substring(string, start):
    chars = set()
    for i, char in enumerate(string[start:], start):
        if char in chars:
            return i
        chars.add(char)
    return len(string)

print(length_of_longest_substring('dvdf'))
