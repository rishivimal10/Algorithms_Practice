"""
Problem:
# Write a program that takes an array A and an index i into A,
# and rearranges the elements such that all elements less than A[r] (the "pivot") appear first,
# followed by elements equal to the pivot, followed by elements greater than the pivot.
#
# suppose A = [0,1,2,0,2,1,1], and the pivot index is 3. Then A[3] = 0, so
# [0,0,1,2,2,1,1] is a valid partitioning. For the same array, if the pivot index is 2, then A[2] = 2,
# the arrays [0,1,0,1,1,2,2] as well as [0,0, 1,1,1,2,2] are valid partitionings.

High-Level Breakdown of my Algorithm:
    - First Pass:
        - Go through array and move all values less than the pivot value to back of list
    - Reverse the list
    - Second Pass:
        - Go through list and move all values greater than pivot to the back of list

    Time Complexity = O(n)
    Space Complexity = O(1)
"""


def dutch_national_flag_solution(array, index):
    pivot_value = array[index]
    left, right = 0, len(array) - 1

    while left < right:
        if array[left] < pivot_value:
            array.append(array[left])
            array.pop(left)
            right -= 1
        else:
            left += 1

    array.reverse()

    left, right = 0, len(array) -1

    while left < right:
        if array[left] > pivot_value:
            array.append(array[left])
            array.pop(left)
            right -= 1
        else:
            left += 1

    return array


def is_solution(sorted_array, pivot):

    first_pivot_index = sorted_array.index(pivot)
    pivot_count = sorted_array.count(pivot)
    ctr = 0

    while ctr < first_pivot_index:
        if not sorted_array[ctr] < pivot:
            return False
        ctr += 1
    stop_index = ctr
    while ctr < (stop_index + pivot_count):
        if not sorted_array[ctr] == pivot:
            return False
        ctr += 1

    while ctr < len(sorted_array):
        if not sorted_array[ctr] > pivot:
            return False
        ctr += 1

    return True
