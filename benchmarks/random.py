"""
Random LP generator 

"""

import numpy as np
import random 

class RandomGenerator:
    def __init__(self, n_range, m_range, min, max, sparsity=1.0, degenerate=False):
        self.n_range = n_range
        self.m_range = m_range
        self.min = min
        self.max = max
        self.sparsity = sparsity
        self.degenerate = degenerate

    def genMatrix():
        # Generate matrices in range [self.min, self.max]
        A = np.random.rand(n, m) * (self.max - self.min) +  self.min
        b = np.random.rand(n, 1) * (self.max - self.min) +  self.min
        c = np.random.rand(m, 1) * (self.max - self.min) +  self.min

        # apply sparsity to A
        sparsity_vec = np.vectorize(applySparsity)

        A = sparsity_vec(A)
        b = sparsity_vec(b)
        c = sparsity_vec(c)

        # apply degeneracy

        return A, b, c


    def applySparsity(n):
        p = random.uniform()
        return n if n <= self.sparsity else 0.0 