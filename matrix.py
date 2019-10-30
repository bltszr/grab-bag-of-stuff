class listMatrix:
    def __init__(self, List):
        self.List = List
    def getHor(self, index):
        return self.List[index - 1]
    def getVer(self, index): # assuming the matrices are 1-indexed
        return [i[index - 1] for i in self.List]

def matrixGetter(x, y):
    matrix = []
    print("Input matrix: ", flush=True)
    for i in range(y):
        n = input()
        lst = [int(x) for x in n.split()]
        matrix.append(lst)
    return matrix

if __name__ == "__main__":
    num = input("Provide the list dimensions in 'x y': ")
    x, y = list(map(int, num.split()))[0], list(map(int, num.split()))[1]
    matrix = matrixGetter(x, y)
    matrix = listMatrix(matrix)
    print()
    print(*(matrix.getHor(1)))
    print(*(matrix.getVer(1)))