from src.solver import SimplexSolver
from benchmarks.generate import RandomGenerator

import numpy as np

"""
Main method for calling SimplexSolver class

"""


if __name__ == "__main__":
    solver = SimplexSolver()
    gen = RandomGenerator([10,10], [10,10], -100, 100, sparsity=0.5)    

    # Solve
    c, A, b = gen.genLP()
    x = solver.solve(c,A,b)
    print(x)
