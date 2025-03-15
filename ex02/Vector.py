class Vector:
    def __init__(self, data):
        self.data = list(data)

    def __str__(self):
        return str(self.data)

    @staticmethod
    def lerp(v1, v2, a):
        if isinstance(v1, (int, float)):
            return (1 - a) * v1 + a * v2
        elif isinstance(v1, Vector) and isinstance(v2, Vector):
            if len(v1.data) != len(v2.data):
                raise ValueError("Vectors must have the same length")
            return Vector(
                [(1 - a) * v1.data[i] + a * v2.data[i] for i in range(len(v1.data))]
            )
        else:
            raise ValueError("Invalid arguments")
