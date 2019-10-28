"""
Project Euler number 39.
Find the perimeter of a right triangle below 1000 such that
the number of possible sidelength combinations it can have is
the maximum.

Sidenote: a previous plan of implementation for this
required a primitive pythagorean triple generator, however that
might not be entirely necessary.
"""
from math import sqrt
from time import time
def integerSum(limit):
    max = 0
    maxperi = 0
    for i in range(1, limit):
        combinations = [(x, y) for x in range(1, i) for y in range(1, i) if (sqrt(x**2 + y**2) + x + y) == i]
        if len(combinations) >= max:
            maxperi = i
            max = len(combinations)
    return maxperi, max

if __name__ == "__main__":
    limit = int(input("Provide limit: "))
    start = time()
    x, y = integerSum(limit)
    end = time()
    print("The number of combinations is %d for the perimeter %d solved in the time of %f" % (y, x, (end-start)))