#!python
from sorting_iterative import insertion_sort
from linkedList import LinkedList


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    # find max and min
    min, max = numbers[0], numbers[0]
    for index in range(len(numbers)):
        if numbers[index] > max:
            max = numbers[index]
        if min > numbers[index]:
            min = numbers[index]
    #  create temporary list
    temp_list = []
    for _ in range(max-min):
        temp_list.append(0)
    #  Fill temp list
    for index in range(len(numbers)):
        if numbers[index] == max:
            temp_list[len(temp_list)-1] += 1
            continue
        temp_list[numbers[index]-min] += 1
    numbers.clear()
    extend = 0
    for index in range(len(temp_list)):
        for _ in range(temp_list[index]):
            if index + 1 == max-min:
                #  We are going to add max value
                numbers.insert(index + extend, (min + index) + 1)
            else:
                numbers.insert(index + extend, min + index)  # index = numbers[value] - min
            extend += 1
    print(numbers)


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    load_factor = 0.75  # This will make the bucket sort dynamic.
    # if num_buckets is None:
    #     num_buckets = 1  # Default

    buckets = []  # Each bucket will contain a linked List
    for _ in range(num_buckets):
        buckets.append(LinkedList())
    min, max = numbers[0], numbers[0]
    for index in range(len(numbers)):
        if numbers[index] > max:
            max = numbers[index]
        if min > numbers[index]:
            min = numbers[index]

    for index in range(len(numbers)):
        linkedList_index = (numbers[index] * len(buckets)-1)//max
        sort_index = indexSort(buckets[linkedList_index].items(), numbers[index])
        if sort_index is None:
            buckets[linkedList_index].append(numbers[index])
        else:
            buckets[linkedList_index].insert_at_index(sort_index, numbers[index])

    number_index = 0
    for index in range(len(buckets)):
        bucket = buckets[index].items()
        for linkedIndex in range(len(bucket)):
            numbers[number_index] = bucket[linkedIndex]
            number_index += 1
    return numbers

        #  Insertion sort the linked list


def indexSort(list, value):
    """ Find index of where the value should be inserted"""
    index = 0
    if len(list) == 0:
        return 0
    if len(list) == 1:
        if list[0] > value:
            # list.insert(0, value)
            return 0
        else:
            # list.append(value)
            return None
    insertion = False
    for index in range(len(list)-1):
        if list[index] < value and value < list[index+1]:
            # list.insert(index + 1, value)
            index = index+1
            insertion = True
            break
    if insertion:
        return index
    else:
        if list[0] > value:
            # list.insert(0, value)
            return 0
        else:
            # list.append(value)
            return None


if __name__ == "__main__":
    list = [1, 5, 10, 2, 2, 3, 4, 6, 7, 20, 20, 100, 100, 3, 10]
    list2 = [0, 1, 2, 10, 12, 15, 20]
    counting_sort(list)
    print(bucket_sort(list))
    #  Find index
    # value = 4
    # print(indexSort(list2, value))
    # index = indexSort(list2, value)
    # if index is None:
    #     list2.append(value)
    # else:
    #     list2.insert(indexSort(list2, value), value)
    # print(list2)
