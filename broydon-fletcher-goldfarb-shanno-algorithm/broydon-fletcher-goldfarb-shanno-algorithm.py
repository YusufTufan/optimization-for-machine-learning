"""
BFGS (Braydon Fletcher Goldfarb Shanno) Algoritması

- Quasi-Newton yöntemidir.
- Doğrusal olmayan fonksiyonların minimizasyonunda kullanılır.
- Hessian matrisinin tersini yaklaşık olarak günceller.
"""

import numpy as np
import math
import matplotlib.pyplot as plt


def f(x):
    """Amaç fonksiyon"""
    return 3 + (x[0] - 1.5 * x[1])**2 + (x[1] - 2)**2


def gradf(x):
    """Amaç fonksiyonun gradyanı (türev vektörü)"""
    return np.array([
        2 * (x[0] - 1.5 * x[1]),
        -3 * (x[0] - 1.5 * x[1]) + 2 * (x[1] - 2)
    ])


def golden_section_search(f, xk, pk, dx=1e-5):
    """
    Altın oran yöntemi ile optimum adım büyüklüğünü bulur.
    """
    xbottom = 0
    xtop = 1
    alpha = (1 + math.sqrt(5)) / 2
    tau = 1 - 1 / alpha
    epsilon = dx / (xtop - xbottom)
    n_iter = round(-2.078 * math.log(epsilon))

    x1 = xbottom + tau * (xtop - xbottom)
    f1 = f(xk + x1 * pk)

    x2 = xtop - tau * (xtop - xbottom)
    f2 = f(xk + x2 * pk)

    for _ in range(n_iter):
        if f1 > f2:
            xbottom = x1
            x1 = x2
            f1 = f2
            x2 = xtop - tau * (xtop - xbottom)
            f2 = f(xk + x2 * pk)
        else:
            xtop = x2
            x2 = x1
            f2 = f1
            x1 = xbottom + tau * (xtop - xbottom)
            f1 = f(xk + x1 * pk)

    return 0.5 * (x1 + x2)


def bfgs():
    """BFGS algoritmasının ana fonksiyonu"""
    x = np.array([-5.4, 1.7])
    n_max = 10000

    eps1 = 1e-10
    eps2 = 1e-10
    eps3 = 1e-10

    k = 0
    identity = np.identity(2)
    M = np.identity(2)
    updated_x = np.array([1e10, 1e10])

    x1_list = [x[0]]
    x2_list = [x[1]]

    while True:
        # Sonlandırma kriterlerini kontrol et
        c1 = k > n_max
        c2 = abs(f(updated_x) - f(x)) < eps1
        c3 = np.linalg.norm(updated_x - x) < eps2
        c4 = np.linalg.norm(gradf(updated_x)) < eps3

        if c1 or c2 or c3 or c4:
            break

        k += 1

        eigvals, _ = np.linalg.eigh(M)

        if np.min(eigvals) > 0:
            pk = -np.dot(np.linalg.inv(M), gradf(x))
        else:
            mu = abs(np.min(eigvals)) + 0.001
            pk = -np.dot(np.linalg.inv(M + mu * identity), gradf(x))

        sk = golden_section_search(f, x, pk)
        prev_grad = gradf(x).reshape(-1, 1)

        x = x + sk * pk
        x = np.array(x)

        current_grad = gradf(x).reshape(-1, 1)
        y = current_grad - prev_grad
        pk = pk.reshape(-1, 1)
        dx = sk * pk

        A = np.dot(y, y.T) / np.dot(y.T, dx)
        B = np.dot(np.dot(M, dx), np.dot(dx.T, M)) / np.dot(dx.T, np.dot(M, dx))
        M = M + A - B

        print(
        f"İterasyon: {k}, Adım: {sk:.6f}, x: {np.round(x, 4)},f(x): {np.round(f(x), 4)}"
        )


        updated_x = x.copy()
        x1_list.append(x[0])
        x2_list.append(x[1])

    if c1:
        print("Maksimum iterasyon sayısına ulaşıldı.")
    if c2:
        print("Fonksiyon değeri değişmiyor.")
    if c3:
        print("x değişmiyor.")
    if c4:
        print("Gradyan sıfıra yaklaştı (durağan nokta).")

    # Çizim
    plt.figure(figsize=(8, 6))
    plt.plot(x1_list, x2_list, marker='o', linestyle='-', markersize=3)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('İterasyon Geçmişi')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    bfgs()
