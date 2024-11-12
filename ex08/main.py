import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_dir.Matrix import Matrix

# Test cases for matrix trace
u = Matrix(
    [
        [1.0, 0.0],
        [0.0, 1.0],
    ]
)
print(u.trace())  # Output: 2.0

print("-----------------------")
u = Matrix(
    [
        [2.0, -5.0, 0.0],
        [4.0, 3.0, 7.0],
        [-2.0, 3.0, 4.0],
    ]
)
print(u.trace())  # Output: 9.0

print("-----------------------")
u = Matrix(
    [
        [-2.0, -8.0, 4.0],
        [1.0, -23.0, 4.0],
        [0.0, 6.0, 4.0],
    ]
)
print(u.trace())  # Output: -21.0
