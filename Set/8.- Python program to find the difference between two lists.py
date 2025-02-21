#- Python program to find the difference between two lists
def diff_lists (list1, list2):
    difference = []

    for item in list1:
        if item not in list2:
            difference.append(item)

    for item in list2:
        if item not in list1:
            difference.append(item)
    return difference
print(diff_lists([2,3,4,5], [4,5,6,7]))