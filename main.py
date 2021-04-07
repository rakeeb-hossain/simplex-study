from src.solver import SimplexSolver
from benchmarks.generate import RandomGenerator

import numpy as np
import src.pivot as pv

"""
Main method for calling SimplexSolver class

"""

if __name__ == "__main__":
    solver = SimplexSolver()
    gen = RandomGenerator([100,100], [100,100], -100, 100, sparsity=0.5)    

    # Solve
    c, A, b = gen.genLP()
    print("LP generated!")
    x, obj_val = solver.solve(c, A, b, pv.DantzigsRule())
    print(x)
    print("Objective val: ")
    print(obj_val)
