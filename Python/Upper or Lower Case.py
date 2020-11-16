# Return the smallest number of steps it takes to convert a string entirely into uppercase or entirely into lower case,
# whichever takes the fewest number of steps.
# A step consists of changing one character from lower to upper case, or vice versa.

def steps_to_convert(txt):
    uppercase = sum(1 for char in txt if char.isupper())
    lowercase = sum(1 for char in txt if char.islower())
    return lowercase if lowercase < uppercase else uppercase
