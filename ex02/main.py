import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_dir.Vector import Vector
from class_dir.Matrix import Matrix

# Scalar examples
print(Vector.lerp(0.0, 1.0, 0.0))  # Output: 0.0
print(Vector.lerp(0.0, 1.0, 1.0))  # Output: 1.0
print(Vector.lerp(0.0, 1.0, 0.5))  # Output: 0.5
print(Vector.lerp(21.0, 42.0, 0.3))  # Output: 27.3

# Vector example
vector_start = Vector([2.0, 1.0])
vector_end = Vector([4.0, 2.0])
print(Vector.lerp(vector_start, vector_end, 0.3))  # Output: [2.6, 1.3]

# Matrix example
matrix_start = Matrix([[2.0, 1.0], [3.0, 4.0]])
matrix_end = Matrix([[20.0, 10.0], [30.0, 40.0]])
print(Matrix.lerp(matrix_start, matrix_end, 0.5))  # Output: [[11., 5.5], [16.5, 22.]]
