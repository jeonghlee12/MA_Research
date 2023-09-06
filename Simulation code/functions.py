import numpy as np
import sympy as sp
from sympy.stats import density, Normal, cdf
from scipy.optimize import root_scalar



# Reservation value
z = sp.symbols("z")


# The equation that defines the reservation value.
# Simplification of equation (4).
def f(z: float, cost: float, w: float, v_std: float) -> float:
    F = Normal("f", w, v_std)
    F1 = Normal("f1", 0, v_std)
    result = sp.N(z * cdf(F)(z) + v_std * density(F)(z) + w * (1 - cdf(F)(z)) - z - cost)
    return result

# Function that calculates the reservation value given the cost, observed factor,
# and the standard deviation of the unobserved factor distribution
# `a': a threshold parameter for the search area of the optimization
def calc_res_value(cost, w, v_var, a):
    v_std = np.sqrt(v_var)
    u0 = w
    bracket = (w - a * v_var, w + a * v_var)
    solution = root_scalar(f, args = (cost, w, v_std), x0=u0, bracket=bracket)
    return solution.root

# The main function that runs the simulation given the parameters of the treatment.
def choice(n, x_mean, x_var, v_var, cost, a):
    x_vals = np.random.normal(x_mean, np.sqrt(x_var), n)    
    opening_order = np.argsort(x_vals)[::-1]
    true_vals = x_vals + np.random.normal(0, np.sqrt(v_var), n)
    
    highest_true_val = 0
    highest_true_val_index = 0
    
    for i in range(len(opening_order)):
        index = opening_order[i]
        true_val = true_vals[index]
        
        if true_val > highest_true_val:
            highest_true_val = true_val
            highest_true_val_index = i + 1
        
        if i < n - 1:
            next_res_val = calc_res_value(cost, x_vals[opening_order[i + 1]], v_var, a)
            if highest_true_val > next_res_val:
                return highest_true_val_index, true_vals[opening_order[0]], true_vals[opening_order[n - 1]], max(true_vals), min(true_vals)
        else: return highest_true_val_index, true_vals[opening_order[0]], true_vals[opening_order[n - 1]], max(true_vals), min(true_vals)