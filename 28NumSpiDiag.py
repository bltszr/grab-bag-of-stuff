"""
Project Euler number 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

from time import time

# EXPLANATION
# the spiral size grows by two and in each circle the distance between two corner numbers grows by 2 as well.
# the jump from the first circle to the next circle is going to be the distance of the corner numbers of the
# outer ring. the number of circles (excluding one) is going to be (circle length - 1) // 2

sideLen = int(input("input the spiral size: "))
start = time()
circleNum = (sideLen - 1) // 2
sum = 1
diff = 2
num = sum
for ring in range(circleNum):
    for cornerNum in range(4):
        num += diff
        sum += num
    diff += 2
print(sum)
print("done in %d seconds" % (time() - start))