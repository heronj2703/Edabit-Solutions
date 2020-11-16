# Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times.
# The paper starts off with a thickness of 0.5mm.

def num_layers(n):
    return str(0.0005 * 2 ** n) + "m"

