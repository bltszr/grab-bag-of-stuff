# project Euler number 10, I think?

import time

primeList = [2]
# def primOdd(n):
    # prim = True
    # for i in range(3, n, 2):
        # if n % i == 0:
            # prim = False
            # break
    # primeList.append(n)
    # return prim

def primeTest(n):
    prime = True
    for i in primeList:
        if n % i == 0:
            prime =se
            break
    if prime == True:
        primeList.append(n)
    return prime
    
def sumPrime(n):
    sum = 2
    for i in range(3, n, 2):
        if primeTest(i) == True:
            sum += i
    return sum

n = int(input("input number: "))
start = time.time()
print(sumPrime(n))

print(str(time.time()-start))