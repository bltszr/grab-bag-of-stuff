"""
This is an algorithm to find all primitive pythagorean
triples for a certain limit such that its biggest number
is smaller than said limit.
"""
from time import time
def Euclid(limit):
    hash = {0: [3, 4, 5]}
    
def pythGen(limit):
    iterator = 1
    hash = {0: [3, 4, 5]}
    c = 5
    while c < limit:
        b = 0
        while b < c:
            a = 0
            while a < b:
                if (((a ** 2) + (b ** 2)) == (c ** 2)):
                    isFound = True
                    for triangle in hash.values():
                        if (a + b + c) % sum(triangle) != 0:
                            continue
                        else:
                            isFound = False
                            break
                    if isFound:
                        hash[iterator] = [a, b, c]
                        iterator += 1
                    a += 1
                a += 1
            b += 1
        c += 1
    return(list(hash.values()))

if __name__ == "__main__":
    start = time()
    limit = int(input("Please provide the limiting number: "))
    pythList = pythGen(limit)
    end = time()
    print(pythList)
    print("Done in %f seconds." % (end-start))