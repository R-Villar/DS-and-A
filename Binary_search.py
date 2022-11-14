def binary_search(list1, item):
    low = 0
    high = len(list1) - 1

    while low <= high:
        # check the middle of the element
        mid = (low + high) // 2
        guess = list1[mid]
        # checks if the middle element is the item we are looking for
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    # returns none if the item is not in the list
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(my_list, 5))
print(binary_search(my_list, -1))
