#4.Develop a function that takes a list of words as input and returns the longest word.
def longest_word(words):
    return max(words, key=len)

list = ["adhi", "pavan", "naren", "tarakaRam"]
print(longest_word(list))




