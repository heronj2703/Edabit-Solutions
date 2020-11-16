# Create a function that counts the number of times a particular letter shows up in the word search.

def letter_counter(lst, letter):
    total = 0
    for row in lst:
        total += row.count(letter)
    return total


