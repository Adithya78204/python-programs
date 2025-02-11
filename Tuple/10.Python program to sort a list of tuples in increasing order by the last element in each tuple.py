#10.Python program to sort a list of tuples in increasing order by the last element in each tuple
def sort_by_last_item_logic(tuple_list):
    n = len(tuple_list)

    # Bubble Sort Algorithm
    for i in range(n - 1):
        for j in range(n - i - 1):
            if tuple_list[j][-1] > tuple_list[j + 1][-1]:  # Compare last elements
                tuple_list[j], tuple_list[j + 1] = tuple_list[j + 1], tuple_list[j]  # Swap

    return tuple_list

# Example usage
tuple_list = [(1, 3, 5), (4, 1, 2), (2, 5, 8), (6, 2, 7)]
sorted_tuples = sort_by_last_item_logic(tuple_list)

print("Sorted Tuples:", sorted_tuples)

