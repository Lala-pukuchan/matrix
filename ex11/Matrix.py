class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]

    def __str__(self):
        return "\n".join(str(row) for row in self.data)

    def abs(self, x):
        return x if x > 0 else -x

    def determinant(self):
        det_sign = 1
        det_product = 1

        A = [row[:] for row in self.data]
        num_rows = len(A)
        num_cols = len(A[0])

        pivot_row = 0

        for pivot_col in range(num_cols):
            pivot_found = False
            pivot_row_index = None
            for row in range(pivot_row, num_rows):
                if abs(A[row][pivot_col]) > 1e-6:
                    pivot_row_index = row
                    pivot_found = True
                    break
            if not pivot_found:
                return 0.0

            if pivot_row_index != pivot_row:
                A[pivot_row], A[pivot_row_index] = A[pivot_row_index], A[pivot_row]
                det_sign *= -1

            pivot_value = A[pivot_row][pivot_col]
            det_product *= pivot_value
            A[pivot_row] = [x / pivot_value for x in A[pivot_row]]

            for r in range(num_rows):
                if r != pivot_row:
                    factor = A[r][pivot_col]
                    A[r] = [A[r][c] - factor * A[pivot_row][c] for c in range(num_cols)]

            pivot_row += 1
            if pivot_row == num_rows:
                break

        threshold = 1e-10
        for i in range(num_rows):
            A[i] = [0.0 if abs(x) < threshold else x for x in A[i]]

        return det_sign * det_product
