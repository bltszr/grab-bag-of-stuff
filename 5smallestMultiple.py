"""
project Euler number 5
"""

def smallestMultiple(n):
    numList = [1]
    for i in range(2, n+1):
        for j in numList[1:]:
            if i % j == 0:
                numList.remove(j)
        numList.append(i)
    
    count = max(numList)
    constCount = count
    isDivisible = False
    while isDivisible == False:
        for k in numList:
            isDivisible = True
            if count % k != 0:
                isDivisible = False
                break
        if isDivisible == True:
            break
        else:
            count += constCount
    
    return count
        

n = int(input("input num: "))
print(smallestMultiple(n))