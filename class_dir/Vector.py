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
        # Return a new Vector with scaled elements
        return Vector([scalar * a for a in self.elements])

    def __str__(self):
        return str(self.elements)

    @classmethod
    def linear_combination(cls, vectors, scalars):
        """
        Compute the linear combination of vectors with given scalars.
        """
        if len(vectors) != len(scalars):
            raise ValueError("Vectors and scalars must have the same length")

        # Start with a zero vector of the same dimension
        result_elements = [0] * len(vectors[0].elements)

        # Perform scaling and summing
        for vector, scalar in zip(vectors, scalars):
            scaled_vector = vector.scl(scalar)
            result_elements = [
                sum(x) for x in zip(result_elements, scaled_vector.elements)
            ]

        return cls(result_elements)