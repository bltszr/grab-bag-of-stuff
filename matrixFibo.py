# Still does not work, I might be dumb

class ListMatrix: # assuming the matrices are 0-indexed, might implement asserting later
    def __init__(self, matrix_list = []):
        # horizontal elements of the matrix
        self.horizontal = matrix_list
        # vertical elements of the matrix
        self.vertical = [[i[j] for i in matrix_list] for j in range(len(matrix_list[0]))]
    # getters for each element specific on the list
    def get_hor(self, index=0):
        return self.horizontal[index]
    def get_ver(self, index=0):
        return self.vertical[index]
    def multiply(self, other): # assuming the matrices don't violate any conventions
        res_matrix = [[0] * len(self.horizontal) for _ in len(other.vertical)]
        for row in range(len(res_matrix)):
            for cell in range(row):
                res_matrix[cell] += sum(self_ele * other_ele for self_ele, other_ele in zip(self.get_ver[row], other.get_hor[cell]))
    def power(self, exponent = 1):
        if exponent == 1:
            return self.horizontal
        else:
            return self.multiply(self.power(exponent - 1))

if __name__ == "__main__":
    fibo = ListMatrix([[1, 1], [1, 0]])
    print(fibo.power(2))