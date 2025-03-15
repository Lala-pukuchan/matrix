from Vector import Vector


class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]

    def __str__(self):
        return "\n".join(str(row) for row in self.data)

    def mul_vec(self, vec):
        if len(vec.data) != len(self.data[0]):
            raise ValueError("Invalid dimensions")
        result = []
        for row in self.data:
            result.append(Vector.dot(Vector(row), vec))
        return Vector(result)

    def mul_mat(self, mat):
        if len(self.data[0]) != len(mat.data):
            raise ValueError("Invalid dimensions")
        m = len(self.data)
        n = len(self.data[0])
        p = len(mat.data[0])
        result = []
        for i in range(m):
            row_result = []
            for j in range(p):
                col_j = [mat.data[k][j] for k in range(n)]
                row_result.append(Vector.dot(Vector(self.data[i]), Vector(col_j)))
            result.append(row_result)
        return Matrix(result)
