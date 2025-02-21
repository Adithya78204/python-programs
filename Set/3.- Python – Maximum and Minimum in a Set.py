#3.- Python – Maximum and Minimum in a Set

numbers = {2,4,6,8,32,54,67,98,78,5,3,1}

max_values = max(numbers)
min_values = min(numbers)

print("max values is:",max_values)
print("min value is:",min_values)

#using for loop

# Define a set
numbers = {10, 45, 2, 89, 23, 67}

# Initialize max and min with first element
max_value = min_value = next(iter(numbers))

# Iterate through the set
for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

# Print results
print("Maximum value:", max_value)
print("Minimum value:", min_value)



numbers = {2,3,5,34,56,6,87,9,32}

min_value = max_value =next(iter(numbers))




















