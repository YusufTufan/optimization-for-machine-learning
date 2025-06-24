# 🧠 Davidon-Fletcher-Powell (DFP) Algorithm
# Bu algoritma, ikinci türev matrisini (Hessian) doğrudan kullanmadan,
# bu matrisi yaklaşık olarak güncelleyerek bir fonksiyonun minimumunu bulur.

import numpy as np
import matplotlib.pyplot as plt
import math

# 🎯 Amaç fonksiyonu
def f(x): 
    return 3 + (x[0] - 1.5 * x[1])**2 + (x[1] - 2)**2

# 📈 Gradyan fonksiyonu (manuel türevlenmiş hali)
def gradf(x):
    return np.array([
        2 * (x[0] - 1.5 * x[1]),
        -3 * (x[0] - 1.5 * x[1]) + 2 * (x[1] - 2)
    ])

# 🟡 Golden Section Line Search: En uygun adım boyunu bulmak için
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

    return 0.5 * (x1 + x2)

# 🔧 Başlangıç ayarları
x = np.array([-5.4, 1.7])  # Başlangıç noktası
H = np.eye(2)              # Başlangıçta birim matris (Hessian approx.)
x1, x2 = [x[0]], [x[1]]    # Görselleştirme için adım kaydı

Nmax = 10000
eps1 = 1e-9
eps2 = 1e-9
eps3 = 1e-9
k = 0

# 🔁 DFP İterasyon döngüsü
while True:
    k += 1
    g = gradf(x)
    pk = -H @ g               # Yeni yön: negatif gradyan ile H'nin çarpımı
    sk = GSmain(f, x, pk)     # Optimal adım uzunluğu
    d = sk * pk               # Hareket vektörü
    x_new = x + d             # Yeni nokta

    g_new = gradf(x_new)
    delta_g = g_new - g

    # 📐 DFP Güncelleme formülü
    d = d.reshape(-1, 1)
    delta_g = delta_g.reshape(-1, 1)
    Hd = H @ delta_g

    term1 = (d @ d.T) / (d.T @ delta_g)
    term2 = (Hd @ Hd.T) / (delta_g.T @ Hd)
    H = H + term1 - term2

    # 🎯 Durdurma kriterleri
    if k >= Nmax:
        print("🚫 Maksimum iterasyon sayısına ulaşıldı.")
        break
    if abs(f(x_new) - f(x)) < eps1:
        print("📉 Fonksiyon değeri sabitlendi.")
        break
    if np.linalg.norm(x_new - x) < eps2:
        print("📍 Değişkenlerde değişiklik yok.")
        break
    if np.linalg.norm(g_new) < eps3:
        print("✅ Gradyan sıfıra çok yakın.")
        break

    # Güncelleme
    x = x_new
    x1.append(x[0])
    x2.append(x[1])

    print(f"k={k:2d}, x={x}, f(x)={f(x):.6f}, ||∇f||={np.linalg.norm(g_new):.3e}")

# 📊 Sonuçların grafiği
plt.plot(x1, x2, label='DFP Yolu')
plt.scatter(x1, x2, s=5, c='red', label='Adımlar')
plt.xlabel("x₁")
plt.ylabel("x₂")
plt.legend()
plt.title("Davidon-Fletcher-Powell Optimizasyon Yolu")
plt.grid(True)
plt.show()
