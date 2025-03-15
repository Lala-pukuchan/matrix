class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]

    def __str__(self):
        return "\n".join(str(row) for row in self.data)

    @staticmethod
    def lerp(m1, m2, a):
        if isinstance(m1, (int, float)):
            return (1 - a) * m1 + a * m2
        elif isinstance(m1, Matrix) and isinstance(m2, Matrix):
            if len(m1.data) != len(m2.data) or len(m1.data[0]) != len(m2.data[0]):
                raise ValueError("Matrix must have the same shape")

            return Matrix(
                [
                    [
                        (1 - a) * m1.data[i][j] + a * m2.data[i][j]
                        for j in range(len(m1.data[0]))
                    ]
                    for i in range(len(m1.data))
                ]
            )
        else:
            raise ValueError("Invalid arguments")
