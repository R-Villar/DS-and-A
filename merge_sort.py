def merger_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: find the midpoint of the lost and divide into sublist
    Conquer: Recursively sort the sublist created in the previous step
    Combine: Merge the sorted sublist created in previous step

    Takes O(kn log n) time
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merger_sort(left_half)
    right = merger_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublist
    Returns two sublist - left anf right

    Takes overall O(k log n) time
    """

    middle_index = len(list) // 2
    left_values = list[:middle_index]
    right_values = list[middle_index:]

    return left_values, right_values


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merge list

    Runs ib overall O(n) time
    """

    sorted_list = []
    i = 0  # keeps track of index in the left list
    j = 0  # keeps track of index in the right list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    #  accounts for scenario where the right list is shorted than the left
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    #  accounts for scenario where the left list is shorted than the left
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54, 44, 78, 35, 1, 41, 12, 21, 3, 7, 4]
l = merger_sort(alist)
print(alist)
print(verify_sorted(alist))
print(l)
print(verify_sorted(l))
