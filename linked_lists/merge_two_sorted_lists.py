from list_node import ListNode

"""
Problem:
#Write a program that takes two lists, assumed to be sorted, and returns their merge.
#The only field your program can change in a node is its next field.
"""


def merge_two_sorted_lists_solution(list1, list2):

    temp = current = ListNode()
    while list1 and list2:

        if list2 < list1:
            current.next = list2
            list2 = list2.next
        else:
            current.next = list1
            list1 = list1.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return temp.next

