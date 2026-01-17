from separation_time_solver import separation_time_solver
import numpy as np
from tqdm import tqdm
def MC_separation_time(D0, N, h):
    # Performs a Monte Carlo simulation to estimate the distribution of separation times
    # for a flavor particle detaching from a thin film of oil.
    # Parameters:
    # D0 : float
    # Initial separation distance (m).
    # N : int
    # Number of Monte Carlo simulations (number of random samples).
    # h : float
    # Time step for the iteration (s).
    # Returns:
    # st_vec : list of float
    # List of separation times (s) for each Monte Carlo simulation.
    # Mass of the flavor particle (kg)
    m = 0.74e-3 # Given as 0.74 g
    # Initialize a list to store the separation times from each simulation
    st_vec = []
    # Loop over N simulations
    for i in tqdm(range(N)): # tqdm provides a progress bar for monitoring
        # Randomly sample the radius of the particle (R) from a uniform distribution
        R = np.random.uniform(0.1e-3, 1e-3) # Radius between 0.1 mm and 1 mm (in meters)
        # Randomly sample the viscosity (eta) from a normal distribution
        eta = np.random.normal(0.2, 0.02) # Mean viscosity is 0.2 Pa.s with std dev of 0.02
        # Compute the separation time using the separation_time_solver function
        st_vec.append(separation_time_solver(D0, 0, m, eta, R, h))
        # Return the list of separation times
    return st_vec