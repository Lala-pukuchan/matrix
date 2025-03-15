import sys
from Matrix import Matrix


def test():
    test_cases = [
        ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
        ([[1, 0], [0, 1]], [[1, 0], [0, 1]]),
        ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
        ([[1, 2], [3, 4], [5, 6]], [[1, 3, 5], [2, 4, 6]]),
    ]

    for input_data, expected in test_cases:
        m = Matrix(input_data)
        result = m.transpose()
        if result.data != expected:
            raise AssertionError(
                f"Transpose test failed for {input_data}: expected {expected}, got {result.data}"
            )
    print("All transpose tests passed.")


def main():
    try:
        test()
    except AssertionError as e:
        print("Test failed:", e)
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    main()
