# finds the nth prime (e.g. the 1st prime is 2, 2nd prime is 3, 6th prime is 13)

def prim(n): #we should probably just import this as a module
    prim = True
    for i in range(2, n):
        if n % i == 0:
            prim = False
            break
    return prim

def nthPrime(n):
    prime = 3
    i = prime
    for j in range(2, n+1):
        while not prim(i):
            i += 2
        else:
            prime = i
            i += 2
    return prime

n = int(input("input num: "))
print(nthPrime(n))