import sys
from Vector import Vector
from Matrix import Matrix


def test_number():
    if Vector.lerp(0.0, 1.0, 0.0) != 0.0:
        raise AssertionError("test_number: lerp(0.,1.,0.) failed")
    if Vector.lerp(0.0, 1.0, 1.0) != 1.0:
        raise AssertionError("test_number: lerp(0.,1.,1.) failed")
    if Vector.lerp(0.0, 42.0, 0.5) != 21.0:
        raise AssertionError("test_number: lerp(0.,42.,0.5) failed")
    if Vector.lerp(-42.0, 42.0, 0.5) != 0.0:
        raise AssertionError("test_number: lerp(-42.,42.,0.5) failed")
    print("All test_number passed.")


def test_vector():
    v1 = Vector([-42.0, 42.0])
    v2 = Vector([42.0, -42.0])
    result = Vector.lerp(v1, v2, 0.5)
    if result.data != [0.0, 0.0]:
        raise AssertionError(
            f"test_vector failed: expected [0.0, 0.0] but got {result.data}"
        )
    print("All test_vector passed.")


def test_number_from_subject():
    if Vector.lerp(0.0, 1.0, 0.0) != 0.0:
        raise AssertionError("test_number_from_subject failed on lerp(0.,1.,0.)")
    if Vector.lerp(0.0, 1.0, 1.0) != 1.0:
        raise AssertionError("test_number_from_subject failed on lerp(0.,1.,1.)")
    if Vector.lerp(0.0, 1.0, 0.5) != 0.5:
        raise AssertionError("test_number_from_subject failed on lerp(0.,1.,0.5)")
    if abs(Vector.lerp(21.0, 42.0, 0.3) - 27.3) > 1e-6:
        raise AssertionError("test_number_from_subject failed on lerp(21.,42.,0.3)")
    print("All test_number_from_subject passed.")


def test_vector_from_subject():
    v1 = Vector([2.0, 1.0])
    v2 = Vector([4.0, 2.0])
    result = Vector.lerp(v1, v2, 0.3)
    expected = [2.6, 1.3]
    for r, e in zip(result.data, expected):
        if abs(r - e) > 1e-6:
            raise AssertionError(
                f"test_vector_from_subject failed: expected {expected}, got {result.data}"
            )
    print("All test_vector_from_subject passed.")


def test_matrix_from_subject():
    m1 = Matrix([[2.0, 1.0], [3.0, 4.0]])
    m2 = Matrix([[20.0, 10.0], [30.0, 40.0]])
    result = Matrix.lerp(m1, m2, 0.5)
    expected = [[11.0, 5.5], [16.5, 22.0]]
    for i in range(len(expected)):
        for j in range(len(expected[0])):
            if abs(result.data[i][j] - expected[i][j]) > 1e-6:
                raise AssertionError(
                    f"test_matrix_from_subject failed: expected {expected}, got {result.data}"
                )
    print("All test_matrix_from_subject passed.")


def main():
    try:
        test_number()
        test_vector()
        test_number_from_subject()
        test_vector_from_subject()
        test_matrix_from_subject()
    except AssertionError as e:
        print("Test failed:", e)
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    main()
