import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_dir.Vector import Vector

# Test cases
u = Vector([0.0, 0.0, 1.0])
v = Vector([1.0, 0.0, 0.0])
print(u.cross_product(v))  # Output: [0. 1. 0.]

u = Vector([1.0, 2.0, 3.0])
v = Vector([4.0, 5.0, 6.0])
print(u.cross_product(v))  # Output: [-3.  6. -3.]

u = Vector([4.0, 2.0, -3.0])
v = Vector([-2.0, -5.0, 16.0])
print(u.cross_product(v))  # Output: [ 17. -58. -16.]
