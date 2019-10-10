def SumquareDiff(n):
    sumCount = 0
    squareCount = 0
    for i in range(n+1):
        sumCount += i
        squareCount += (i ** 2)
    sumCount *= sumCount
    return sumCount - squareCount

n = int(input("input num: "))
print(SumquareDiff(n))