"""
Polinom Regresyon Analizi
-------------------------
Bu program, verilen veri noktalarına en iyi uyan polinom modelini bulmayı amaçlar.
Farklı derece polinomları deneyerek en iyi modeli seçer.

Kullanılan yöntemler:
1. En Küçük Kareler Yöntemi (Least Squares)
2. K-fold benzeri validation (basit çapraz doğrulama)
3. Model karşılaştırma ve seçimi
"""

import numpy as np
import matplotlib.pyplot as plt
from dataset2 import ti, yi  # Zaman ve çıktı verileri


def polinomIO(t, x):
    """
    Verilen polinom katsayıları ile tahmini y değerlerini hesaplar.
    """
    yhat = []
    for ti_ in t:
        toplam = 0
        for i in range(len(x)):
            toplam += x[i] * (ti_ ** i)
        yhat.append(toplam)
    return yhat


def findx(ti, yi, derece):
    """
    En küçük kareler yöntemi ile polinom katsayılarını bulur.
    """
    n = len(ti)
    J = -np.ones((n, 1))
    for d in range(1, derece + 1):
        J = np.hstack((J, -np.ones((n, 1)) * np.array(ti).reshape(n, 1) ** d))

    A = np.linalg.inv(J.T @ J)
    B = J.T @ yi
    x = -A @ B
    return x


def plotresult(ti, yi, x, fval):
    """
    Gerçek verilerle polinom modelini aynı grafikte çizer.
    """
    T = np.arange(min(ti), max(ti), 0.1)
    yhat = polinomIO(T, x)

    plt.figure(figsize=(10, 6))
    plt.scatter(ti, yi, color="darkred", marker='x')
    plt.plot(T, yhat, color="green", linewidth=1)
    plt.xlabel("ti")
    plt.ylabel("yi")
    plt.title(f"{len(x)-1} dereceden polinom modeli | FV: {fval:.2f}",
              fontstyle="italic")
    plt.legend(["Polinom Modeli", "Gerçek Veri"])
    plt.grid(True, alpha=0.3)
    plt.show()


# Veri bölümü: Çift indeksler eğitim, tek indeksler doğrulama
train_idx = np.arange(0, len(ti), 2)
train_in = np.array(ti)[train_idx]
train_out = np.array(yi)[train_idx]

val_idx = np.arange(1, len(ti), 2)
val_in = np.array(ti)[val_idx]
val_out = np.array(yi)[val_idx]

# Her derece için model kur, değerlendir, görselleştir
PD = []
FV = []

for derece in range(1, 10):
    x = findx(train_in, train_out, derece)
    yhat = polinomIO(val_in, x)
    e = np.array(val_out) - np.array(yhat)
    fval = np.sum(e ** 2)

    PD.append(derece)
    FV.append(fval)

    print(f"Polinom Derecesi: {derece}, FV: {fval:.4f}")
    plotresult(ti, yi, x, fval)


# Son performans grafikleri
plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.bar(PD, FV, color='darkred')
plt.xlabel('Polinom derecesi')
plt.ylabel('Validation performansı')
plt.title('Polinom modeli (Normal ölçek)', fontstyle='italic')
plt.grid(color='green', linestyle='--', linewidth=0.1, alpha=0.3)

plt.subplot(122)
plt.bar(PD, FV, color='darkred')
plt.yscale('log')
plt.xlabel('Polinom derecesi')
plt.ylabel('Validation performansı (log ölçek)')
plt.title('Polinom modeli (Logaritmik ölçek)', fontstyle='italic')
plt.grid(color='green', linestyle='--', linewidth=0.1, alpha=0.3)

plt.tight_layout()
plt.show()
