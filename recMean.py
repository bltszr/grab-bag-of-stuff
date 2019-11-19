"""Find the mean of any list, nested or otherwise
without using any iterative loops, the built-in sum,
count, or numpy.
"""

def summation(alist) -> int:
    if type(alist) == int:
        return alist
    elif len(alist) == 0:
        return 0
    else:
        return summation(alist[0]) + summation(alist[1:])

def length(alist) -> int:
    if type(alist) == int:
        return 1
    elif len(alist) == 0:
        return 0
    else:
        return length(alist[0]) + length(alist[1:])

def mean(alist) -> int:
    return summation(alist) / length(alist)
    
def main():
    print("First testcase: [1 ,[2 ,3 ,[4]]] -->", mean([1 ,[2 ,3 ,[4]]]))
    print("Second testcase: ([[[1]] ,[[2] ,[3] ,[4]]] -->", mean([[[1]] ,[[2] ,[3] ,[4]]]))
    
main()