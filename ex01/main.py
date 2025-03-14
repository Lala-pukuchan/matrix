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
                f"Linear combination failed:\n  vectors: {[str(v) for v in vectors]}, coefs: {coefs}\n  expected {expected} but got {result.data}"
            )
    print("All linear combination tests passed.")


def main():
    try:
        test_linear_combination()
    except AssertionError as e:
        print("Test failed:", e)
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    main()
