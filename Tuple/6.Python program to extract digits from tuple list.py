#6.Python program to extract digits from tuple list
def extract_digits(tuple_list):
    digits = []  # Create an empty list to store digits

    for tup in tuple_list:  # Loop through each tuple in the list
        for num in str(tup):  # Convert tuple elements to string and iterate
            if num.isdigit():  # Check if the character is a digit
                digits.append(int(num))  # Convert back to integer and add to list

    return digits  # Return the list of extracted digits


# Example usage
tuple_list = [(123, 45), (67, 89), (10, 2)]
result = extract_digits(tuple_list)
print("Extracted Digits:", result)
