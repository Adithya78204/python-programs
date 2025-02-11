def remove_tup(lst,k):
    empty_list = []

    for tup in lst:
        if len(tup) != k:
            empty_list.append(tup)
    return empty_list
tup_list = [(2,3),(1,23,3),(6,),(45,65,33),(65,12)]
k =1
result = remove_tup(tup_list,k)
print(result)
