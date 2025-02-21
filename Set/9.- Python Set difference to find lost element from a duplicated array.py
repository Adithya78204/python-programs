#9.- Python Set difference to find lost element from a duplicated array
def find_lost_element(original, duplicate):
    for item in original:
        if item not in duplicate:
            return item  # Found the missing element

# Example usage
original = [1, 2, 3, 4, 5]
duplicate = [2, 3, 1, 5]  # 4 is missing

print("Lost element:", find_lost_element(original, duplicate))  # Output: 4
