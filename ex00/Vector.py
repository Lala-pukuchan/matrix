class Vector:
    def __init__(self, data):
        self.data = list(data)

    def __str__(self):
        return str(self.data)

    def add(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("The vectors must have the same dimensions.")
        return [self.data[i] + other.data[i] for i in range(len(self.data))]

    def sub(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("The vectors must have the same dimensions.")
        return [self.data[i] - other.data[i] for i in range(len(self.data))]

    def scl(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("The scalar must be a number.")
        return [self.data[i] * scalar for i in range(len(self.data))]
