"""
Project Euler number 15.
The goal is to calculate all possible combinations of
paths to get from one corner to another. Notice that
the number of steps never change, and it will always
be length of the two sides of the square, as one of
the possible paths. Notice also that the number of
steps per direction never changes, and it will also
be the number of each step. This means that the formula
will simply be a permutation formula of the number 
of steps choosing the number of steps per direction.
Refer to this https://www.youtube.com/watch?v=wc1hZpDPQFA
"""

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
sideLength = int(input("Provide the side length of the path: "))
print("The number of combinations is", (fac(sideLength * 2) / fac(sideLength) ** 2))
