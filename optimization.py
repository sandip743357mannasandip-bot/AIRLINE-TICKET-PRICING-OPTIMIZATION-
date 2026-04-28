import numpy as np
import matplotlib.pyplot as plt

# Define parameter
# These would come from our regression in practice
# Using representative values from the dataset
beta_0 = 8.5          # intercept from log-linear regression
beta_dot_X = 1.2      # β⊤X for a sample flight
alpha = 1 / 9087.06   # 1/mean_price as estimated earlier
C = 180               # seat capacity
# Compute A = exp(β₀ + β⊤X)
A = np.exp(beta_0 + beta_dot_X)
print(f"A = exp(β₀ + β⊤X) = {A:.4f}")
print(f"α = {alpha:.6f}")
print(f"True optimum 1/α = ₹{1/alpha:.2f}")
# calculate f, f', f''
def f(p):
    """Objective: expected revenue"""
    demand = A * np.exp(-alpha * p)
    return p * min(demand, C)

def f_prime(p):
    """First derivative of f(p) = p·A·e^(-αp)"""
    return A * np.exp(-alpha * p) * (1 - alpha * p)

def f_double_prime(p):
    """Second derivative of f(p)"""
    return alpha * A * np.exp(-alpha * p) * (alpha * p - 2)

# Newton's Method


def newtons_method(p_init, alpha, tol=1e-6, max_iter=100):
   
    p = p_init
    history = [p]
    
    print(f"\n{'Iter':<6} {'p':>12} {'f(p)':>14} {'f prime':>14} {'f double prime':>16}")
    print("-" * 65)
    
    for i in range(max_iter):
        fp  = f_prime(p)
        fpp = f_double_prime(p)
        
        print(f"{i:<6} {p:>12.4f} {f(p):>14.4f} {fp:>14.6f} {fpp:>16.6f}")
        
        # Check if already at optimum
        if abs(fp) < tol:
            print(f"\n Converged at iteration {i}")
            break
        
        # Safety check — avoid division by near-zero
        if abs(fpp) < 1e-12:
            print("  Second derivative near zero, stopping.")
            break
        
        # Newton update: simplified form (exponentials cancel)
        # p = p - f'(p)/f''(p)
        # = p - (1 - α·p) / (α·(α·p - 2))
        p_new = p - (1 - alpha * p) / (alpha * (alpha * p - 2))
        
        history.append(p_new)
        
        # Convergence check on step size too
        if abs(p_new - p) < tol:
            p = p_new
            print(f"\n Converged at iteration {i+1} (step size < tol)")
            break
        
        p = p_new
    
    return p, history

# Initial guess: start at mean price
p_init = 9087.06

p_star, history = newtons_method(p_init, alpha)

print(f"\n{'='*45}")
print(f"Newton's optimal price  : ₹{p_star:.2f}")
print(f"Analytical optimal (1/α): ₹{1/alpha:.2f}")
print(f"Revenue at p*           : ₹{f(p_star):.2f}")
print(f"Iterations taken        : {len(history)}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# ── Plot 1: Revenue curve ──
prices   = np.linspace(1000, 30000, 500)
revenues = [f(p) for p in prices]

