# find the prime below 1000000 which can be written as a sum of a sequence of consecutive primes (e.g. 2, 3, 5, 7, 11, 13, and so on)
# example the longest one below 100 is 41 which is the sum of 2, 3, 5, 7, 11, and 13
# this works for the 100 but not for the 1000000. Can't tell if it works for any other number.

import time

def consecSum(n):
    primeList = [2, 3]
    prime = 5
    newSum = sum(primeList)
    maxSum = 5
    while newSum < n:
        isPrime = True
        for i in primeList:
            if prime % i == 0:
                isPrime = False
                break
        if isPrime == True:
            primeList.append(prime)
        else:
            prime += 2
            continue
        if sum(primeList) > n:
            break
        else:
            newSum = sum(primeList)
        sumIsPrime = True
        for j in primeList:
            if newSum % j == 0:
                sumIsPrime = False
                break
        if sumIsPrime == True:
            if newSum > maxSum:
                maxSum = newSum
        prime += 2    
    return maxSum
    
n = int(input("input number: "))
start = time.time()
x = consecSum(n)
print("the sum is %d" % (x), "\ntime est. %f ms" % ((time.time() - start) * 100))