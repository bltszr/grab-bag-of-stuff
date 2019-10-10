"""
find the first number in the fibonacci sequence and its index with a certain length
project Euler no. 50: find the index of the first number in the fibonacci sequence 
which is 1000 digits long
"""
from time import time
fib_dict = {}

def fib(n):
    if n < 2: 
        return n
    elif not n in fib_dict :
            fib_dict[n]= fib(n-1) + fib(n-2)
    return fib_dict[n]

limit = int(input("length of fibonacci number: "))
start = time()
n = 1
i = 1

while len(str(fib(n))) < limit:
    n += 1
    i += 1

print("The fibonacci number is %d with the index %d \
done in the time of %f seconds" % ((fib(n)), i, ((time()-start) * 100)))