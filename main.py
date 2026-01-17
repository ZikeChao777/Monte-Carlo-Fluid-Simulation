from MC_separation_time import MC_separation_time
import numpy as np
import matplotlib.pyplot as plt
# Define a range of initial separation distances (in meters)
# Values are converted from micrometers to meters (e.g., 1 μm = 1e-6 m)
Dvec = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50])*1e-6
# Initialize a dictionary to store the results
# The keys will represent the initial separation distances, and the values will be the Monte Carlo results
res_dict = {}
# Loop through each initial separation distance in Dvec
for d0 in Dvec:
    # Perform Monte Carlo simulation for the current initial separation distance (d0)
    # Using 10,000 samples and a time step (h) of 1e-5 seconds
    mc_vec = MC_separation_time(d0, 10000, 1e-5)
    # Store the Monte Carlo results in the dictionary with a descriptive key
    res_dict[f"D0={d0}"] = mc_vec # At this point, `res_dict` contains the separation time distributions for each initial separation distance

# Print out the mean and standard deviation of separation times for each initial distance
print("Separation Times Statistics (in seconds):")
for key, values in res_dict.items():
    # Calculate the mean of the separation times for the current initial distance
    mean_time = np.mean(values)
    # Calculate the standard deviation of the separation times
    std_time = np.std(values)
    # Print the results with the corresponding initial separation distance
    print(f"{key}: Mean = {mean_time:.4f} s, Std Dev = {std_time:.4f} s")
# Plot the distribution of separation times for selected initial distances
plt.figure(figsize=(10, 6)) # Set the figure size to 10x6 inches
# Loop through each entry in the results dictionary to plot the histogram
for key, values in res_dict.items():
    # Plot a histogram for the current initial distance
    # `bins=50` sets the number of bins in the histogram
    # `alpha=0.6` controls the transparency of the histogram bars
    # `label=key` adds a label for the current dataset
    plt.hist(values, bins=50, alpha=0.6, label=key)
# Add labels, title, and legend to the plot
plt.xlabel("Separation Time (s)")
plt.ylabel("Frequency")
plt.title("Distribution of Separation Times for Different Initial Distances")
# Add a legend to distinguish histograms for different initial distances
plt.legend()
plt.grid(True)
# # Display the plot
plt.show()



