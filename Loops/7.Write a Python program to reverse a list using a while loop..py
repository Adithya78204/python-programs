#7.Write a Python program to reverse a list using a while loop.
numbers = [1, 2, 3, 4, 5]
reversed_list = []  # Create an empty list to store reversed elements
index = len(numbers) - 1  # Start from the last index

while index >= 0:
    reversed_list.append(numbers[index])  # Append elements in reverse order
    index -= 1  # Move to the previous index

print("Original list:", numbers)
print("Reversed list:", reversed_list)
