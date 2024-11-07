class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def add(self, m):
        if len(self.rows) != len(m.rows) or len(self.rows[0]) != len(m.rows[0]):
            raise ValueError("Matrices must be the same size for addition.")
        self.rows = [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.rows, m.rows)]

    def sub(self, m):
        if len(self.rows) != len(m.rows) or len(self.rows[0]) != len(m.rows[0]):
            raise ValueError("Matrices must be the same size for subtraction.")
        self.rows = [[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(self.rows, m.rows)]

    def scl(self, scalar):
        self.rows = [[scalar * a for a in row] for row in self.rows]

    def __str__(self):
        return '\n'.join(str(row) for row in self.rows)

