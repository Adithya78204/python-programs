#8.Python program to join tuples if similar initial element
def join_tuples(tuple_list):
    result = {}  # Dictionary to store tuples grouped by the first element

    for tup in tuple_list:  # Loop through each tuple
        key = tup[0]  # Get the first element as key
        if key in result:
            result[key] += tup[1:]  # Join tuples by adding remaining elements
        else:
            result[key] = tup  # Store the first occurrence of a tuple

    return list(result.values())  # Convert dictionary values back to list of tuples

# Example usage
tuple_list = [(1, 2, 3), (2, 4), (1, 5, 6), (3, 7), (2, 8, 9)]
result = join_tuples(tuple_list)
print("Joined Tuples:", result)
