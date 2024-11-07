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
        """
        Scale each element in the matrix by a scalar.
        """
        self.rows = [[scalar * a for a in row] for row in self.rows]
        return self  # Return self to allow chaining

    @classmethod
    def linear_combination(cls, matrices, scalars):
        """
        Compute the linear combination of matrices with given scalars.
        """
        if len(matrices) != len(scalars):
            raise ValueError("Matrices and scalars must have the same length")

        # Initialize result matrix with zero values
        result_rows = [[0] * len(matrices[0].rows[0]) for _ in range(len(matrices[0].rows))]

        # Perform scaling and summing
        for matrix, scalar in zip(matrices, scalars):
            scaled_matrix = Matrix([[scalar * a for a in row] for row in matrix.rows])
            result_rows = [
                [sum(x) for x in zip(*rows)] for rows in zip(result_rows, scaled_matrix.rows)
            ]

        return cls(result_rows)

    @staticmethod
    def lerp(start, end, t):
        """
        Linearly interpolate between two matrices or two scalars.
        """
        if isinstance(start, (int, float)) and isinstance(end, (int, float)):
            # Scalar case
            return start + t * (end - start)
        elif isinstance(start, Matrix) and isinstance(end, Matrix):
            # Matrix case
            if len(start.rows) != len(end.rows) or len(start.rows[0]) != len(end.rows[0]):
                raise ValueError("Matrices must be the same size for interpolation.")
            result_matrix = Matrix.linear_combination([start, end], [1 - t, t])
            # Round each element to 1 decimal place
            result_matrix.rows = [
                [round(x, 1) for x in row] for row in result_matrix.rows
            ]
            return result_matrix
        else:
            raise ValueError("Start and end must be both scalars or matrices")

    def __str__(self):
        return '\n'.join(str(row) for row in self.rows)
