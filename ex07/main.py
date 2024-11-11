import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_dir.Vector import Vector
from class_dir.Matrix import Matrix

# Test cases for matrix-vector multiplication
u = Matrix([[1.0, 0.0], [0.0, 1.0]])
v = Vector([4.0, 2.0])
print(u.mul_vec(v))  # Output: [4. 2.]

print("-----------------------")
u = Matrix([[2.0, 0.0], [0.0, 2.0]])
v = Vector([4.0, 2.0])
print(u.mul_vec(v))  # Output: [8. 4.]

print("-----------------------")
u = Matrix([[2.0, -2.0], [-2.0, 2.0]])
v = Vector([4.0, 2.0])
print(u.mul_vec(v))  # Output: [ 4. -4.]

print("-----------------------")
# Test cases for matrix-matrix multiplication
u = Matrix([[1.0, 0.0], [0.0, 1.0]])
v = Matrix([[1.0, 0.0], [0.0, 1.0]])
print(u.mul_mat(v))  # Output: [[1. 0.] [0. 1.]]

print("-----------------------")
u = Matrix([[1.0, 0.0], [0.0, 1.0]])
v = Matrix([[2.0, 1.0], [4.0, 2.0]])
print(u.mul_mat(v))  # Output: [[2. 1.] [4. 2.]]

print("-----------------------")
u = Matrix([[3.0, -5.0], [6.0, 8.0]])
v = Matrix([[2.0, 1.0], [4.0, 2.0]])
print(u.mul_mat(v))  # Output: [[-14.  -7.] [ 44.  22.]]
