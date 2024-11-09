import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_dir.Vector import Vector

u = Vector([1.0, 0.0])
v = Vector([1.0, 0.0])
print(u.angle_cos(v))  # Output: 1.0

u = Vector([1.0, 0.0])
v = Vector([0.0, 1.0])
print(u.angle_cos(v))  # Output: 0.0

u = Vector([-1.0, 1.0])
v = Vector([1.0, -1.0])
print(u.angle_cos(v))  # Output: -1.0

u = Vector([2.0, 1.0])
v = Vector([4.0, 2.0])
print(u.angle_cos(v))  # Output: 1.0

u = Vector([1.0, 2.0, 3.0])
v = Vector([4.0, 5.0, 6.0])
print(u.angle_cos(v))  # Output: 0.974631846
