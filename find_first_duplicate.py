def find_first_duplicate(arr):
    seen = set()

    for i in arr:

        if i in seen:
            return i
        seen.add(i)
    return -1


print(find_first_duplicate([2, 1, 3, 3, 2]))
print(find_first_duplicate([1, 2, 3, 4]))
print(find_first_duplicate([]))
print(find_first_duplicate([7, 1, 2, 3, 7]))