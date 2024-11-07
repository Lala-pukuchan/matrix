import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from class_dir.Vector import Vector
from class_dir.Matrix import Matrix

# Vector operations
u = Vector([2.0, 3.0])
v = Vector([5.0, 7.0])
u.add(v)
print(u)  # Output: [7.0, 10.0]

u = Vector([2.0, 3.0])
v = Vector([5.0, 7.0])
u.sub(v)
print(u)  # Output: [-3.0, -4.0]

u = Vector([2.0, 3.0])
u.scl(2.0)
print(u)  # Output: [4.0, 6.0]

# Matrix operations
u = Matrix([[1.0, 2.0], [3.0, 4.0]])
v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
u.add(v)
print(u)  # Output: [[8.0, 6.0], [1.0, 6.0]]

u = Matrix([[1.0, 2.0], [3.0, 4.0]])
v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
u.sub(v)
print(u)  # Output: [[-6.0, -2.0], [5.0, 2.0]]

u = Matrix([[1.0, 2.0], [3.0, 4.0]])
u.scl(2.0)
print(u)  # Output: [[2.0, 4.0], [6.0, 8.0]]
