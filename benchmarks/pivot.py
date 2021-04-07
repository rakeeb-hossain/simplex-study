from abc import ABC, abstractmethod
import numpy as np
import random

class PivotRule(ABC):
    def __init__(self):
        self.time = 0
        self.A = A
        super().__init__()
    
    @abstractmethod
    def computePivotIndex(self):
        pass

    

def Bland(reduced_costs):
    chosen_j = 0
    for j in reduced_costs.keys():
		if reduced_costs[j] < 0.0:
			chosen_j = j
				break
    return chosen_j
    
def Dantzig(reduced_costs):
    return np.argmin(reduced_costs)[0]

def Random(reduced_costs):
    negative_indices = []

    for i, x in enumerate(reduced_costs):
        if x < 0:
            negative_indices.append(i)            

    return random.choice(negative_indices)