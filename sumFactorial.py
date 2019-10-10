import time
# project Euler number 20: sum the digits of a factorial (e.g. 100!)
n = int(input("input the factorial to be summed: "))
# iterative method
start1 = time.time()
fact1 = 1
for i in range(1, n + 1):
    fact1 *= i

sum1 = (sum(list((map(int, list(str(fact1)))))))
print("The value of the sum is %d with the time of %d" % (sum1, (time.time()-start1)))

# recursive method
# this actually hits the recursive depth limit lmfao
start2 = time.time()
def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return (fact(n) * fact(n-1))
        
sum2 = (sum(list((map(int, list(str(fact(n))))))))
print("The value of sum is %d with the time of %f" % (sum2, (time.time()-start2)))