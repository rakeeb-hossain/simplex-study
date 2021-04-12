from src.solver import SimplexSolver
from benchmarks.generate import RandomGenerator

import numpy as np
import src.pivot as pv
import sys

"""
Main method for calling SimplexSolver class

"""

if __name__ == "__main__":
    solver = SimplexSolver(is_degen=False, debug=False)
    test_num = 20
    sparsity_vals = [0.1, 0.3, 0.5, 0.7, 0.9]
    dims_n = 25
    dims_m = 75

    for s in sparsity_vals:
        gen = RandomGenerator([dims_n,dims_n+1], [dims_m,dims_m+1], -100, 100, sparsity=s)    
        stats = [[0,0] for i in range(0,4)]
        ctr = 0

        print("testing sparsity: " + str(s))

        while ctr < test_num:
            print("starting test " + str(ctr))
            # Generate LP
            c, A, b = gen.genLP()

            # Run solves
            try:
                res = []
                _ = solver.solve(c, A, b, pv.SteepestEdge2())
                res.append( [solver.num_pivots, solver.pivot_time] )
                print("done steepest2")

                _ = solver.solve(c, A, b, pv.DantzigsRule())
                res.append( [solver.num_pivots, solver.pivot_time] )
                print("done dantzig")

                _ = solver.solve(c, A, b, pv.BlandsRule())
                res.append( [solver.num_pivots, solver.pivot_time] )
                print("done blands")

                _ = solver.solve(c, A, b, pv.RandomRule())
                res.append( [solver.num_pivots, solver.pivot_time] )
                print("done random")

                
                for i, p in enumerate(res):
                    stats[i][0] = stats[i][0] + p[0]
                    stats[i][1] = stats[i][1] + p[1]
            except Exception as e:
                print(e)
                ctr = ctr - 1

            ctr = ctr + 1

        for p in stats:
            print("Results for sparsity {} \33[32m{}, {}\033[0m".format(s, p[0]/test_num, p[1]/test_num), file=sys.stderr)
