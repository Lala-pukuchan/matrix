import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_dir.Vector import Vector

u = Vector([0.0, 0.0, 0.0])
print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")  # Output: 0.0, 0.0, 0.0

# Create a vector with elements 1, 2, 3
u = Vector([1.0, 2.0, 3.0])
print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")  # Output: 6.0, 3.74165738, 3.0

# Create a vector with elements -1, -2
u = Vector([-1.0, -2.0])
print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")  # Output: 3.0, 2.236067977, 2.0
