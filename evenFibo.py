def Fib(m):
    if m == 0:
        return 1
    elif m == 1:
        return 1
    else:
        return Fib(m-1) + Fib(m-2)

i = 2
sum = 0
while Fib(i) < 4000000:
    sum +=  Fib(i)
    i += 3
    
print(sum)