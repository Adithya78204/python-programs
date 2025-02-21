#- Python program to find common elements in three lists using sets
def common_elements(list1, list2, list3):
    common = []
    for item in list1:
        if item in list2 and item in list3:
            common.append(item)
    return common
print(common_elements([2,3,5],[4,5,6],[5,7,8]))

