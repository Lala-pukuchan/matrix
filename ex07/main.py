#!/usr/bin/env python3
import sys
from Vector import Vector
from Matrix import Matrix

def test():
    m_zero = Matrix([[0, 0], [0, 0]])
    v_any = Vector([4, 2])
    result = m_zero.mul_vec(v_any)
    if result.data != [0, 0]:
        raise AssertionError(f"Test failed for zero matrix: expected [0, 0], got {result.data}")
    
    m_id = Matrix([[1, 0], [0, 1]])
    result = m_id.mul_vec(v_any)
    if result.data != v_any.data:
        raise AssertionError(f"Test failed for identity matrix: expected {v_any.data}, got {result.data}")
    
    m_all1 = Matrix([[1, 1], [1, 1]])
    v = Vector([4, 2])
    result = m_all1.mul_vec(v)
    if result.data != [6, 6]:
        raise AssertionError(f"Test failed for matrix [[1,1],[1,1]]: expected [6,6], got {result.data}")
    
    m_diag2 = Matrix([[2, 0], [0, 2]])
    v = Vector([2, 1])
    result = m_diag2.mul_vec(v)
    if result.data != [4, 2]:
        raise AssertionError(f"Test failed for matrix [[2,0],[0,2]]: expected [4,2], got {result.data}")
    
    m_half = Matrix([[0.5, 0], [0, 0.5]])
    v = Vector([4, 2])
    result = m_half.mul_vec(v)
    if result.data != [2, 1]:
        raise AssertionError(f"Test failed for matrix [[0.5,0],[0,0.5]]: expected [2,1], got {result.data}")
    
    print("All test (mul_vec) basic tests passed.")
    
    m1 = Matrix([[1, 0], [0, 1]])
    m2 = Matrix([[1, 0], [0, 1]])
    result_mat = m1.mul_mat(m2)
    if result_mat.data != [[1, 0], [0, 1]]:
        raise AssertionError(f"Test failed for identity matrix multiplication: expected [[1,0],[0,1]], got {result_mat.data}")
    
    m1 = Matrix([[1, 0], [0, 1]])
    m2 = Matrix([[2, 1], [4, 2]])
    result_mat = m1.mul_mat(m2)
    if result_mat.data != [[2, 1], [4, 2]]:
        raise AssertionError(f"Test failed for identity * matrix: expected [[2,1],[4,2]], got {result_mat.data}")
    
    m1 = Matrix([[3, -5], [6, 8]])
    m2 = Matrix([[2, 1], [4, 2]])
    result_mat = m1.mul_mat(m2)
    if result_mat.data != [[-14, -7], [44, 22]]:
        raise AssertionError(f"Test failed for matrix multiplication: expected [[-14,-7],[44,22]], got {result_mat.data}")
    
    print("All test (mul_mat) basic tests passed.")

def test_from_subject():
    u = Matrix([[1.0, 0.0], [0.0, 1.0]])
    v = Vector([4.0, 2.0])
    result = u.mul_vec(v)
    if result.data != [4.0, 2.0]:
        raise AssertionError(f"test_from_subject mul_vec test1 failed: expected [4.0,2.0], got {result.data}")
    
    u = Matrix([[2.0, 0.0], [0.0, 2.0]])
    v = Vector([4.0, 2.0])
    result = u.mul_vec(v)
    if result.data != [8.0, 4.0]:
        raise AssertionError(f"test_from_subject mul_vec test2 failed: expected [8.0,4.0], got {result.data}")
    
    u = Matrix([[2.0, -2.0], [-2.0, 2.0]])
    v = Vector([4.0, 2.0])
    result = u.mul_vec(v)
    if result.data != [4.0, -4.0]:
        raise AssertionError(f"test_from_subject mul_vec test3 failed: expected [4.0,-4.0], got {result.data}")
    
    u = Matrix([[1.0, 0.0], [0.0, 1.0]])
    v = Matrix([[1.0, 0.0], [0.0, 1.0]])
    result_mat = u.mul_mat(v)
    if result_mat.data != [[1.0, 0.0], [0.0, 1.0]]:
        raise AssertionError(f"test_from_subject mul_mat test1 failed: expected identity, got {result_mat.data}")
    
    u = Matrix([[1.0, 0.0], [0.0, 1.0]])
    v = Matrix([[2.0, 1.0], [4.0, 2.0]])
    result_mat = u.mul_mat(v)
    if result_mat.data != [[2.0, 1.0], [4.0, 2.0]]:
        raise AssertionError(f"test_from_subject mul_mat test2 failed: expected [[2.,1.],[4.,2.]], got {result_mat.data}")
    
    u = Matrix([[3.0, -5.0], [6.0, 8.0]])
    v = Matrix([[2.0, 1.0], [4.0, 2.0]])
    result_mat = u.mul_mat(v)
    if result_mat.data != [[-14.0, -7.0], [44.0, 22.0]]:
        raise AssertionError(f"test_from_subject mul_mat test3 failed: expected [[-14., -7.],[44.,22.]], got {result_mat.data}")
    
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
