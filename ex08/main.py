import sys
from Matrix import Matrix


def test():
    test_cases = [
        ([[0, 0], [0, 0]], 0),
        ([[1, 0], [0, 1]], 2),
        ([[1, 2], [3, 4]], 5),
        ([[8, -7], [4, 2]], 10),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
    ]
    for data, expected in test_cases:
        m = Matrix(data)
        result = m.trace()
        if abs(result - expected) > 1e-6:
            raise AssertionError(
                f"Test failed for matrix {data}: expected trace {expected}, got {result}"
            )
    print("All trace tests passed in test().")


def test_from_subject():
    m = Matrix([[1.0, 0.0], [0.0, 1.0]])
    if abs(m.trace() - 2.0) > 1e-6:
        raise AssertionError(
            f"Subject test failed for identity matrix: expected 2.0, got {m.trace()}"
        )

    m = Matrix([[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]])
    if abs(m.trace() - 9.0) > 1e-6:
        raise AssertionError(
            f"Subject test failed for matrix: expected 9.0, got {m.trace()}"
        )

    m = Matrix([[-2.0, -8.0, 4.0], [1.0, -23.0, 4.0], [0.0, 6.0, 4.0]])
    if abs(m.trace() - (-21.0)) > 1e-6:
        raise AssertionError(
            f"Subject test failed for matrix: expected -21.0, got {m.trace()}"
        )

    print("All subject trace tests passed in test_from_subject().")


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
