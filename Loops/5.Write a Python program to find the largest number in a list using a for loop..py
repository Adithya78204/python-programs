#5.Write a Python program to find the largest number in a list using a for loop.
l = [2, 5, 9, 20, 32, 45, 36, 87]
largest = l[0]  # Initialize with the first element

for number in l:
    if number > largest:
        largest = number  # Update largest if current number is greater

print("The largest number is:", largest)  # Print the final largest number

#find largest and second largest numbers
l = [2, 5, 9, 20, 32, 45, 36, 87]
largest = second_largest = float('-inf')  # Initialize both with negative infinity
for number in l:
    if number > largest:
        second_largest = largest  # Update second largest before changing largest
        largest = number  # Update largest
    elif number > second_largest and number != largest:
        second_largest = number  # Update second largest if it's smaller than largest

print("The largest number is:", largest)
print("The second largest number is:", second_largest)
