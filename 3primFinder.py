def primGen(n): # general function
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
    
if __name__ == "__main__":
    print(prim(600851475143)) # project Euler number 3