import sys
from Matrix import Matrix


def test():
    test_cases = [
        ([[0, 0], [0, 0]], 0.0),
        ([[1, 0], [0, 1]], 1.0),
        ([[2, 0], [0, 2]], 4.0),
        ([[1, 1], [1, 1]], 0.0),
        ([[0, 1], [1, 0]], -1.0),
        ([[1, 2], [3, 4]], -2.0),
        ([[-7, 5], [4, 6]], -62.0),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 1.0),
    ]
    tol = 1e-6
    for data, expected in test_cases:
        m = Matrix(data)
        det = m.determinant()
        if abs(det - expected) > tol:
            raise AssertionError(
                f"Test failed for matrix {data}: expected determinant {expected}, got {det}"
            )
    print("All determinant tests passed in test().")


def test_from_subject():
    tol = 1e-6
    m = Matrix([[1.0, -1.0], [-1.0, 1.0]])
    if abs(m.determinant() - 0.0) > tol:
        raise AssertionError(
            f"Subject test 1 failed: expected 0.0, got {m.determinant()}"
        )

    m = Matrix([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
    if abs(m.determinant() - 8.0) > tol:
        raise AssertionError(
            f"Subject test 2 failed: expected 8.0, got {m.determinant()}"
        )

    m = Matrix([[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0]])
    if abs(m.determinant() - (-174.0)) > tol:
        raise AssertionError(
            f"Subject test 3 failed: expected -174.0, got {m.determinant()}"
        )

    m = Matrix(
        [
            [8.0, 5.0, -2.0, 4.0],
            [4.0, 2.5, 20.0, 4.0],
            [8.0, 5.0, 1.0, 4.0],
            [28.0, -4.0, 17.0, 1.0],
        ]
    )
    if abs(m.determinant() - 1032.0) > tol:
        raise AssertionError(
            f"Subject test 4 failed: expected 1032.0, got {m.determinant()}"
        )

    print("All subject determinant tests passed in test_from_subject().")


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
