# A set is a collection of unique items. A set can be formed from a list from removing all duplicate items.

def setify(lst):
    lst = list(set(lst))
    lst.sort()
    return lst
