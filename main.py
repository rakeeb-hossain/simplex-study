from src.solver import SimplexSolver
from benchmarks.generate import RandomGenerator

import numpy as np
import src.pivot as pv
import sys

"""
Main method for calling SimplexSolver class

"""

if __name__ == "__main__":
    solver = SimplexSolver()
    gen = RandomGenerator([25,100], [25,100], -100, 100, sparsity=0.90)    
    test_num = 1

    for i in range(0, test_num):
        # Generate LP
        c, A, b = gen.genLP()

        # Run solves
        _ = solver.solve(c, A, b, pv.DantzigsRule())
        print("\33[32m{}, {}\033[0m".format(solver.num_pivots, solver.pivot_time), file=sys.stderr)

        _ = solver.solve(c, A, b, pv.BlandsRule())
        print("\33[32m{}, {}\033[0m".format(solver.num_pivots, solver.pivot_time), file=sys.stderr)

        _ = solver.solve(c, A, b, pv.RandomRule())
        print("\33[32m{}, {}\033[0m".format(solver.num_pivots, solver.pivot_time), file=sys.stderr)
