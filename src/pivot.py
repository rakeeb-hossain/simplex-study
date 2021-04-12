from abc import ABC, abstractmethod
import numpy as np
import random
import time
import timeit
import math
import collections

def timer(fxn):
    def timed_fxn(self, *arg, **kw):
        start = timeit.default_timer()
        fxn(self, *arg, **kw)
        elapsed = timeit.default_timer() - start
        self.elapsed  = self.elapsed + elapsed
    
    return timed_fxn

class PivotRule(ABC):
    def __init__(self):
        self.elapsed = 0
        self.A = None
        self.B = None
    
    @abstractmethod
    def computePivotIndex(self, reduced_costs):
        pass

class BlandsRule(PivotRule):
    def computePivotIndex(self, reduced_costs):
        chosen_j = 0

        od = collections.OrderedDict(sorted(reduced_costs.items()))

        for j in od.keys():
            if od[j] < 0.0:
                chosen_j = j
                break
        return chosen_j


class DantzigsRule(PivotRule):
    def computePivotIndex(self, reduced_costs):
        return min(reduced_costs, key=reduced_costs.get)

class RandomRule(PivotRule):
    def computePivotIndex(self, reduced_costs):
        negative_indices = []

        for j in reduced_costs.keys():
            if reduced_costs[j] < 0.0:
                negative_indices.append(j)            

        return random.choice(negative_indices)

class SteepestEdge(PivotRule):
    def computePivotIndex(self, reduced_costs):
        chosen_j = 0
        chosen_steepness = 0
        for j in reduced_costs.keys():
            if reduced_costs[j] < 0.0:
                colj = self.A[...,j].ravel() # denom = 2-norm of B^{-1} A_j
                column_squared = np.square(colj)
                accum = np.sum(column_squared)
                denom = math.sqrt(1 + accum)
                steepness = (reduced_costs[j] / denom)
                if (steepness < chosen_steepness):
                    chosen_steepness = steepness
                    chosen_j = j
        return chosen_j

class SteepestEdge2(PivotRule):
    def computePivotIndex(self, reduced_costs):
        chosen_j = 0
        chosen_steepness = 0
        for j in reduced_costs.keys():
            if reduced_costs[j] < 0.0:
                colj = self.A[...,j].ravel()
                d = np.linalg.solve(self.B, colj)
                denom = np.dot(d, d)
                denom = math.sqrt(denom + 1)
                steepness = (reduced_costs[j] / denom)
                if (steepness < chosen_steepness):
                    chosen_steepness = steepness
                    chosen_j = j
        return chosen_j
