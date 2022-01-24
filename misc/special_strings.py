#!/usr/bin/env python

class Trie:
    def __init__(self, is_word=False):
        self.children = {}
        self.is_word = is_word


    def add_word(self, word):
        node = self
        for letter in word:
            child = node.children.get(letter)
            if child:
                node = child
            else:
                child = Trie()
                node.children[letter] = child
                node = child
        node.is_word = True


    def is_special(self, word, trie=None, index=0, subwords_found=0):
        if not trie:
            trie = self
        child = trie.children.get(word[index])
        if not child:
            return False
        if index == len(word) - 1:
            # This is the last character in the word
            return child.is_word and subwords_found >= 1
        else:
            if child.is_word and self.is_special(word, self, index + 1, subwords_found + 1):
                return True
        return self.is_special(word, child, index + 1, subwords_found)


def special(words):
    trie = Trie()
    for word in words:
        trie.add_word(word)
    return [word for word in words if trie.is_special(word)]


words = ['f', 'o', 'bar', 'baz', 'bazinga', 'foofoo', 'foobarbaz', 'bazbara', 'oobazfobar', 'bazbazbara']

print(special(words))
