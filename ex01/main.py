import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from class_dir.Vector import Vector


# Create vectors
e1 = Vector([1.0, 0.0, 0.0])
e2 = Vector([0.0, 1.0, 0.0])
e3 = Vector([0.0, 0.0, 1.0])
v1 = Vector([1.0, 2.0, 3.0])
v2 = Vector([0.0, 10.0, -100.0])

# Perform linear combinations
result1 = Vector.linear_combination([e1, e2, e3], [10.0, -2.0, 0.5])
## 10.0 * e1 + (-2.0) * e2 + 0.5 * e3 = [10.0, -2.0, 0.5]
print(result1)  # Output: [10.0, -2.0, 0.5]

result2 = Vector.linear_combination([v1, v2], [10.0, -2.0])
print(result2)  # Output: [10.0, 0.0, 230.0]
