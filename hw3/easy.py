import numpy as np


class IncorrectMatrixSizeException(Exception):

    def __init__(self, left_n, left_m, right_n, right_m):
        self.left_n = left_n
        self.left_m = left_m
        self.right_n = right_n
        self.right_m = right_m


class MyMatrix:

    def __init__(self, matrix):
        self.value = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])

    def __add__(self, other):
        try:
            if self.n != other.n or self.m != other.m:
                raise IncorrectMatrixSizeException(self.n, self.m, other.n, other.m)
            result = [[0 for _ in range(self.n)] for _ in range(self.m)]
            for i in range(self.n):
                for j in range(self.m):
                    result[i][j] = self.value[i][j] + other.value[i][j]
            return MyMatrix(result)
        except IncorrectMatrixSizeException as e:
            print("Incorrect matrices sizes\n")
            return None

    def __mul__(self, other):
        try:
            if self.m != other.n:
                raise IncorrectMatrixSizeException(self.n, self.m, other.n, other.m)
            result = [[0 for _ in range(self.n)] for _ in range(other.m)]
            for i in range(self.n):
                for j in range(other.m):
                    for k in range(self.m):
                        result[i][j] += self.value[i][k] * other.value[k][j]
            return MyMatrix(result)
        except IncorrectMatrixSizeException as e:
            print("Incorrect matrices sizes\n")
            return None

    def __matmul__(self, other):
        try:
            if self.n != other.n or self.m != other.m:
                raise IncorrectMatrixSizeException(self.n, self.m, other.n, other.m)
            result = [[0 for _ in range(self.n)] for _ in range(self.m)]
            for i in range(self.n):
                for j in range(self.m):
                    result[i][j] = self.value[i][j] * other.value[i][j]
            return MyMatrix(result)
        except IncorrectMatrixSizeException as e:
            print("Incorrect matrices sizes\n")
            return None

    def __str__(self):
        s = str()
        for row in self.value:
            s += str(row) + '\n'
        return s


np.random.seed(0)
a = MyMatrix(np.random.randint(0, 10, (10, 10)))
b = MyMatrix(np.random.randint(0, 10, (10, 10)))

with open("./artifacts/easy/matrix+.txt", 'w') as f:
    f.write((a + b).__str__())

with open("./artifacts/easy/matrix1.txt", 'w') as f:
    f.write((a * b).__str__())

with open("./artifacts/easy/matrix@.txt", 'w') as f:
    f.write((a @ b).__str__())
