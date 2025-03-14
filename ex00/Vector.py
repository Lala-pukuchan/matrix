class Vector:
    def __init__(self, data):
        self.data = list(data)

    def __str__(self):
        return str(self.data)

    def add(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("The matrices must have the same dimensions.")
        return [self[i] + other[i] for i in range(len(self))]
