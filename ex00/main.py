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
        if result != expected:
            raise AssertionError(
                f"Matrix addition failed:\n  {mat1} + {mat2} expected {expected} but got {result}"
            )
    print("All matrix addition tests passed.")


def test_vector_subtraction():
    test_cases = [
        ([0, 0], [0, 0], [0, 0]),
        ([1, 0], [0, 1], [1, -1]),
        ([1, 1], [1, 1], [0, 0]),
        ([21, 21], [21, 21], [0, 0]),
        ([-21, 21], [21, -21], [-42, 42]),
        (
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9],
        ),
    ]
    for vec1, vec2, expected in test_cases:
        v1 = Vector(vec1)
        v2 = Vector(vec2)
        result = v1.sub(v2)
        if result != expected:
            raise AssertionError(
                f"Vector subtraction failed:\n  {vec1} - {vec2} expected {expected} but got {result}"
            )
    print("All vector subtraction tests passed.")


def test_matrix_subtraction():
    test_cases = [
        ([[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]),
        ([[1, 0], [0, 1]], [[0, 0], [0, 0]], [[1, 0], [0, 1]]),
        ([[1, 1], [1, 1]], [[1, 1], [1, 1]], [[0, 0], [0, 0]]),
        ([[21, 21], [21, 21]], [[21, 21], [21, 21]], [[0, 0], [0, 0]]),
    ]
    for mat1, mat2, expected in test_cases:
        m1 = Matrix(mat1)
        m2 = Matrix(mat2)
        result = m1.sub(m2)
        if result != expected:
            raise AssertionError(
                f"Matrix subtraction failed:\n  {mat1} - {mat2} expected {expected} but got {result}"
            )
    print("All matrix subtraction tests passed.")


def test_vector_scaling():
    test_cases = [
        ([0, 0], 1, [0, 0]),
        ([1, 0], 1, [1, 0]),
        ([1, 1], 2, [2, 2]),
        ([21, 21], 2, [42, 42]),
        ([42, 42], 0.5, [21, 21]),
    ]
    for vec, scalar, expected in test_cases:
        v = Vector(vec)
        result = v.scl(scalar)
        if result != expected:
            raise AssertionError(
                f"Vector scaling failed:\n  {vec} * {scalar} expected {expected} but got {result}"
            )
    print("All vector scaling tests passed.")


def test_matrix_scaling():
    test_cases = [
        ([[0, 0], [0, 0]], 0, [[0, 0], [0, 0]]),
        ([[1, 0], [0, 1]], 1, [[1, 0], [0, 1]]),
        ([[1, 2], [3, 4]], 2, [[2, 4], [6, 8]]),
        ([[21, 21], [21, 21]], 0.5, [[10.5, 10.5], [10.5, 10.5]]),
    ]
    for mat, scalar, expected in test_cases:
        m = Matrix(mat)
        result = m.scl(scalar)
        if result != expected:
            raise AssertionError(
                f"Matrix scaling failed:\n  {mat} * {scalar} expected {expected} but got {result}"
            )
    print("All matrix scaling tests passed.")


def test_vector_from_subject():
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0])
    result = u.add(v)
    if result != [7.0, 10.0]:
        raise AssertionError(
            f"test_vector_from_subject (add) failed: expected [7.0, 10.0], got {result}"
        )

    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0])
    result = u.sub(v)
    if result != [-3.0, -4.0]:
        raise AssertionError(
            f"test_vector_from_subject (sub) failed: expected [-3.0, -4.0], got {result}"
        )

    u = Vector([2.0, 3.0])
    result = u.scl(2.0)
    if result != [4.0, 6.0]:
        raise AssertionError(
            f"test_vector_from_subject (scl) failed: expected [4.0, 6.0], got {result}"
        )
    print("All vector from subject tests passed.")


def test_matrix_from_subject():
    u = Matrix([[1.0, 2.0], [3.0, 4.0]])
    v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
    result = u.add(v)
    if result != [[8.0, 6.0], [1.0, 6.0]]:
        raise AssertionError(
            f"test_matrix_from_subject (add) failed: expected [[8.0, 6.0], [1.0, 6.0]], got {result}"
        )

    u = Matrix([[1.0, 2.0], [3.0, 4.0]])
    v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
    result = u.sub(v)
    if result != [[-6.0, -2.0], [5.0, 2.0]]:
        raise AssertionError(
            f"test_matrix_from_subject (sub) failed: expected [[-6.0, -2.0], [5.0, 2.0]], got {result}"
        )

    u = Matrix([[1.0, 2.0], [3.0, 4.0]])
    result = u.scl(2.0)
    if result != [[2.0, 4.0], [6.0, 8.0]]:
        raise AssertionError(
            f"test_matrix_from_subject (scl) failed: expected [[2.0, 4.0], [6.0, 8.0]], got {result}"
        )
    print("All matrix from subject tests passed.")


def main():
    try:
        test_vector_addition()
        test_matrix_addition()
        test_vector_subtraction()
        test_matrix_subtraction()
        test_vector_scaling()
        test_matrix_scaling()
        test_vector_from_subject()
        test_matrix_from_subject()
    except AssertionError as e:
        print("Test failed:", e)
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    main()
