"""
Hyperbolic Model Grid Search (Varying Node Count)
This script searches for the best S (node count) to minimize validation error.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from dataset6 import ti, yi


def tanh(x):
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))


def hyperbolic_io(t, x):
    S = int((len(x) - 1) / 3)
    yhat = []
    for ti_ in t:
        toplam = x[3 * S]
        for j in range(S):
            toplam += x[2 * S + j] * tanh(x[j] * ti_ + x[S + j])
        yhat.append(toplam)
    return yhat


def error(xk, t, y):
    yhat = hyperbolic_io(t, xk)
    return np.array(y) - np.array(yhat)


def find_jacobian(t, x):
    S = int((len(x) - 1) / 3)
    n = len(t)
    J = np.zeros((n, 3 * S + 1))
    for i in range(n):
        for j in range(S):
            tanh_val = tanh(x[j] * t[i] + x[S + j])
            sech_sq = 1 - tanh_val ** 2
            J[i, j] = -x[j + 2 * S] * t[i] * sech_sq
            J[i, S + j] = -x[j + 2 * S] * sech_sq
            J[i, 2 * S + j] = -tanh_val
        J[i, 3 * S] = -1
    return J


def plot_result(ti, yi, x_best, fval, S):
    T = np.arange(min(ti), max(ti), 0.1)
    yhat = hyperbolic_io(T, x_best)
    plt.scatter(ti, yi, color='darkred', marker='x')
    plt.plot(T, yhat, color='green')
    plt.xlabel('ti')
    plt.ylabel('yi')
    plt.title(f'{S}-Node Model | FV: {fval:.4f}', fontstyle='italic')
    plt.grid(True)
    plt.legend(['Model', 'Ger\u00e7ek Veri'])
    plt.show()


# Dataset split
train_idx = np.arange(0, len(ti), 2)
train_in = np.array(ti)[train_idx]
train_out = np.array(yi)[train_idx]
val_idx = np.arange(1, len(ti), 2)
val_in = np.array(ti)[val_idx]
val_out = np.array(yi)[val_idx]

# Parameters
max_iter = 1000
epsilon1 = epsilon2 = epsilon3 = 1e-9
mu_max = 1e99
NODEmax = int((len(train_in) - 1) / 3)

NODE = []
FV = []
global_best = 1e10
S_best = 0

# Sweep over node counts
for S in range(2, NODEmax):
    xk = np.random.rand(3 * S + 1) - 0.5
    mu = 1
    mu_scale = 10
    I = np.identity(3 * S + 1)
    k = 0
    best_fval = 1e99
    converged = True

    while k < max_iter and converged:
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
                converged = False
                break

            x_new = xk + sk * zk
            fz = np.sum(error(x_new, train_in, train_out) ** 2)
            if fz < ftra:
                pk = zk
                mu /= mu_scale
                k += 1
                xk = xk + sk * pk
                break
            else:
                mu *= mu_scale
                if mu > mu_max:
                    converged = False
                    break

        fval = np.sum(error(xk, val_in, val_out) ** 2)
        if fval < best_fval:
            best_fval = fval
            x_best = xk.copy()

    plot_result(ti, yi, x_best, best_fval, S)
    NODE.append(S)
    FV.append(best_fval)

    if best_fval < global_best:
        global_best = best_fval
        S_best = S

    print(f"S = {S}, FV = {best_fval:.4f}, Global Best = {global_best:.4f}")

# Plot all performances
plt.bar(NODE, FV, color='orange', width=0.4)
plt.bar(S_best, global_best, color='blue', width=0.4)
plt.xlabel('Node (S)')
plt.ylabel('Validation Error')
plt.title('Validation Error vs Node Count')
plt.grid(True)
plt.show()

print("Best Node Count:", S_best)
