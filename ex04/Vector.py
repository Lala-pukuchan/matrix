class Vector:
    def __init__(self, data):
        self.data = list(data)

    def __str__(self):
        return str(self.data)

    def abs(self, x):
        return x if x > 0 else -x

    def norm_1(self):
        return sum(abs(x) for x in self.data)

    def norm(self):
        return sum(x**2 for x in self.data) ** 0.5

    def norm_inf(self):
        return max(abs(x) for x in self.data)
