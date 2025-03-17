import sys
from Matrix import Matrix


def test():
    test_cases = [
        ([[0, 0], [0, 0]], 0),
        ([[1, 0], [0, 1]], 2),
        ([[2, 0], [0, 2]], 2),
        ([[1, 1], [1, 1]], 1),
        ([[0, 1], [1, 0]], 2),
        ([[1, 2], [3, 4]], 2),
        ([[-7, 5], [4, 6]], 2),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
    ]
    for data, expected_rank in test_cases:
        m = Matrix(data)
        rank = m.rank()
        if rank != expected_rank:
            raise AssertionError(
                f"Test failed for matrix {data}: expected rank {expected_rank}, got {rank}"
            )
    print("All basic rank tests passed in test().")


def test_from_subject():
    u = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    if u.rank() != 3:
        raise AssertionError(f"Subject test 1 failed: expected rank 3, got {u.rank()}")

    u = Matrix([[1.0, 2.0, 0.0, 0.0], [2.0, 4.0, 0.0, 0.0], [-1.0, 2.0, 1.0, 1.0]])
    if u.rank() != 2:
        raise AssertionError(f"Subject test 2 failed: expected rank 2, got {u.rank()}")

    u = Matrix([[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0], [21.0, 18.0, 7.0]])
    if u.rank() != 3:
        raise AssertionError(f"Subject test 3 failed: expected rank 3, got {u.rank()}")

    print("All subject rank tests passed in test_from_subject().")


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
