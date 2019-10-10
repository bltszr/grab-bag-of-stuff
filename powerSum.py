"""
find the sum of all the digits contained in the value of 2^n
project Euler no. 16: find the sum of all digits contained
in the value of 2^1000
"""
import time
n = int(input("provide the power with which 2 will be raised: "))
start = time.time()
x = 2 ** n
# print(x)
# print(list(str(x)))
# print(list((map(int, list(str(x))))))
print(sum(list((map(int, list(str(x)))))))
print("the time is: ", (start - time.time()))