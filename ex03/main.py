import sys
from Vector import Vector


def test():
    test_cases = [
        ([0, 0], [0, 0], 0),
        ([1, 0], [0, 0], 0),
        ([1, 0], [1, 0], 1),
        ([1, 0], [0, 1], 0),
        ([1, 1], [1, 1], 2),
        ([4, 2], [2, 1], 10),
    ]
    for vdata1, vdata2, expected in test_cases:
        v1 = Vector(vdata1)
        v2 = Vector(vdata2)
        result = Vector.dot(v1, v2)
        if abs(result - expected) > 1e-6:
            raise AssertionError(
                f"Dot product test failed: {vdata1} dot {vdata2} expected {expected} but got {result}"
            )
    print("All tests passed.")


def test_from_subject():
    # Test 1:
    u = Vector([0.0, 0.0])
    v = Vector([1.0, 1.0])
    result = Vector.dot(u, v)
    if abs(result - 0.0) > 1e-6:
        raise AssertionError(f"test_from_subject 1 failed: expected 0.0, got {result}")

    # Test 2:
    u = Vector([1.0, 1.0])
    v = Vector([1.0, 1.0])
    result = Vector.dot(u, v)
    if abs(result - 2.0) > 1e-6:
        raise AssertionError(f"test_from_subject 2 failed: expected 2.0, got {result}")

    # Test 3:
    u = Vector([-1.0, 6.0])
    v = Vector([3.0, 2.0])
    result = Vector.dot(u, v)
    if abs(result - 9.0) > 1e-6:
        raise AssertionError(f"test_from_subject 3 failed: expected 9.0, got {result}")

    print("All test_from_subject passed.")


def main():
    """
    v1: vector with (a1, a2)
    v2: vector with (b1, b2)
    v1·v2 = a1b1 + a2b2
    """
    try:
        test()
        test_from_subject()
    except AssertionError as e:
        print("Test failed:", e)
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    main()
