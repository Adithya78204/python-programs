#- Python program to count number of vowels using sets in given string
def count_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}  # Set of vowels
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count

text = "Hello, How are you?"
print("Number of vowels:", count_vowels(text))  # Output: 7



