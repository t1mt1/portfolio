import numpy as np

def free(x):
    return 0

def barrier(x):
    V = np.zeros_like(x)
    mask = (x >= 5) & (x <= 6)
    V[mask] = 3
    return V

def harmonic_oscillator(x, k):
    return k * x**2
