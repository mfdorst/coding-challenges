#!/usr/bin/env python

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    return diameter(tree)


def diameter(tree):
    l, d = longest_path_and_diameter(tree)
    return d


def longest_path_and_diameter(tree):
    if not tree.left and not tree.right:
        return 0, 0
    if tree.left:
        left_longest, left_diameter = longest_path_and_diameter(tree.left)
        if not tree.right:
            return left_longest + 1, max(left_longest + 1, left_diameter)
    if tree.right:
        right_longest, right_diameter = longest_path_and_diameter(tree.right)
        if not tree.left:
            return right_longest + 1, max(right_longest + 1, right_diameter)

    return max(left_longest, right_longest) + 1, max(left_longest + right_longest + 2, left_diameter, right_diameter)


def max(a, b, c=None):
    max_ab = a if a > b else b
    return (max_ab if max_ab > c else c) if c else max_ab



print(longest_path_and_diameter(None))
print(longest_path_and_diameter(Node(None, None)))

tree = Node(Node(), None)

print(longest_path_and_diameter(tree))

tree = Node(Node(), Node())

print(longest_path_and_diameter(tree))

tree = Node(Node(Node(), Node(None, Node())), Node())

print(longest_path_and_diameter(tree))

tree = Node(Node(Node(), Node(None, Node())), Node(None, Node()))

print(longest_path_and_diameter(tree))

tree = Node(Node(Node(Node(), Node(None, Node())), Node(None, Node())))

print(longest_path_and_diameter(tree))
