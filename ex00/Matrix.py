class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]

    def __str__(self):
        return "\n".join(str(row) for row in self.data)

    def add(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("The matrices must have the same dimensions.")
        return [
            [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ]

    def sub(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("The matrices must have the same dimensions.")
        return [
            [self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ]

    def scl(self, scl):
        if not isinstance(scl, (int, float)):
            raise ValueError("The scalar must be a number.")
        return [
            [self.data[i][j] * scl for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ]
