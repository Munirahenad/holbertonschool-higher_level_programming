#!/usr/bin/python3
"""Module for matrix multiplication."""


def matrix_mul(m_a, m_b):
    """Multiply 2 matrices.

    Args:
        m_a: first matrix (list of lists of int/float)
        m_b: second matrix (list of lists of int/float)

    Returns:
        New matrix = m_a * m_b

    Raises:
        TypeError / ValueError with exact required messages.
    """
    # 1) must be a list
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    # 2) must be list of lists
    if not all(type(row) is list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) is list for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3) can't be empty ([] or [[]])
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4) elements must be int/float
    for row in m_a:
        for x in row:
            if type(x) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for x in row:
            if type(x) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    # 5) must be rectangle (same row sizes)
    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")

    # 6) multiplication compatibility
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # multiply
    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            s = 0
            for k in range(len(m_b)):
                s += m_a[i][k] * m_b[k][j]
            new_row.append(s)
        result.append(new_row)

    return result

