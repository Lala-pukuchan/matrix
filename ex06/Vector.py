class Vector:
    def __init__(self, data):
        self.data = list(data)

    def __str__(self):
        return str(self.data)

    @staticmethod
    def cross_product(v1, v2):
        if len(v1.data) != 3 or len(v2.data) != 3:
            raise ValueError("Vectors must have 3 components.")
        a1, a2, a3 = v1.data
        b1, b2, b3 = v2.data
        return Vector([a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1])
