class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]

    def __str__(self):
        return "\n".join(str(row) for row in self.data)

    def trace(self):
        return sum(self.data[i][i] for i in range(len(self.data)))
