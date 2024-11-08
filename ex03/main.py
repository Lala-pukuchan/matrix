import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_dir.Vector import Vector

# Example usage
u = Vector([0.0, 0.0])
v = Vector([1.0, 1.0])
print(u.dot(v))  # Output: 0.0

u = Vector([1.0, 1.0])
v = Vector([1.0, 1.0])
print(u.dot(v))  # Output: 2.0

u = Vector([-1.0, 6.0])
v = Vector([3.0, 2.0])
print(u.dot(v))  # Output: 9.0
