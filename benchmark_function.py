import numpy as np
from scipy import optimize


def sphere(vector):
    if all(-100 <= e <= 100 for e in vector):
        return np.sum(e**2 for e in vector)
    else:
        # using the infinity strategy
        # TODO: in particle swarm?
        return float("inf")


def rosenbrock(vector):
    if all(-30 <= e <= 30 for e in vector):
        return optimize.rosen(vector)
    else:
        return float("inf")


def rastrigin(vector):
    return 10 * len(vector) + np.sum(e**2 - 10 * np.cos(2 * np.pi * e) for e in vector)


def schwefel(vector):
    return sum(-e * np.sin(np.sqrt(np.abs(e))) for e in vector)
