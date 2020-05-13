#!python
from sorting_iterative import insertion_sort


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    Running time: O(n) it iterates of (n) items given
    Memory usage: O(n) we're storing (n) merged items in a new array.

    """

    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    index_One = 0
    index_Two = 0
    list = []
    while True:
        try:
            if items1[index_One] > items2[index_Two]:
                list.append(items2[index_Two])
                index_Two += 1
            else:
                list.append(items1[index_One])
                index_One += 1
        except Exception:
            """ Figure out which index is greater"""
            if index_One >= len(items1):
                for value in items2[index_Two:]:
                    list.append(value)
            else:
                for value in items1[index_One:]:
                    list.append(value)
            break
    return list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    Running time: avg O(n^2) because of insertion_sort
    Memory usage: O(n) because we're creating an array of (n) elements to merge
    """
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order
    list = insertion_sort(items)
    index = int(len(list)/2)
    first, second = list[:index], list[index:]
    result = merge(first, second)
    items[:] = result
    return
    # return list[:index], list[index:]


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    Running time: O(nlogn) for both because merge_sort is splitting the items in
    half each time and merge is taking both lists so (n) elements.
    Memory usage: O(n) because in each recursive call it creates a new array
    which take no more than (n) elements and after the merge it is deleted."""
    # TODO: Check if list is so small it's already sorted (base case)  10,9,8,7,6,5,4,3,2,1
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) > 1:
        middle_index = len(items)//2
        first_half = items[:middle_index]
        second_half = items[middle_index:]
        merge_sort(first_half)
        merge_sort(second_half)
        result = merge(first_half, second_half)
        for index in range(len(items)):
            items[index] = result[index]
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (the very first item) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Best case running time: O(nlogn) if you partition the middle in a sorted list
    Worst case running time: O(n^2) if the pivot is the first/last or you're
    sorting it and when it's already sorted
    Memory usage:
        - Best: O(logn) which depends on the tree height
        - Worst: O(n) this is usually the case when the running time is O(n^2)"""

    pivot = items[low]
    low_index, high_index = low, high

    while low_index < high_index:
        while items[low_index] <= pivot and low_index < high_index:
            low_index += 1
        while items[high_index] > pivot:
            high_index -= 1
        if (low_index < high_index):
            items[low_index], items[high_index] = items[high_index], items[low_index]
    items[low], items[high_index] = items[high_index], items[low]  # Swaps the pivot
    return high_index  # returns the index of the partition


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(nlogn) if you partition the middle in a sorted list
    Worst case running time: O(n^2) if the pivot is the first/last or you're
    sorting it and when it's already sorted
    Memory usage:
        - Best: O(logn) which depends on the tree height
        - Worst: O(n) this is usually the case when the running time is O(n^2)"""
    if low is None and high is None:
        low, high = 0, len(items) - 1

    # Check if list or range is so small it's already sorted (base case)
    if low < high:
        partitioned_loc = partition(items, low, high)
        quick_sort(items, low, partitioned_loc - 1)
        quick_sort(items, partitioned_loc + 1, high)


# if __name__ == "__main__":
