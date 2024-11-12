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

    def determinant(self):
        """
        Calculate the determinant of the matrix.
        Only defined for square matrices.
        Time Complexity: O(n!)
        - The function uses cofactor expansion to compute the determinant, which has a factorial time complexity.
        - For each element in the first row, it recursively calculates the determinant of an (n-1) x (n-1) submatrix.
        - For an n x n matrix, this results in O(n!) complexity because each recursive call spawns further recursive calls for smaller submatrices.

        Space Complexity: O(n^2)
        - Each recursive call creates a submatrix by removing one row and one column, storing these in memory.
        - For an n x n matrix, the space required to store these submatrices across all recursive calls is O(n^2).
        - Additionally, the recursion depth can reach up to n, so the maximum space complexity is bounded by O(n^2) for an n x n matrix.
        """
        # Ensure the matrix is square
        if len(self.rows) != len(self.rows[0]):
            raise ValueError("Determinant is only defined for square matrices.")

        # Base case for 2x2 matrix
        if len(self.rows) == 2:
            return self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1][0]

        # Recursive case for larger matrices
        det = 0
        for i in range(len(self.rows)):
            m = self.rows[0][i] * ((-1) ** i)
            sub_matrix = [row[:i] + row[i + 1 :] for row in self.rows[1:]]
            det += m * Matrix(sub_matrix).determinant()

        return det

    def adjugate(self):
        """
        Calculate the adjugate of the matrix.
        Only defined for square matrices.
        [[3, 5],
        [-7, 2]]
        to
        [[2, -5],
        [7, 3]]
        convert 3 to 2
        and negative -7 to 7, 5 to -5
        """
        if not self.is_square():
            raise ValueError("Adjugate is only defined for square matrices.")
        # Calculate the matrix of minors
        minors = [
            [
                ((-1) ** (i + j))
                * Matrix(
                    [
                        row[:j] + row[j + 1 :]
                        for row in self.rows[:i] + self.rows[i + 1 :]
                    ]
                ).determinant()
                for j in range(len(self.rows))
            ]
            for i in range(len(self.rows))
        ]

        # Transpose the matrix of minors to get the cofactor matrix (the adjugate)
        cofactors = list(map(list, zip(*minors)))
        return Matrix(cofactors)

    def is_square(self):
        """
        Check if the matrix is square.
        """
        return len(self.rows) == len(self.rows[0])

    def inverse(self):
        """
        Calculate the inverse of the matrix.
        """
        if not self.is_square():
            raise ValueError("Inverse is only defined for square matrices.")

        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is not invertible.")

        # Calculate adjugate and scale by 1/det
        adjugate = self.adjugate()
        inverse_matrix = adjugate.scl(1 / det)

        # Clean up small negative zeros
        inverse_matrix.rows = [
            [0.0 if abs(x) < 1e-10 else x for x in row] for row in inverse_matrix.rows
        ]
        return inverse_matrix
