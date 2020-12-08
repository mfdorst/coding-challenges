#!/usr/bin/env python


class Link:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def mergeLinkedLists(list_a, list_b):
    if not list_a:
        return list_b
    if not list_b:
        return list_a
    
    result = list_a if list_a.value < list_b.value else list_b

    while list_a and list_b:
        while list_a.next and list_a.next.value <= list_b.value:
            list_a = list_a.next
        if list_a.value <= list_b.value:
            temp = list_a.next
            list_a.next = list_b
            list_b = temp
        else:
            temp = list_a
            list_a = list_b
            list_b = temp
    return result


def print_list(list):
    while list:
        print(list.value, end=' ')
        list = list.next
    print()


list_a = Link(1, Link(4, Link(5)))
list_b = Link(2, Link(3))

print_list(merge_lists(list_a, list_b))


list_a = Link()
list_b = Link()

print_list(merge_lists(list_a, list_b))
