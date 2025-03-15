import sys
from Vector import Vector

def test_euclidean_norm():
    test_cases = [
        ([0], 0.0),
        ([1], 1.0),
        ([0, 0], 0.0),
        ([1, 0], 1.0),
        ([2, 1], 2.236067977),
        ([4, 2], 4.472135955),
        ([-4, -2], 4.472135955)
    ]
    for vec_data, expected in test_cases:
        v = Vector(vec_data)
        result = v.norm()
        if abs(result - expected) > 1e-6:
            raise AssertionError(f"test_euclidean_norm failed for {vec_data}: expected {expected}, got {result}")
    print("All test_euclidean_norm passed.")

def test_manhattan_norm():
    test_cases = [
        ([0], 0.0),
        ([1], 1.0),
        ([0, 0], 0.0),
        ([1, 0], 1.0),
        ([2, 1], 3.0),
        ([4, 2], 6.0),
        ([-4, -2], 6.0)
    ]
    for vec_data, expected in test_cases:
        v = Vector(vec_data)
        result = v.norm_1()
        if abs(result - expected) > 1e-6:
            raise AssertionError(f"test_manhattan_norm failed for {vec_data}: expected {expected}, got {result}")
    print("All test_manhattan_norm passed.")

def test_supremum_norm():
    test_cases = [
        ([0], 0.0),
        ([1, 0], 1.0),
        ([2, -5, 3], 5.0)
    ]
    for vec_data, expected in test_cases:
        v = Vector(vec_data)
        result = v.norm_inf()
        if abs(result - expected) > 1e-6:
            raise AssertionError(f"test_supremum_norm failed for {vec_data}: expected {expected}, got {result}")
    print("All test_supremum_norm passed.")

def test():
    u = Vector([0.0, 0.0, 0.0])
    if abs(u.norm_1() - 0.0) > 1e-6 or abs(u.norm() - 0.0) > 1e-6 or abs(u.norm_inf() - 0.0) > 1e-6:
        raise AssertionError("Test failed for Vector([0.,0.,0.])")

    u = Vector([1.0, 2.0, 3.0])
    if abs(u.norm_1() - 6.0) > 1e-6 or abs(u.norm() - 3.74165738) > 1e-6 or abs(u.norm_inf() - 3.0) > 1e-6:
        raise AssertionError("Test failed for Vector([1.,2.,3.])")

    u = Vector([-1.0, -2.0])
    if abs(u.norm_1() - 3.0) > 1e-6 or abs(u.norm() - 2.236067977) > 1e-6 or abs(u.norm_inf() - 2.0) > 1e-6:
        raise AssertionError("Test failed for Vector([-1.,-2.])")
    print("All subject norm tests passed.")

def main():
    try:
        test_euclidean_norm()
        test_manhattan_norm()
        test_supremum_norm()
        test()
    except AssertionError as e:
        print("Test failed:", e)
        sys.exit(1)
    print("All tests passed.")

if __name__ == "__main__":
    main()
