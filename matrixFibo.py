class ListMatrix: # assuming the matrices are 1-indexed, might implement asserting later
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list
        # horizontal elements of the matrix
        self.horizontal = matrix_list
        # vertical elements of the matrix
        self.vertical = [[i[j] for i in self.matrix_list] for j in range(len(self.matrix_list[0]))]
    # getters for each element specific on the list
    def get_hor(self, index):
        return self.matrix_list[index - 1]
    def get_ver(self, index):
        return self.vertical[index - 1]
    def multiply(self, othermatrix):
        