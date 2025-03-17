import sys
from Matrix import Matrix

def matrix_almost_equal(m1, m2, tol=1e-6):
    if len(m1) != len(m2):
        return False
    for row1, row2 in zip(m1, m2):
        if len(row1) != len(row2):
            return False
        for a, b in zip(row1, row2):
            if abs(a - b) > tol:
                return False
    return True

def test():
    test_cases = [
        ([[1, 0], [0, 1]], [[1, 0], [0, 1]]),
        ([[2, 0], [0, 2]], [[0.5, 0], [0, 0.5]]),
        ([[0.5, 0], [0, 0.5]], [[2, 0], [0, 2]]),
        ([[0, 1], [1, 0]], [[0, 1], [1, 0]]),
        ([[1, 2], [3, 4]], [[-2, 1], [1.5, -0.5]]),
        (
            [[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]],
            [[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]]
        )
    ]
    tol = 1e-6
    for data, expected in test_cases:
        m = Matrix(data)
        inv = m.inverse()
        if not matrix_almost_equal(inv.data, expected, tol):
            raise AssertionError(f"Test failed for matrix {data}: expected inverse {expected}, got {inv.data}")
    print("All basic inverse tests passed in test().")

def test_from_subject():
    tol = 1e-6
    u = Matrix([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ])
    expected = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ]
    inv = u.inverse()
    if not matrix_almost_equal(inv.data, expected, tol):
        raise AssertionError(f"Subject test 1 failed: expected {expected}, got {inv.data}")

    u = Matrix([
        [2.0, 0.0, 0.0],
        [0.0, 2.0, 0.0],
        [0.0, 0.0, 2.0]
    ])
    expected = [
        [0.5, 0.0, 0.0],
        [0.0, 0.5, 0.0],
        [0.0, 0.0, 0.5]
    ]
    inv = u.inverse()
    if not matrix_almost_equal(inv.data, expected, tol):
        raise AssertionError(f"Subject test 2 failed: expected {expected}, got {inv.data}")

    u = Matrix([
        [8.0, 5.0, -2.0],
        [4.0, 7.0, 20.0],
        [7.0, 6.0, 1.0]
    ])
    expected = [
        [0.649425287, 0.097701149, -0.655172414],
        [-0.781609195, -0.126436782, 0.965517241],
        [0.143678161, 0.074712644, -0.206896552]
    ]
    inv = u.inverse()
    if not matrix_almost_equal(inv.data, expected, tol):
        raise AssertionError(f"Subject test 3 failed: expected {expected}, got {inv.data}")

    print("All subject inverse tests passed in test_from_subject().")

def main():
    try:
        test()
        test_from_subject()
    except AssertionError as e:
        print("Test failed:", e)
        sys.exit(1)
    print("All tests passed.")

if __name__ == "__main__":
    main()
