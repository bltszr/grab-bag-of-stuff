class listMatrix: # assuming the matrices are 1-indexed, might implement asserting later
    def __init__(self, matrixList):
        self.matrixList = matrixList
        # horizontal elements of the matrix
        self.Horizontal = matrixList
        # vertical elements of the matrix
        self.Vertical = [[i[j] for i in self.matrixList] for j in range(len(self.matrixList[0]))]
    # getters for each element specific on the list
    def getHor(self, index):
        return self.matrixList[index - 1]
    def getVer(self, index):
        return self.Vertical[index - 1]

def matrixGetter(x, y):
    matrix = []
    print("Input matrix: ")
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