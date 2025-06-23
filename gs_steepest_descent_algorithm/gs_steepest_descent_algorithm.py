# 📉 Steepest Descent Method with Golden Section Line Search
# Bu algoritma, bir fonksiyonun minimum noktasını gradyan yönünde inişle bulur.
# Optimal adım boyu Altın Oran (Golden Section Search) yöntemi ile belirlenir.

import numpy as np
import math
import matplotlib.pyplot as plt

# 🎯 Amaç fonksiyonu
def f(x): 
    return 3 + (x[0] - 1.5*x[1])**2 + (x[1] - 2)**2

# 📈 Gradyan fonksiyonu
def gradF(x):
    return np.array([
        2 * (x[0] - 1.5 * x[1]),
        -3 * (x[0] - 1.5 * x[1]) + 2 * (x[1] - 2)
    ])

# 🟡 Golden Section Search ile optimal adım boyu seçimi
def GSmain(f, xk, pk):
    xalt, xust = 0, 1
    dx = 1e-5
    alpha = (1 + math.sqrt(5)) / 2
    tau = 1 - 1 / alpha
    epsilon = dx / (xust - xalt)
    N = round(-2.078 * math.log(epsilon))

    x1 = xalt + tau * (xust - xalt)
    x2 = xust - tau * (xust - xalt)
    f1 = f(xk + x1 * pk)
    f2 = f(xk + x2 * pk)

    for _ in range(N):
        if f1 > f2:
            xalt = x1
            x1 = x2
            f1 = f2
            x2 = xust - tau * (xust - xalt)
            f2 = f(xk + x2 * pk)
        else:
            xust = x2
            x2 = x1
            f2 = f1
            x1 = xalt + tau * (xust - xalt)
            f1 = f(xk + x1 * pk)

    return 0.5 * (x1 + x2)  # En uygun adım uzunluğu

# 🔧 Başlangıç ayarları
x = np.array([-5.4, 1.7])
x1, x2 = [x[0]], [x[1]]
Nmax = 10000
eps1 = 1e-10
eps2 = 1e-10
eps3 = 1e-10
k = 0
updatedx = np.array([1e10, 1e10])

# 🔁 Optimizasyon Döngüsü
while True:
    k += 1
    pk = -gradF(x)              # Gradyan yönünde iniş
    sk = GSmain(f, x, pk)       # Altın oran ile adım boyu belirleme
    x = x + sk * pk             # Yeni nokta

    # Kriter kontrolleri
    stop1 = k >= Nmax
    stop2 = abs(f(updatedx) - f(x)) < eps1
    stop3 = np.linalg.norm(updatedx - x) < eps2
    stop4 = np.linalg.norm(gradF(updatedx)) < eps3

    print(f"k: {k}, sk: {sk:.4f}, x: {x}, f(x): {f(x):.6f}, ||∇f||: {np.linalg.norm(gradF(x)):.6f}")

    if stop1 or stop2 or stop3 or stop4:
        break

    updatedx = x.copy()
    x1.append(x[0])
    x2.append(x[1])

# 📌 Durdurma sebebi bildirimi
if stop1:
    print("🚫 Maksimum iterasyon sayısına ulaşıldı.")
if stop2:
    print("📉 Fonksiyon değeri değişmiyor.")
if stop3:
    print("📍 Değişkenlerde anlamlı değişim yok.")
if stop4:
    print("✅ Durağan noktaya ulaşıldı.")

# 📊 Optimizasyon Yolu Grafiği
plt.plot(x1, x2, label="İterasyon Yolu")
plt.scatter(x1, x2, s=5, c='red', label="Adımlar")
plt.xlabel("x₁")
plt.ylabel("x₂")
plt.legend()
plt.title("Gradient Descent + Golden Section")
plt.grid(True)
plt.show()
