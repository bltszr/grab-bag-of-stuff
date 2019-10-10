# code sums all multiples of three and five below a given integer
# project Euler no. 1
import sys

sum = 0
for i in range(1000):
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i

sys.stdout.write(str(sum))