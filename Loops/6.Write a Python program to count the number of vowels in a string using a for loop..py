#6.Write a Python program to count the number of vowels in a string using a for loop.
def count_vowels(string):
    vowels = "aeiouAEIOU"  # Define vowels (both lowercase and uppercase)
    count = 0  # Initialize vowel count

    for char in string:
        if char in vowels:
            count += 1  # Increment count if the character is a vowel

    return count

# Example usage
text = "Hello, how are you?"
print("Number of vowels:", count_vowels(text))
