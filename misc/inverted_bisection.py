#!/usr/bin/env python

class Link:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def invertedBisection(lst):
    return inverted_bisection(lst)

def inverted_bisection(lst):
    length = list_len(lst)
    if length == 1:
        return lst
    l1 = lst
    if length % 2 == 0:
        l2 = split_list(l1, length // 2)
        l1, l2 = invert_list(l1), invert_list(l2)
        return join_list(l1, l2)
    else:
        m = split_list(l1, length // 2)
        l2 = split_list(m, 1)
        l1, l2 = invert_list(l1), invert_list(l2)
        return join_list(join_list(l1, m), l2)


def join_list(l1, l2):
    n = l1
    while n.next:
        n = n.next
    n.next = l2
    return l1


def split_list(lst, n):
    node = lst
    for i in range(n - 1):
        node = node.next
    nxt = node.next
    node.next = None
    return nxt


def invert_list(lst):
    if not lst:
        return None
    if not lst.next:
        return lst
    n1 = lst
    n2 = n1.next
    n3 = n2.next if n2 else None
    n1.next = None
    while n3:
        n2.next = n1
        n1 = n2
        n2 = n3
        n3 = n3.next
    n2.next = n1
    return n2


def list_len(lst):
    n = lst
    length = 0
    while n:
        length += 1
        n = n.next
    return length


def print_list(lst):
    if not lst:
        return
    node = lst
    while node.next:
        print(f'{node.value} -> ', end='')
        node = node.next
    print(node.value)


lst = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6, Link(7)))))))

print_list(lst)

print_list(inverted_bisection(lst))