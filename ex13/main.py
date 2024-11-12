import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_dir.Matrix import Matrix

u = Matrix(
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ]
)
print(u.rank())
# 3

u = Matrix(
    [
        [1.0, 2.0, 0.0, 0.0],
        [2.0, 4.0, 0.0, 0.0],
        [-1.0, 2.0, 1.0, 1.0],
    ]
)
print(u.rank())
# 2

u = Matrix(
    [
        [8.0, 5.0, -2.0],
        [4.0, 7.0, 20.0],
        [7.0, 6.0, 1.0],
        [21.0, 18.0, 7.0],
    ]
)
print(u.rank())
# 3
