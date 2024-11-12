import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_dir.Matrix import Matrix

# Test cases for matrix transpose
u = Matrix([[1, 2, 3], [4, 5, 6]])
print(u.transpose())  # Output: [[1, 4], [2, 5], [3, 6]]

print("-----------------------")
u = Matrix([[1, 2], [3, 4], [5, 6]])
print(u.transpose())  # Output: [[1, 3, 5], [2, 4, 6]]

print("-----------------------")
u = Matrix([[1]])
print(u.transpose())  # Output: [[1]]

print("-----------------------")
u = Matrix([[1, 2, 3]])
print(u.transpose())  # Output: [[1], [2], [3]]

print("-----------------------")
u = Matrix([[1], [2], [3]])
print(u.transpose())  # Output: [[1, 2, 3]]
