from src.solver import SimplexSolver
from benchmarks.generate import RandomGenerator

import numpy as np
import src.pivot as pv
import sys

"""
Main method for calling SimplexSolver class

"""

if __name__ == "__main__":
    solver = SimplexSolver(is_degen=False)
    gen = RandomGenerator([25,100], [25,100], -100, 100, sparsity=0.90)    
    test_num = 1

    ctr = 0
    while ctr < test_num:
        # Generate LP
        c, A, b = gen.genLP()

        # Run solves
        try:
            _ = solver.solve(c, A, b, pv.SteepestEdge(A))
            print("\33[32m{}, {}\033[0m".format(solver.num_pivots, solver.pivot_time), file=sys.stderr)

            _ = solver.solve(c, A, b, pv.DantzigsRule(A))
            print("\33[32m{}, {}\033[0m".format(solver.num_pivots, solver.pivot_time), file=sys.stderr)

            _ = solver.solve(c, A, b, pv.BlandsRule(A))
            print("\33[32m{}, {}\033[0m".format(solver.num_pivots, solver.pivot_time), file=sys.stderr)

            _ = solver.solve(c, A, b, pv.RandomRule(A))
            print("\33[32m{}, {}\033[0m".format(solver.num_pivots, solver.pivot_time), file=sys.stderr)
        except:
            print("ERROR")
            ctr = ctr - 1

        ctr = ctr + 1
