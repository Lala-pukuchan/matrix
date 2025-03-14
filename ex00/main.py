import sys
from Vector import Vector
from Matrix import Matrix


def test_vector_addition():
    test_cases = [
        ([0, 0], [0, 0], [0, 0]),
        ([1, 0], [0, 1], [1, 1]),
        ([1, 1], [1, 1], [2, 2]),
        ([21, 21], [21, 21], [42, 42]),
        ([-21, 21], [21, -21], [0, 0]),
        (
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        ),
    ]
    for vec1, vec2, expected in test_cases:
        v1 = Vector(vec1)
        v2 = Vector(vec2)
        result = v1.add(v2)
        if result != expected:
            raise AssertionError(
                f"Vector addition failed:\n  {vec1} + {vec2} expected {expected} but got {result}"
            )
    print("All vector addition tests passed.")


def test_matrix_addition():
    test_cases = [
        ([[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]),
        ([[1, 0], [0, 1]], [[0, 0], [0, 0]], [[1, 0], [0, 1]]),
        ([[1, 1], [1, 1]], [[1, 1], [1, 1]], [[2, 2], [2, 2]]),
        ([[21, 21], [21, 21]], [[21, 21], [21, 21]], [[42, 42], [42, 42]]),
    ]
    for mat1, mat2, expected in test_cases:
        m1 = Matrix(mat1)
        m2 = Matrix(mat2)
        result = m1.add(m2)
        if result.data != expected:
            raise AssertionError(
                f"Matrix addition failed:\n  {mat1} + {mat2} expected {expected} but got {result.data}"
            )
    print("All matrix addition tests passed.")


def main():
    try:
        test_vector_addition()
        test_matrix_addition()
    except AssertionError as e:
        print("Test failed:", e)
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    main()
