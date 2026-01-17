import numpy as np

# Calculates the time required for a flavor particle to completely separate
# from a thin film of oil using an iterative numerical method.

# Parameters:
# D0 : float
#    Initial separation distance (m).
# v0 : float
#    Initial velocity of the particle (m/s).
# m : float
#    Mass of the flavor particle (kg).
# eta : float
#    Viscosity of the oil (Pa.s).
# R : float
#   Radius of the flavor particle (m).
# h : float
#    Time step for the iteration (s).

# Returns:
# t : float
#   Total separation time (s).

def separation_time_solver(D0, v0, m, eta, R, h):
    # Calculate the constant C, which represents the viscous drag coefficient
    C = 6 * np.pi * eta * R**2
    # Calculate the external force F0 acting on the particle (assumed to be gravitational force)
    F0 = m * 9.8
    # Initialize the first two positions based on the initial separation distance and velocity
    d0 = D0 # Initial position (m)
    d1 = h*v0+d0 # Position after the first time step (m)
    d2 = d1 # Temporary variable for the next position (m)

    # Initialize time counter
    t = 1 # Start from the first time step

    # Iterative loop: Continue until the separation distance d2 reaches a threshold
    while d2 < 0.1e-3: # Stop when the separation distance exceeds 0.1 mm (1e-4 m)
        # Calculate the numerator of the iterative formula for d2
        numerator = h**2 * F0 + h*C*d0/2/d1 - m *d0 + 2 * m *d1
        # Calculate the denominator of the iterative formula for d2
        denominator = m + h*C/2/d1
        # Update the next separation distance d2
        d2 = numerator / denominator
        # Update d0 and d1 for the next iteration
        d0, d1 = d1, d2
        # Increment time counter
        t = t + 1
    # Return the total separation time in seconds
    return t * h

