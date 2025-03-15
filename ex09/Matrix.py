class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]

    def __str__(self):
        return "\n".join(str(row) for row in self.data)

    def transpose(self):
        return Matrix(
            [
                [self.data[j][i] for j in range(len(self.data))]
                for i in range(len(self.data[0]))
            ]
        )
