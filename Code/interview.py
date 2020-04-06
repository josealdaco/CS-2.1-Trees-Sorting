#  array of n,  target  sum = t. not sortet - to +

#
# def sumValue(list, target):
#     for index in range(len(list)):
#         for second_index in range(len(list) - index):
#             if list[second_index + 1] + list[index] == target:
#                 return (list[index+ 1], list[second_index])
#     return False


# two arrays of n each, find pair of number t

#
# def sumtwoLists(listOne, listTwo, target):
#     index = len(listOne)
#     tupleList = []
#     for index in range(len(listOne)):
#         if listOne[index] + listTwo[index] == target:
#             tupleList.append((listOne[index], listTwo[index]))
#         else:
#             tupleList.insert(0, (listOne[index], listTwo[index]))
#     return tupleList[len(tupleList)-1]
#

#(1) -> (2) -> (3) -> (4)
#  class Reverse, recursive add .Next to list and start from tail to list-1


if __name__ == "__main__":
    # print(sumValue([1,2,3,4,5,6,7,8], 8))
    print(sumtwoLists([1,2,3,4,5], [6,7,8,9,10], 14))
