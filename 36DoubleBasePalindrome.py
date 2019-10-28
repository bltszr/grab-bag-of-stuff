"""
Find the sum of the numbers smaller than one million which are palindromic
both in base 10 and base 2. e.g. "585" is palindromic in base 10, and in
base 2 it is "1001001001", which is also palindromic.
"""
from time import time
sum = 0
limit = int(input("Please input a number limit: "))
start = time()
for i in range(limit):
    if str(i) == str(i)[::-1]:
        if str(bin(i)[2:]) == str(bin(i)[:1:-1]):
            sum += i
            print(i)
end = time()
print("\nThe sum %d found in %d miliseconds" % (sum, end-start))