import sys
from Vector import Vector


def test():
    test_cases = [
        ([1, 0], [0, 1], 0.0),
        ([8, 7], [3, 2], 0.9914542955425437),
        ([1, 1], [1, 1], 1.0),
        ([4, 2], [1, 1], 0.9486832980505138),
        ([-7, 3], [6, 4], -0.5462677805469223),
    ]
    for a, b, expected in test_cases:
        v1 = Vector(a)
        v2 = Vector(b)
        res = Vector.angle_cos(v1, v2)
        if abs(res - expected) > 1e-6:
            raise AssertionError(
                f"Basic test failed for {a} and {b}: expected {expected}, got {res}"
            )
        res_swapped = Vector.angle_cos(v2, v1)
        if abs(res_swapped - expected) > 1e-6:
            raise AssertionError(
                f"Commutativity test failed for {a} and {b}: expected {expected}, got {res_swapped}"
            )
    print("All basic angle_cos tests passed.")


def test_from_subject():
    u = Vector([1.0, 0.0])
    v = Vector([1.0, 0.0])
    if abs(Vector.angle_cos(u, v) - 1.0) > 1e-6:
        raise AssertionError(
            f"test_from_subject failed: expected 1.0, got {Vector.angle_cos(u, v)}"
        )

    u = Vector([1.0, 0.0])
    v = Vector([0.0, 1.0])
    if abs(Vector.angle_cos(u, v) - 0.0) > 1e-6:
        raise AssertionError(
            f"test_from_subject failed: expected 0.0, got {Vector.angle_cos(u, v)}"
        )

    u = Vector([-1.0, 1.0])
    v = Vector([1.0, -1.0])
    if abs(Vector.angle_cos(u, v) - (-1.0)) > 1e-6:
        raise AssertionError(
            f"test_from_subject failed: expected -1.0, got {Vector.angle_cos(u, v)}"
        )

    u = Vector([2.0, 1.0])
    v = Vector([4.0, 2.0])
    if abs(Vector.angle_cos(u, v) - 1.0) > 1e-6:
        raise AssertionError(
            f"test_from_subject failed: expected 1.0, got {Vector.angle_cos(u, v)}"
        )

    u = Vector([1.0, 2.0, 3.0])
    v = Vector([4.0, 5.0, 6.0])
    if abs(Vector.angle_cos(u, v) - 0.974631846) > 1e-6:
        raise AssertionError(
            f"test_from_subject failed: expected 0.974631846, got {Vector.angle_cos(u, v)}"
        )

    print("All test_from_subject passed.")


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
