from src.solver import SimplexSolver

import numpy as np

"""
Main method for calling SimplexSolver class

"""


if '__name__' == '__main__':
    solver = SimplexSolver()

    # get c, A, b

    # solve
    x = solver.solve(c, A, b)
