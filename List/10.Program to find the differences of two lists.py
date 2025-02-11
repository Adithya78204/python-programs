#10.Program to find the differences of two lists.py
def list_diff(list1, list2):
    diff1 = list(set(list1) - set(list2)) #convert list into set
    diff2 = list(set(list2) - set(list1))
    return diff1, diff2

list1 = [2,3,4,5,6,7]
list2 = [5,6,7,8,9,10]

diff1, diff2 = list_diff(list1, list2)
print(diff1)
print(diff2)



