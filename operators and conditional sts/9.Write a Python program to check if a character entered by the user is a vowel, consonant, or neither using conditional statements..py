#9.Write a Python program to check if a character entered by the user is a vowel, consonant, or neither using conditional statements.
def check_character(ch):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

    if ch in vowels:
        print(ch, "is a Vowel")
    elif ch in consonants:
        print(ch, "is a Consonant")
    else:
        print(ch, "is neither a Vowel nor a Consonant")

char = input("Enter a character: ")
if len(char) == 1:  #only a single character is checked
    check_character(char)
else:
    print("Please enter only one character.")




