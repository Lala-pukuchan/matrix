class Vector:
    def __init__(self, elements):
        self.elements = elements

    def add(self, v):
        """
        o(n) space complexity:  zip ([1, 2, 3], [a, b, c]) -> [1, a], [2, b], [3, c]
        o(n) time complexity: 1+a, 2+b, 3+c
        """
        if len(self.elements) != len(v.elements):
            raise ValueError("Vectors must be the same size for addition.")
        self.elements = [a + b for a, b in zip(self.elements, v.elements)]

    def sub(self, v):
        if len(self.elements) != len(v.elements):
            raise ValueError("Vectors must be the same size for subtraction.")
        self.elements = [a - b for a, b in zip(self.elements, v.elements)]

    def scl(self, scalar):
        self.elements = [scalar * a for a in self.elements]

    def __str__(self):
        return str(self.elements)
