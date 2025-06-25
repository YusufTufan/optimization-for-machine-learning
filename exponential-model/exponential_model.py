"""
Exponential Model Fitting (No Validation)
Fits a model of the form y = a * exp(b * t) to the data using LM optimization.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from dataset5 import ti, yi


def exponential_io(t, x):
    return [x[0] * math.exp(x[1] * ti_) for ti_ in t]


def error(xk, t, y):
    yhat = exponential_io(t, xk)
    return np.array(y) - np.array(yhat)


def find_jacobian(t, x):
    n = len(t)
    J = np.zeros((n, 2))
    for i in range(n):
        exp_val = math.exp(x[1] * t[i])
        J[i, 0] = -exp_val
        J[i, 1] = -x[0] * t[i] * exp_val
    return J


# Training data (even-indexed)
train_idx = np.arange(0, len(ti), 2)
train_in = np.array(ti)[train_idx]
train_out = np.array(yi)[train_idx]

# Initial parameters
xk = np.random.rand(2) - 0.5
mu, mu_scale, mu_max = 1, 10, 1e99
max_iter = 500
eps1 = eps2 = eps3 = 1e-9
I = np.identity(2)

# History
k = 0
ftra_hist = []
iter_hist = []

ek = error(xk, train_in, train_out)
ftra = np.sum(ek ** 2)
ftra_hist.append(ftra)
iter_hist.append(k)

print(f"k: {k}, x1: {xk[0]:.6f}, x2: {xk[1]:.6f}, f: {ftra:.6f}")

while k < max_iter:
    ek = error(xk, train_in, train_out)
    Jk = find_jacobian(train_in, xk)
    gk = 2 * Jk.T @ ek
    Hk = 2 * Jk.T @ Jk + 1e-8 * I
    ftra = np.sum(ek ** 2)
    sk = 1

    while True:
        try:
            zk = -np.linalg.inv(Hk + mu * I) @ gk
        except np.linalg.LinAlgError:
            break

        x_new = xk + sk * zk
        fz = np.sum(error(x_new, train_in, train_out) ** 2)

        if fz < ftra:
            pk = zk
            mu /= mu_scale
            xk = xk + sk * pk
            k += 1
            print(f"k: {k}, x1: {xk[0]:.6f}, x2: {xk[1]:.6f}, f: {fz:.6f}")
            break
        else:
            mu *= mu_scale
            if mu > mu_max:
                break

    ftra_hist.append(ftra)
    iter_hist.append(k)

    if (np.abs(ftra - fz) < eps1 or
        np.linalg.norm(sk * pk) < eps2 or
        np.linalg.norm(gk) < eps3):
        break

# Final plot
T = np.arange(min(ti), max(ti), 0.1)
yhat = exponential_io(T, xk)
plt.scatter(ti, yi, color='darkred', marker='x')
plt.plot(T, yhat, color='green')
plt.xlabel('ti')
plt.ylabel('yi')
plt.title('Exponential Model Fit', fontstyle='italic')
plt.grid(True)
plt.legend(['Model', 'Data'])
plt.show()

print("Final parameters:", xk)
