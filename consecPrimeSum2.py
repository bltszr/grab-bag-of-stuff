# second approach where we accumulate all primes first, and then subtract one by one until we find the prime
# first rendition of this program went from the top prime until it finds a prime number. this is apparently wrong
# this always gives wrong answers

import time
primeList = [2, 3]

def primeTest(n):
    prime = True
    for i in primeList:
        if n % i == 0:
            prime = False
            break
    return prime

def consecPrimeSum(n):
    prime = 5
    primeSum = 5
    while primeSum < n:
        if primeTest(prime) == True:
            primeList.append(prime)
            primeSum += prime
            prime += 2
        else:
            prime += 2
            continue
    for i in primeList:
        if primeTest(primeSum) == False:
            primeSum -= i
        else:
            print(i, prime)
            break
    return primeSum

n = int(input("input number: "))
start = time.time()
x = consecPrimeSum(n)
print("the sum is %d" % (x), "\ntime est. %f seconds" % ((time.time() - start) * 100))