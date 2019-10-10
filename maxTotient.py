"""
Euler's totient or the phi(n) is used to determine the number of
numbers which are RELATIVELY prime--or CO-PRIME--to n. This means
the numbers which share no common factors with n except 1, which are
smaller than n itself. For example, the relative primes of 9 is 1, 2, 4, 
5, 7, and 8. This means that phi(9) = 6.

Now find the value of n smaller than a certain number for which
n / phi(n) is maximum.

Project Euler no. 69: find the value of n smaller than 1000000 such that
n / phi(n) is maximum.
"""

limit = int(input("please provide the limiting number: "))
n = 2
maxVal = 1
maxPhi = 2
while n < limit:
    coprime = [1]
    num = 1
    while num > n:
        for i in coprime:
            if i == 1:
                continue
            else:
                if num % i == 0:
                
??????????????????????