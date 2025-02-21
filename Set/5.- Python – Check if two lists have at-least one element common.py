#5.- Python – Check if two lists have at-least one element common
def common_element(list1, list2):
    return bool(set(list1) & set(list2))

list1 = [2,3,4,5]
list2 = [5,6,7,8]
print(common_element(list1,list2))

#uing for loop
def common_element(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

print(common_element([2,3,4],[4,5,6])) #true
print(common_element([7,8,9],[1,2,3])) #false