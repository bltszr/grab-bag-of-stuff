def primGen(n):
    prim = True
    for i in range(2, n):
        if n % i == 0:
            prim = False
            break
    return prim
    
def primOdd(n): # for odd numbers only
    prim = True
    for i in range(3, n, 2):
        if n % i == 0:
            prim = False
            break
    return prim
    
# print(prim(600851475143))