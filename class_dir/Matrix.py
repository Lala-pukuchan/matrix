from .Vector import Vector
import numpy as np


class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def add(self, m):
        if len(self.rows) != len(m.rows) or len(self.rows[0]) != len(m.rows[0]):
            raise ValueError("Matrices must be the same size for addition.")
        self.rows = [
            [a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.rows, m.rows)
        ]

    def sub(self, m):
        if len(self.rows) != len(m.rows) or len(self.rows[0]) != len(m.rows[0]):
            raise ValueError("Matrices must be the same size for subtraction.")
        self.rows = [
            [a - b for a, b in zip(row1, row2)] for row1, row2 in zip(self.rows, m.rows)
        ]

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
        result_rows = [
            [0] * len(matrices[0].rows[0]) for _ in range(len(matrices[0].rows))
        ]

        # Perform scaling and summing
        for matrix, scalar in zip(matrices, scalars):
            scaled_matrix = Matrix([[scalar * a for a in row] for row in matrix.rows])
            result_rows = [
                [sum(x) for x in zip(*rows)]
                for rows in zip(result_rows, scaled_matrix.rows)
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
            if len(start.rows) != len(end.rows) or len(start.rows[0]) != len(
                end.rows[0]
            ):
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
        return "\n".join(str(row) for row in self.rows)

    def mul_vec(self, vector):
        """
        Multiply the matrix by a vector.
        """
        if len(self.rows[0]) != len(vector.elements):
            raise ValueError("Matrix column count must match vector size.")

        # Multiply each row by the vector
        result_elements = [
            sum(a * b for a, b in zip(row, vector.elements)) for row in self.rows
        ]
        return Vector(result_elements)

    def mul_mat(self, other):
        """
        Multiply the matrix by another matrix.
        """
        if len(self.rows[0]) != len(other.rows):
            raise ValueError("Matrix A's column count must match Matrix B's row count.")

        # Transpose the second matrix to simplify dot products
        other_t = list(zip(*other.rows))

        # Compute matrix multiplication
        result_rows = [
            [sum(a * b for a, b in zip(row, col)) for col in other_t]
            for row in self.rows
        ]
        return Matrix(result_rows)

    def trace(self):
        """
        Calculate the trace of the matrix.
        Only defined for square matrices.
        """
        # Ensure the matrix is square
        if len(self.rows) != len(self.rows[0]):
            raise ValueError("Trace is only defined for square matrices.")

        # Sum the diagonal elements
        return sum(self.rows[i][i] for i in range(len(self.rows)))

    def transpose(self):
        """
        Transpose the matrix.
        converts rows to columns and columns to rows.
        map function is for-loop equivalent and converts tuple to list.
        [[1, 2, 3],
        [4, 5, 6]]
        to
        [[1, 4],
        [2, 5],
        [3, 6]]
        """
        self.rows = list(map(list, zip(*self.rows)))
        return self

    def row_echelon(self):
        """
        Convert the matrix to row-echelon form.
        time complexity: O(n^3) 3 nested loops
        space complexity: O(n^2) create new matrix n rows and n columns
        """
        # Copy the matrix to avoid modifying the original
        matrix = [row[:] for row in self.rows]

        # Initialize pivot position
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        pivot_row = 0

        for pivot_col in range(num_cols):
            # Find a non-zero pivot and swap rows if needed
            if matrix[pivot_row][pivot_col] == 0:
                for j in range(pivot_row + 1, num_rows):
                    if matrix[j][pivot_col] != 0:
                        matrix[pivot_row], matrix[j] = matrix[j], matrix[pivot_row]
                        break
                else:
                    continue  # Skip to the next column if no non-zero pivot is found

            # Normalize the pivot row
            pivot = matrix[pivot_row][pivot_col]
            matrix[pivot_row] = [x / pivot for x in matrix[pivot_row]]

            # Eliminate entries below the pivot
            for j in range(pivot_row + 1, num_rows):
                if matrix[j][pivot_col] != 0:
                    factor = matrix[j][pivot_col]
                    matrix[j] = [
                        a - factor * b for a, b in zip(matrix[j], matrix[pivot_row])
                    ]

            # Eliminate entries above the pivot (Gauss-Jordan elimination step)
            for j in range(pivot_row - 1, -1, -1):
                if matrix[j][pivot_col] != 0:
                    factor = matrix[j][pivot_col]
                    matrix[j] = [
                        a - factor * b for a, b in zip(matrix[j], matrix[pivot_row])
                    ]

            # Move to the next pivot row
            pivot_row += 1
            if pivot_row >= num_rows:
                break

        # Replace small values with 0.0 to avoid -0.0
        threshold = 1e-10
        for i in range(num_rows):
            matrix[i] = [0.0 if abs(x) < threshold else x for x in matrix[i]]

        return Matrix(matrix)
