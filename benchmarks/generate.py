"""
Random LP generator 

"""

import numpy as np
import random 


# TO-DO: Add option to ensure LP is feasible/unbounded

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

        np.random.seed(None)

    def genLP(self):
        """
        Returns feasible LP matrices c, A, b

        """
        while True:
            # Select an n and m
            n = np.random.randint(self.n_range[0], self.n_range[1])
            m = np.random.randint(self.m_range[0], self.m_range[1])

            # Generate matrices in range [self.min, self.max]
            A = np.random.rand(n, m) * (self.max_val - self.min_val) +  self.min_val
            x = np.random.rand(m, 1) * (self.max_val - self.min_val)
            c = np.random.rand(m, 1) * (self.max_val - self.min_val) +  self.min_val

            # apply sparsity to A
            sparsity_vec = np.vectorize(self.applySparsity)
            A = sparsity_vec(A)

            # ensure A is full rank, else try generating again
            if np.linalg.matrix_rank(A) < min(n, m):
                continue

            # generate b from Ax
            b = np.matmul(A,x)

            return c, A, b

    
    def genUnboundedLP(self):
        # Select an n and m
        n = random.randint(self.n_range[0], self.n_range[1])
        m = random.randint(self.m_range[0], self.m_range[1])

        # pick vectors u and v with v != 0
        u = np.random.rand(m, 1) * (self.max_val - self.min_val) +  self.min_val
        v = np.random.rand(m, 1) * (self.max_val - self.min_val) +  self.min_val

        # ensure v != 0
        if np.count_nonzero(v==0) != 0:
            r = random.randint(0,m-1)
            v[r] = random.uniform(self.min_val, self.max_val)

        # pick A
        A = np.random.rand(n, m) * (self.max_val - self.min_val) +  self.min_val
        sparsity_vec = np.vectorize(self.applySparsity)
        A = sparsity_vec(A)

        #

    def applySparsity(self, n):
        p = np.random.uniform(0,1)
        return 0.0 if p <= self.sparsity else n 

    def checkSparsity(self, A):
        zeroes = (A.shape[0] - np.count_nonzero(A, axis=0)).sum()
        s = float(zeroes)/(A.shape[0] * A.shape[1])
        print(s)
        
