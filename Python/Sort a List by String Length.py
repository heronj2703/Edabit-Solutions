# Create a function that takes a list of strings and return a list, sorted from shortest to longest.

def sort_by_length(lst):
    return sorted(lst, key=len)
