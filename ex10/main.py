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
        ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
        ([[1, 0], [0, 1]], [[1, 0], [0, 1]]),
        ([[4, 2], [2, 1]], [[1, 0.5], [0, 0]]),
        ([[-7, 2], [4, 8]], [[1, 0], [0, 1]]),
        ([[1, 2], [4, 8]], [[1, 2], [0, 0]]),
    ]
    for input_data, expected in test_cases:
        m = Matrix(input_data)
        rref = m.row_echelon()
        if not matrix_almost_equal(rref.data, expected):
            raise AssertionError(
                f"Row echelon test failed for {input_data}:\nexpected {expected}\ngot {rref.data}"
            )
    print("All basic row echelon tests passed in test().")


def test_from_subject():
    u = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    expected = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    if not matrix_almost_equal(u.row_echelon().data, expected):
        raise AssertionError(
            f"Subject test 1 failed: expected {expected}, got {u.row_echelon().data}"
        )

    u = Matrix([[1.0, 2.0], [3.0, 4.0]])
    expected = [[1.0, 0.0], [0.0, 1.0]]
    if not matrix_almost_equal(u.row_echelon().data, expected):
        raise AssertionError(
            f"Subject test 2 failed: expected {expected}, got {u.row_echelon().data}"
        )

    u = Matrix([[1.0, 2.0], [2.0, 4.0]])
    expected = [[1.0, 2.0], [0.0, 0.0]]
    if not matrix_almost_equal(u.row_echelon().data, expected):
        raise AssertionError(
            f"Subject test 3 failed: expected {expected}, got {u.row_echelon().data}"
        )

    u = Matrix(
        [
            [8.0, 5.0, -2.0, 4.0, 28.0],
            [4.0, 2.5, 20.0, 4.0, -4.0],
            [8.0, 5.0, 1.0, 4.0, 17.0],
        ]
    )
    expected = [
        [1.0, 0.625, 0.0, 0.0, -12.1666667],
        [0.0, 0.0, 1.0, 0.0, -3.6666667],
        [0.0, 0.0, 0.0, 1.0, 29.5],
    ]
    if not matrix_almost_equal(u.row_echelon().data, expected):
        raise AssertionError(
            f"Subject test 4 failed: expected {expected}, got {u.row_echelon().data}"
        )

    print("All subject row echelon tests passed in test_from_subject().")


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
