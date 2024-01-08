#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    try:
        result = np.dot(m_a, m_b)
        return result
    except ValueError as e:
        raise ValueError(f"Matrices cannot be multiplied: {e}")
