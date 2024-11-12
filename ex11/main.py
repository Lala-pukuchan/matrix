import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_dir.Matrix import Matrix


# • What happens when det(A) = 0
#   area of the parallelogram is 0, the vectors are linearly dependent
# • What the determinant represents geometrically in the vector space after using the matrix for a linear transformation.
#   The determinant represents the scaling factor of the linear transformation described by the matrix
# Test cases for matrix determinant
u = Matrix(
    [
        [1.0, -1.0],
        [-1.0, 1.0],
    ]
)
print(u.determinant())  # Output: 0.0

print("-----------------------")
u = Matrix(
    [
        [2.0, 0.0, 0.0],
        [0.0, 2.0, 0.0],
        [0.0, 0.0, 2.0],
    ]
)
print(u.determinant())  # Output: 8.0

print("-----------------------")
u = Matrix(
    [
        [8.0, 5.0, -2.0],
        [4.0, 7.0, 20.0],
        [7.0, 6.0, 1.0],
    ]
)
print(u.determinant())  # Output: -174.0

print("-----------------------")
u = Matrix(
    [
        [8.0, 5.0, -2.0, 4.0],
        [4.0, 2.5, 20.0, 4.0],
        [8.0, 5.0, 1.0, 4.0],
        [28.0, -4.0, 17.0, 1.0],
    ]
)
print(u.determinant())  # Output: 1032.0
