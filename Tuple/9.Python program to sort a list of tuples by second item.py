#9.Python program to sort a list of tuples by second item
def sort_by_second_item(tuple_list):
    n = len(tuple_list)  # Get the length of the list

    # Bubble Sort Algorithm
    for i in range(n - 1):  # Outer loop for passes
        for j in range(n - i - 1):  # Inner loop for comparisons
            if tuple_list[j][1] > tuple_list[j + 1][1]:  # Compare second elements
                tuple_list[j], tuple_list[j + 1] = tuple_list[j + 1], tuple_list[j]  # Swap

    return tuple_list  # Return sorted list

tuple_list = [(1, 3), (4, 1), (2, 5), (6, 2)]
sorted_tuples = sort_by_second_item(tuple_list)

print("Sorted Tuples:", sorted_tuples)
