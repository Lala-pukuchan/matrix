import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_dir.Matrix import Matrix

# Test cases
u = Matrix([
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
])
print(u.row_echelon())
# Output: [[1. 0. 0.]
#          [0. 1. 0.]
#          [0. 0. 1.]]
print("-----------------------")

u = Matrix([
    [1.0, 2.0],
    [3.0, 4.0],
])
print(u.row_echelon())
# Output: [[1. 0.]
#          [0. 1.]]
print("-----------------------")

u = Matrix([
    [1.0, 2.0],
    [2.0, 4.0],
])
print(u.row_echelon())
# Output: [[1. 2.]
#          [0. 0.]]
print("-----------------------")

u = Matrix([
    [8.0, 5.0, -2.0, 4.0, 28.0],
    [4.0, 2.5, 20.0, 4.0, -4.0],
    [8.0, 5.0, 1.0, 4.0, 17.0],
])
print(u.row_echelon())
# Output: [[ 1.          0.625       0.          0.        -12.16666667]
#          [ 0.          0.          1.          0.         -3.66666667]
#          [ 0.          0.          0.          1.         29.5       ]]