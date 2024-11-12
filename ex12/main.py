import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_dir.Matrix import Matrix

# Test cases for matrix inverse
u = Matrix(
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ]
)
print(u.inverse().rows[0])
print(u.inverse().rows[1])
print(u.inverse().rows[2])
# Output:
# [1.0, 0.0, 0.0]
# [0.0, 1.0, 0.0]
# [0.0, 0.0, 1.0]

print("-----------------------")
u = Matrix(
    [
        [2.0, 0.0, 0.0],
        [0.0, 2.0, 0.0],
        [0.0, 0.0, 2.0],
    ]
)
print(u.inverse().rows[0])
print(u.inverse().rows[1])
print(u.inverse().rows[2])

# Output:
# [0.5, 0.0, 0.0]
# [0.0, 0.5, 0.0]
# [0.0, 0.0, 0.5]

print("-----------------------")
u = Matrix(
    [
        [8.0, 5.0, -2.0],
        [4.0, 7.0, 20.0],
        [7.0, 6.0, 1.0],
    ]
)
print(u.inverse().rows[0])
print(u.inverse().rows[1])
print(u.inverse().rows[2])
# Output:
# [0.649425287, 0.097701149, -0.655172414]
# [-0.781609195, -0.126436782, 0.965517241]
# [0.143678161, 0.074712644, -0.206896552]
