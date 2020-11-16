# Create a function that replaces all the vowels in a string with a specified character.

def replace_vowels(txt, ch):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for vowel in vowels:
        if vowel in txt:
            txt = txt.replace(vowel, ch)
    return txt
