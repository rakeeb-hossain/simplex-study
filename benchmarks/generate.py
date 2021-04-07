"""
Random LP generator 

"""

import numpy as np
import random 

class RandomGenerator:
    def __init__(self, n_range, m_range, min_val, max_val, sparsity=1.0, degenerate=False):
        """
        Args
        n_range: 2-array of range for matrix length
        m_range: 2-array of range for matrix width
        min_val: min val for matrix entries
        max_val: max val for matrix entries
        sparsity: probability of an entry being 0
        degenerate: whether or not the LP is degenerate

        Ex.
        r = RandomGenerator([10,10], [10,10], -100, 100, sparsity=0.5)
        c, A, b = r.genLP()

        """

        self.n_range = n_range
        self.m_range = m_range
        self.min_val = min_val
        self.max_val = max_val
        self.sparsity = sparsity
        self.degenerate = degenerate

    def genLP(self):
        """
        Returns LP matrices c, A, b

        """

        # Select an n and m
        n = random.randint(self.n_range[0], self.n_range[1])
        m = random.randint(self.m_range[0], self.m_range[1])

        # Generate matrices in range [self.min, self.max]
        A = np.random.rand(n, m) * (self.max_val - self.min_val) +  self.min_val
        b = np.random.rand(n, 1) * (self.max_val - self.min_val) +  self.min_val
        c = np.random.rand(m, 1) * (self.max_val - self.min_val) +  self.min_val

        # apply sparsity to A
        sparsity_vec = np.vectorize(self.applySparsity)

        A = sparsity_vec(A)
        # b = sparsity_vec(b)
        # c = sparsity_vec(c)

        # apply degeneracy

        return c, A, b


    def applySparsity(self, n):
        p = random.uniform(0,1)
        return n if p <= self.sparsity else 0.0 

