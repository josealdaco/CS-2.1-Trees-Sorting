#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    Running time: O(n) we're iterating over all elements
    Memory usage: O(1) we're not creating new memory
    """
    if len(items) <= 1:
        return True

    n = int(len(items)/2)
    t = n - 1
    weight = 1
    reverse = False
    while n < len(items):
        if items[t] > items[n]:
            return False
        if reverse is False:
            n -= weight
        if t == 0 and reverse is False:
            reverse = True
        if reverse is True:
            n += weight + 1
            t = n - 1
        else:
            t -= 1
    return True
    # TODO: Check that all adjacent items are in order, return early if so


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    Running time: avg O(n^2) because we have an outer loop iterating over all
    elements and an inner loop iterating over elements n - 1 - i
    Memory usage: O(1) we're never creating new memory and doing it in place.
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    if len(items) <= 1:
        return items
    r = 0
    amount = len(items)-1
    swap = False
    while amount != 0:
        try:
            if items[r] > items[r + 1]:
                value = items[r + 1]
                items.pop(r + 1)
                items.insert(r, value)
                swap = True
        except IndexError:
            r = amount
        r += 1
        if r >= amount:
            amount -= 1
            r = 0
            if swap is False:
                """ This will break if no changes have been made.
                Worst case is if the incorrect order is in the end ex.[1,2,3,4,5,-1]"""
                break
            swap = False
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    Running time: O(n^2) we have two loops iterating over all the elements
    Memory usage: O(1) we're never creating new memory and doing it in place.
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    if len(items) <= 1:
        return items
    amount = len(items)-1
    index = 1
    swap_index = 0
    min = items[0]
    minimum_index = 0
    while amount > 0:
        if min >= items[index]:
            min = items[index]
            minimum_index = index
        index += 1
        if index == len(items):
            value = items[swap_index]
            items.pop(swap_index)
            items.insert(swap_index, min)
            items.pop(minimum_index)
            items.insert(minimum_index, value)
            swap_index += 1
            index = swap_index
            amount -= 1
            min = items[index]

    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    Running time: O(n^2) because we have one loop iterating over all elements
    and a nested loop that also iterates over n-1 elements.
    Memory usage: O(1) we're never creating new memory and doing it in place.
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    index = 0
    minimum_index = 0
    while True:
        try:
            if items[index] > items[index + 1]:
                min = items[index + 1]
                minimum_index = index  #  3
                items.pop(index + 1)  # 12,5,6,8,10  #  5,6,8,12,10
                while True:
                    if min > items[index]:
                        items.insert(index + 1, min)
                        index = minimum_index
                        break
                    if index == 0:
                        items.insert(index, min)
                        index = minimum_index
                        break
                    index -= 1
        except IndexError:
            index = len(items)-1
        index += 1
        if index >= len(items):
            break
    return items


if __name__ == "__main__":
    print(is_sorted([-1, 1, 2, 3, 4, 5]))
    print(bubble_sort(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']))
    print(selection_sort(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']))
    print(insertion_sort([1, -3, -4, 5, 6, -1]))
