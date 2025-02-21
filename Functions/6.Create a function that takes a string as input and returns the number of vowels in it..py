#6.Create a function that takes a string as input and returns the number of vowels in it.
def num_of_vowels(string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in string if char in vowels)
    return count

string = "hello, welcome to the python"
print(num_of_vowels(string))
