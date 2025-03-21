class Vector:
    def __init__(self, data):
        self.data = list(data)

    def __str__(self):
        return str(self.data)

    @staticmethod
    def dot(v1, v2):
        if isinstance(v1, Vector) and isinstance(v2, Vector):
            if len(v1.data) != len(v2.data):
                raise ValueError("Vectors must have the same length")
            return sum(v1.data[i] * v2.data[i] for i in range(len(v1.data)))
        else:
            raise ValueError("Invalid arguments")

    def norm(self):
        return sum(x**2 for x in self.data) ** 0.5

    def angle_cos(v1, v2):
        if isinstance(v1, Vector) and isinstance(v2, Vector):
            if len(v1.data) != len(v2.data):
                raise ValueError("Vectors must have the same length")
            return Vector.dot(v1, v2) / (v1.norm() * v2.norm())
        else:
            raise ValueError("Invalid arguments")
