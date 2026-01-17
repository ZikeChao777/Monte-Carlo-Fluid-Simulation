# Stochastic Simulation of Particle Separation

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-green.svg)

## 📖 Overview
This project simulates the fluid dynamics of flavour particles separating from a thin oil film. It implements a **Numerical Solver** using the Finite Difference Method (FDM) and employs **Monte Carlo Simulation** to quantify the impact of stochastic manufacturing uncertainties (particle radius and viscosity) on separation times.

## 🧮 Mathematical Framework

### 1. Governing Equation (Fluid Dynamics)
The particle motion is governed by Newton's Second Law, incorporating viscous drag and external force. The 2nd-order ODE is defined as:

$$m \frac{d^2D}{dt^2} = F_0 - 6\pi\eta R^2 \frac{1}{D}\frac{dD}{dt}$$

Where:
- $D(t)$: Separation distance between particle and film.
- $F_0$: Applied external force.
- $\eta$: Dynamic viscosity of the oil.
- $R$: Particle radius.

### 2. Monte Carlo Stochastic Model
To model real-world variability, the simulation performs iterative sampling:
- **Radius ($R$):** Sampled from Uniform Distribution $U(0.1, 1.0) \text{ mm}$.
- **Viscosity ($\eta$):** Sampled from Normal Distribution $\mathcal{N}(0.2, 0.02^2) \text{ Pa}\cdot\text{s}$.

## 📂 Project Structure

```text
.
├── separation_time_solver.py  # Core ODE solver (Finite Difference Method)
├── MC_separation_time.py      # Monte Carlo kernel for stochastic sampling
├── main.py                    # Driver script for execution and plotting
├── simulation_result.png      # Visualization output
└── README.md                  # Project documentation

```
## 📊 Sample Output

Below is the visualization of the simulation results. The histogram displays the distribution of separation times for **10,000 stochastic runs**.

![Simulation Result](simulation_result.png)

*Figure 1: Probability distribution of separation times. The spread indicates the impact of manufacturing tolerances (radius) and viscosity fluctuations on process efficiency.*

## 🚀 How to Run

### Prerequisites
Ensure you have the required Python libraries installed:
```bash
pip install numpy matplotlib tqdm

