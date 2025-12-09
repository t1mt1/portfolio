from scipy.special import hermite, factorial
import numpy as np




def gaussian_wavepacket(x, sigma=1, k0=3, x0=0):
 return (1/(2 * sigma**2 * np.pi))**0.25 * np.exp(1j * k0 * x) * np.exp(-((x - x0)**2) / (4 * sigma**2))

def harmonic_oscillator_eigenstate(n, x, m=1, hbar=1, omega=1):
    xi = np.sqrt(m * omega / hbar) * x
    Hn = hermite(n)(xi)
    prefactor = 1.0 / np.sqrt(2**n * factorial(n)) * (m*omega/(np.pi*hbar))**0.25
    psi_n = prefactor * Hn * np.exp(-0.5 * xi**2)
    return psi_n