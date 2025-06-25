"""
Radial Basis Function (RBF) Network Regression
Fits a nonlinear model to data using Gaussian RBFs with varying number of centers.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from dataset3 import ti, yi


def gaussian_function(t, c, sigma):
    return math.exp(-(t - c) ** 2 / (sigma ** 2))


def rbf_io(t, x, c, sigma):
    yhat = []
    for ti_ in t:
        toplam = 0
        for i in range(len(x)):
            toplam += x[i] * gaussian_function(ti_, c[i], sigma[i])
        yhat.append(toplam)
    return yhat


def find_xcs(ti, yi, rbf_count):
    segment_len = (max(ti) - min(ti)) / rbf_count
    sigma = [segment_len] * rbf_count
    centers = [min(ti) + segment_len / 2 + i * segment_len for i in range(rbf_count)]

    n = len(ti)
    J = np.zeros((n, rbf_count))
    for i in range(n):
        for j in range(rbf_count):
            J[i, j] = -gaussian_function(ti[i], centers[j], sigma[j])

    A = np.linalg.inv(J.T @ J)
    B = J.T @ yi
    x = -A @ B
    return x, centers, sigma


def plot_result(ti, yi, x, c, s, fval):
    T = np.arange(min(ti), max(ti), 0.1)
    yhat = rbf_io(T, x, c, s)
    plt.scatter(ti, yi, label='Training Data', color='blue', marker='x')
    plt.plot(T, yhat, label='RBF Model', color='red')
    plt.xlabel('ti')
    plt.ylabel('yi')
    plt.title(f'{len(x)}-Düğümlü RBF Modeli | FV: {fval:.4f}', fontstyle='italic')
    plt.grid(True)
    plt.legend()
    plt.show()


# Veri bölme
train_idx = np.arange(0, len(ti), 2)
train_in = np.array(ti)[train_idx]
train_out = np.array(yi)[train_idx]
val_idx = np.arange(1, len(ti), 2)
val_in = np.array(ti)[val_idx]
val_out = np.array(yi)[val_idx]

# Farklı RBF sayılarıyla model eğitimi
RBF_list = []
FV_list = []

for rbf_count in range(1, 10):
    x, c, s = find_xcs(train_in, train_out, rbf_count)
    yhat = rbf_io(val_in, x, c, s)
    e = np.array(val_out) - np.array(yhat)
    fval = np.sum(e ** 2)

    RBF_list.append(rbf_count)
    FV_list.append(fval)

    print(f"RBF Sayısı: {rbf_count}, Doğrulama Hatası: {fval:.4f}")
    plot_result(ti, yi, x, c, s, fval)

# Performans grafiği
plt.bar(RBF_list, FV_list, color='darkred')
plt.xlabel('RBF Sayısı')
plt.ylabel('Doğrulama Hatası')
plt.title('RBF Modeli - Doğrulama Performansı', fontstyle='italic')
plt.grid(True)
plt.show()
