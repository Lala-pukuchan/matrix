class Vector:
    def __init__(self, data):
        self.data = list(data)

    def __str__(self):
        return str(self.data)

    @staticmethod
    def linear_combination(vectors, coefs):
        if len(vectors) != len(coefs):
            raise ValueError("The vectors and coefficients must have the same length.")
        result = [0] * len(vectors[0].data)
        for i in range(len(vectors)):
            for j in range(len(vectors[i].data)):
                result[j] += vectors[i].data[j] * coefs[i]
        return result
