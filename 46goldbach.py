"""
project Euler number 46: Goldbach's other conjecture
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
as thus: n = p + 2(k^2)
This was proven to be false.
Find the smallest number for which this case is not true.
Note thus that prime numbers (p) can be expressed as n - 2(k^2)
"""
import time


"""
this one is way too slow

def primOdd(n): # for odd numbers only
    prim = True
    for i in range(3, n, 2):
        if n % i == 0:
            prim = False
            break
    return prim

start = time.time()
isFound = False
n = 9
while isFound == False:
    k = 1
    p = n - (2 * (k ** 2))
    while primOdd(n) == True:
        n += 2
    while primOdd(p) == False:
        if k > n:
            isFound = True
            break
        k += 1
    else:
        continue
        
print("The smallest counterexample for Goldbach's other conjecture is %d found in the time of %f seconds" % (n, (time.time()-start)))
"""

compOddGen = []
def goldbach(limit, x, y):
    compOddGen.extend([x * y for x in range(3, limit, 2) for y in range(2, x + 1)])
    