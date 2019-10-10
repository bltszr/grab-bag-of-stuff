import time
# find the length of a collatz sequence with a certain starting number
n = int(input("input number: "))
start = time.time()
def collatz(n):
    count = 0
    uN = n
    while uN > 1:
        if uN % 2 == 0:
            uN //= 2
        else:
            uN = (3 * uN) + 1
        count += 1
    return count

if n == 1000000:
    max = 152 # this is the length of 1000000
    maxNum = 1000000
else:
    max = 0
    maxNum = 0

i = 3
while  i < n - 1:
    if collatz(i) > max:
        max = collatz(i)
        maxNum = i
    i += 2

print("the number is %d" % (maxNum), "with a length of %d" %(max), "\ntime est. %f" % (time.time() - start))