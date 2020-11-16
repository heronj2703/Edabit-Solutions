# Create a function that moves all capital letters to the front of a word.


def cap_to_front(s):
    lst = list(s)
    str1 = ''.join(char for char in lst if char.isupper())
    str2 = ''.join(char for char in lst if char.islower())
    return str1 + str2



