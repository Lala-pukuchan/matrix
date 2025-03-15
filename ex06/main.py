import sys
from Vector import Vector


def test():
    test_cases = [
        ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
        ([1, 0, 0], [0, 0, 0], [0, 0, 0]),
        ([1, 0, 0], [0, 1, 0], [0, 0, 1]),
        ([8, 7, -4], [3, 2, 1], [15, -20, -5]),
        ([1, 1, 1], [0, 0, 0], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
    ]
    for vdata1, vdata2, expected in test_cases:
        v1 = Vector(vdata1)
        v2 = Vector(vdata2)
        result = Vector.cross_product(v1, v2)
        if any(abs(r - e) > 1e-6 for r, e in zip(result.data, expected)):
            raise AssertionError(
                f"Basic cross product test failed: {vdata1} x {vdata2} expected {expected} but got {result.data}"
            )
    print("All basic cross product tests passed.")


def test_from_subject():
    u = Vector([0.0, 0.0, 1.0])
    v = Vector([1.0, 0.0, 0.0])
    result = Vector.cross_product(u, v)
    if any(abs(r - e) > 1e-6 for r, e in zip(result.data, [0.0, 1.0, 0.0])):
        raise AssertionError(
            f"Subject test 1 failed: expected [0.0, 1.0, 0.0] but got {result.data}"
        )

    u = Vector([1.0, 2.0, 3.0])
    v = Vector([4.0, 5.0, 6.0])
    result = Vector.cross_product(u, v)
    if any(abs(r - e) > 1e-6 for r, e in zip(result.data, [-3.0, 6.0, -3.0])):
        raise AssertionError(
            f"Subject test 2 failed: expected [-3.0, 6.0, -3.0] but got {result.data}"
        )

    u = Vector([4.0, 2.0, -3.0])
    v = Vector([-2.0, -5.0, 16.0])
    result = Vector.cross_product(u, v)
    if any(abs(r - e) > 1e-6 for r, e in zip(result.data, [17.0, -58.0, -16.0])):
        raise AssertionError(
            f"Subject test 3 failed: expected [17.0, -58.0, -16.0] but got {result.data}"
        )
    print("All subject cross product tests passed.")


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
