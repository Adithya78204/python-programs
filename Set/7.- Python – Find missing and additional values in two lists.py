#- Python – Find missing and additional values in two lists
def mis_add_values(list1, list2):
    missing = []
    additional = []
    for item in list1:
        if item not in list2:
            missing.append(item)

    for item in list2:
        if item not in list1:
            additional.append(item)

    return missing,additional
list1 = [2,3,4,5]
list2 = [4,5,6,7]
missing,additional = mis_add_values(list1,list2)
print("missing values:", missing)
print("additional values:", additional)
