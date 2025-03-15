import sys
from Vector import Vector


def test_linear_combination():
    test_cases = [
        ([Vector([-42.0, 42.0])], [-1.0], [42.0, -42.0]),
        ([Vector([-42.0]), Vector([-42.0]), Vector([-42.0])], [-1.0, 1.0, 0.0], [0.0]),
        (
            [Vector([-42.0, 42.0]), Vector([1.0, 3.0]), Vector([10.0, 20.0])],
            [1.0, -10.0, -1.0],
            [-62.0, -8.0],
        ),
        (
            [Vector([-42.0, 100.0, -69.5]), Vector([1.0, 3.0, 5.0])],
            [1.0, -10.0],
            [-52.0, 70.0, -119.5],
        ),
    ]
    for vectors, coefs, expected in test_cases:
        result = Vector.linear_combination(vectors, coefs)
        if result != expected:
            raise AssertionError(
                f"Linear combination failed:\n  vectors: {[str(v) for v in vectors]}, coefs: {coefs}\n  expected {expected} but got {result}"
            )


def test_linear_combination_from_subject():
    # テスト1
    e1 = Vector([1.0, 0.0, 0.0])
    e2 = Vector([0.0, 1.0, 0.0])
    e3 = Vector([0.0, 0.0, 1.0])
    result = Vector.linear_combination([e1, e2, e3], [10.0, -2.0, 0.5])
    if result != [10.0, -2.0, 0.5]:
        raise AssertionError(
            f"Subject linear combination test 1 failed: expected [10.0, -2.0, 0.5], got {result}"
        )

    # テスト2
    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([0.0, 10.0, -100.0])
    result = Vector.linear_combination([v1, v2], [10.0, -2.0])
    if result != [10.0, 0.0, 230.0]:
        raise AssertionError(
            f"Subject linear combination test 2 failed: expected [10.0, 0.0, 230.0], got {result}"
        )


def main():
    try:
        test_linear_combination()
        test_linear_combination_from_subject()
        print("All linear combination from subject tests passed.")
    except AssertionError as e:
        print("Test failed:", e)
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    main()
