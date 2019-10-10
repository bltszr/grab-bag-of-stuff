def prim(n):
    prim = True
    for i in range(2, n):
        if n % i == 0:
            prim = False
            break
    return prim

# for odd numbers only
def largestPrim(n):
    largestPrime = -1
    TrueN = n
    i = 3 # change this to two if the number is even
    while i < TrueN:
        if n % i == 0:
            if prim(i) == True:
                largestPrime = i
                n = n // i
        else:
            i += 2
    return largestPrime
    
print(largestPrim(408464633))