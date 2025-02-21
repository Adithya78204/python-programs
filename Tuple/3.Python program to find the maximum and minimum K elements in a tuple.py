#.3.Python program to find the maximum and minimum K elements in a tuple.py
def find_min_max_k(tup, k):
    temp_list = list(tup)   # convert tuple to list cuz tuple is immutable

    min_k = []        # assinging value purpose taking
    for i in range(k):  # k loop for repeatation
        smallest = min(temp_list) # Find the smallest number
        min_k.append(smallest)  #Store in result list
        temp_list.remove(smallest) # Remove from list to find the next smallest

    temp_list = list(tup)

    max_k = []
    for i in range(k):
        largest = max(temp_list)
        max_k.append(largest)
        temp_list.remove(largest)

    return min_k, max_k
my_tuple = (3,2,5,76,45,87,45,68,4,21)
k = 3
min_k_elements, max_k_elements = find_min_max_k(my_tuple, k)
print(min_k_elements)
print(max_k_elements)














def min_max_k(tup, k):
    temp_list = list(tup)

    min_k = []
    for i in range(k):
        smallest = min(temp_list)
        min_k.append(smallest)
        temp_list.remove(smallest)

    temp_list = list(tup)

    max_k = []
    for i in range(k):
        largest = max(temp_list)
        max_k.append(largest)
        temp_list.remove(largest)

    return min_k, max_k
my_tuple = (2,3,54,65,23,45,6,78,9)
k = 2
min_k_elements, max_k_elements = find_min_max_k(my_tuple, k)
print(min_k_elements)
print(max_k_elements)
