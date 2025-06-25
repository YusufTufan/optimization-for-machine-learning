"""
Hyperbolic Model Optimization (Fixed Node Count)
This script fits a hyperbolic model to a given dataset using a fixed node count (S).
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


# Split dataset into training and validation
train_idx = np.arange(0, len(ti), 2)
train_in = np.array(ti)[train_idx]
train_out = np.array(yi)[train_idx]

val_idx = np.arange(1, len(ti), 2)
val_in = np.array(ti)[val_idx]
val_out = np.array(yi)[val_idx]

# Optimization Parameters
S = 15
xk = np.random.rand(3 * S + 1) - 0.5
mu, mu_scale, mu_max = 1, 10, 1e99
max_iter = 1000
eps1 = eps2 = eps3 = 1e-9
I = np.identity(3 * S + 1)

# Initial Evaluation
k = 0
best_fval = 1e99
ftra_hist, fval_hist, iter_hist = [], [], []
ek = error(xk, train_in, train_out)
ftra = np.sum(ek ** 2)
eval_ = error(xk, val_in, val_out)
fval = np.sum(eval_ ** 2)
ftra_hist.append(ftra)
fval_hist.append(fval)
iter_hist.append(k)

print(f"k: {k}, x1: {xk[0]:.6f}, x2: {xk[1]:.6f}, f: {ftra:.6f}")

# Optimization Loop
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
            xk = x_new
            mu /= mu_scale
            k += 1
            print(f"k: {k}, x1: {xk[0]:.6f}, x2: {xk[1]:.6f}, f: {fz:.6f}")
            break
        else:
            mu *= mu_scale
            if mu > mu_max:
                break

    eval_ = error(xk, val_in, val_out)
    fval = np.sum(eval_ ** 2)

    if fval < best_fval:
        best_fval = fval
        x_best = xk.copy()
        k_best = k

    ftra_hist.append(ftra)
    fval_hist.append(fval)
    iter_hist.append(k)

    if (np.abs(ftra - fz) < eps1 or
        np.linalg.norm(sk * zk) < eps2 or
        np.linalg.norm(gk) < eps3):
        break

# Plot prediction
T = np.arange(min(ti), max(ti), 0.1)
yhat = hyperbolic_io(T, x_best)
plt.scatter(ti, yi, color='darkred', marker='x')
plt.plot(T, yhat, color='green')
plt.xlabel('ti')
plt.ylabel('yi')
plt.title(f'Hiperbolik Model | FV: {best_fval:.4f}')
plt.grid(True)
plt.legend(['Hiperbolik Model', 'Ger\u00e7ek Veri'])
plt.show()

# Plot performance
plt.plot(iter_hist, ftra_hist, color='green')
plt.plot(iter_hist, fval_hist, color='red')
plt.axvline(x=k_best, color='blue', linestyle='dashed')
plt.xlabel('Iterasyon')
plt.ylabel('Performanslar')
plt.title('Egitim vs Dogrulama Hatalari')
plt.grid(True)
plt.legend(['Training', 'Validation'])
plt.show()
