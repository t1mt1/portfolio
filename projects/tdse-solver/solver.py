from scipy.special import hermite, factorial
import numpy as np
import potentials
from scipy import linalg
from scipy.sparse import diags 
from scipy.sparse.linalg import spsolve, splu 
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter
import initial_conditions
from initial_conditions import gaussian_wavepacket, harmonic_oscillator_eigenstate

#constants
hbar = 1  
m = 1  


class TDSE_Solver:

    def __init__(self, potential_func=potentials.free, L=25, N=2000, J=1000, dt=0.001):
        #parameters
        self.L = L
        self.N = N
        self.J = J
        self.dt = dt
        self.dx = L / J
        self.lambda_ = dt / (2 * self.dx**2)
        self.x = np.linspace(-L/4, 3*L/4, J)
        self.V = potential_func(self.x) 
        #matrix coefficients
        c1 = (hbar**2/(2*m))*self.lambda_
        c2 = 1j*hbar -(hbar**2/m)*self.lambda_ - (self.V*self.dt)/2
        c3 = 1j*hbar + (hbar**2/(m))*self.lambda_ + (self.V*self.dt)/2
        #constructing matrices A and B
        A = diags([c1*np.ones(J-1), c2, c1*np.ones(J-1)], [-1, 0, 1], shape=(J, J)).toarray()
        A[0, 0] += hbar**2/(2*m)
        A[J-1, J-1] += hbar**2/(2*m)
        B = diags([-c1*np.ones(J-1), c3, -c1*np.ones(J-1)], [-1, 0, 1], shape=(J, J)).toarray()
        B[0, 0] -= self.lambda_*hbar**2/(2*m) 
        B[J-1, J-1] -= self.lambda_*hbar**2/(2*m) 
        #precomputing the inverse of A multiplied by B
        self.C = np.linalg.solve(A, B)

    def time_step(self, psi):
        return np.dot(self.C, psi)
    
    def normalise(self, psi):
        return psi/np.sqrt(np.sum(np.abs(psi)**2) * self.dx)
