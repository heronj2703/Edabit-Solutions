# Create a function that takes a single string as argument
# and returns an ordered list containing the indices of all capital letters in the string.

def index_of_caps(word):
    return [word.find(char) for char in word if char.isupper()]
