import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])


def find_smallest(values):
    smallest_index = 0
    for i in range(1, len(values)):
        if values[i] < values[smallest_index]:
            smallest_index = i
    return smallest_index


def selection_sort(values):
    sorted_list = []
    # print("%-25s %-25s" % (values, sorted_list))
    for i in range(len(values)):
        smallest = find_smallest(values)
        sorted_list.append(values.pop(smallest))
        # print("%-25s %-25s" % (values, sorted_list))
    return sorted_list


print(selection_sort(numbers))
