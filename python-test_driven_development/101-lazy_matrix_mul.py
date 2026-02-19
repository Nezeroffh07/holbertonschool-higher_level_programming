#!/usr/bin/python3
"""Module for lazy_matrix_mul method using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices by using the module NumPy."""
    return np.matmul(m_a, m_b)
