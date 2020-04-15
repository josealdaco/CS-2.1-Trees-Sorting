#!python
from sorting_iterative import insertion_sort


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
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
    TODO: Memory usage: ??? Why and under what conditions?"""
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
    TODO: Memory usage: ??? Why and under what conditions?"""
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
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # Pivot will start in the middle, between low and high given points
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pivot_point = ((high)+low)//2
    print("Pivot point", pivot_point, "low", low, "high", high)
    pivot = items[pivot_point]  # start in the middle
    low_index, high_index = low, high
    dict_index = {"low": [],
                  "high": [],
                  "list": []
                  }
    while low_index < pivot_point and high_index > pivot_point:
        if items[low_index] > pivot:
            dict_index["low"].append(low_index)
        else:
            dict_index["list"].append(("low", low_index))
        print("High index", high_index, items)
        if items[high_index] < pivot:
            dict_index["high"].append(high_index)
        else:
            dict_index["list"].append(("high", high_index))
        low_index += 1
        high_index -= 1
    #  Add pivot to the last in low section
    #  Change later
    temp_list = []
    dict_index['list'].insert(0, ('high', pivot_point))
    for index in range(len(dict_index['list'])):
        if dict_index['list'][index][0] == 'low':
            temp_list.insert(0, items[dict_index['list'][index][1]])
        else:
            temp_list.append(items[dict_index['list'][index][1]])
    for lower in range(len(dict_index['low'])):
        temp_list.append(items[dict_index['low'][lower]])
        if pivot_point > 0:
            pivot_point -= 1
    for higher in range(len(dict_index['high'])):
        temp_list.insert(0, items[dict_index['high'][higher]])
        pivot_point += 1
    print("Items", items, "temp", temp_list)
    items.clear()
    for final_index in range(len(temp_list)):
        items.append(temp_list[final_index])
    return pivot_point


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    # Check if high and low range bounds have default values (not given)
    if low is None and high is None:
        low, high = 0, len(items) - 1

    # Check if list or range is so small it's already sorted (base case)
    if high > 1:
        # Partition items in-place around a pivot and get index of pivot
        # O(n): iterates the entire list
        partitioned_loc = partition(items, low, high)
        # Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, partitioned_loc)
        print("Partition", partitioned_loc, items)
        quick_sort(items, partitioned_loc + 1, high-1)
    return


if __name__ == "__main__":
    #  Merge
    print(merge_sort([3, 15, 4, 7, 20, 6, 18, 11, 9, 7]))
    list = [41, 3, 15, 4, 1, 20, 51, 18, 11, 9, 7]
    quick_sort(list)
