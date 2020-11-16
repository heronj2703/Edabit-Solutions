# Jay and Silent Bob have been given a fraction of an ounce but they only understand grams.
# Convert a fraction passed as a string to grams with up to two decimal places.
# An ounce weighs 28 grams.
# Easy


def jay_and_bob(txt):
    def minimal_number(x):
        if type(x) is str:
            if x == '':
                x = 0
        f = float(x)
        if f.is_integer():
            return int(f)
        else:
            return f

    conversion_table = {
        'half': 2,
        'quarter': 4,
        'eighth': 8,
        'sixteenth': 16
    }
    output = minimal_number(28 / conversion_table[txt])
    return str(output) + " grams"

