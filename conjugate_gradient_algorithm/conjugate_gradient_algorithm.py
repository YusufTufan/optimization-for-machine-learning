
# 🔁 Conjugate Gradient Method for Multivariable Optimization
# Bu algoritma, özellikle büyük boyutlu problemlerde etkin çözüm sağlayan bir optimizasyon tekniğidir.
# İlerleyişi, negatif gradyan yönüne dayalı olarak yönelmiş ardışık adımlarla gerçekleştirilir.

import numpy as np
import matplotlib.pyplot as plt

# 🎯 Hedef fonksiyon
def f(x): 
    return 3 + (x[0] - 1.5*x[1])**2 + (x[1] - 2)**2

# 📈 Gradyan (1. türev)
def gradF(x):
    return np.array([2 * (x[0] - 1.5 * x[1]), -3 * (x[0] - 1.5 * x[1]) + 2 * (x[1] - 2)])

# 🌐 Kontur grafiği için yüzey oluştur
x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)
X1, X2 = np.meshgrid(x1, x2)
Z = f([X1, X2])

plt.figure(figsize=(10, 8))
contour = plt.contour(X1, X2, Z, levels=20)
plt.clabel(contour, inline=True, fontsize=8)
plt.xlabel('x₁')
plt.ylabel('x₂')
plt.title('Conjugate Gradient Algorithm Progress')
plt.grid(True)

# 🔧 Başlangıç parametreleri
x = np.array([-4.5, -3.5])
x_points = [x.copy()]
gradf = gradF(x)
gradf_prev = None
pk = -gradf
k = 0
eps1 = eps2 = eps3 = 1e-10
Nmax = 1000

# 🔁 Conjugate Gradient Döngüsü
while k < Nmax:
    if k != 0:
        # Beta (Fletcher-Reeves yöntemi)
        Beta = np.dot(gradf, gradf) / np.dot(gradf_prev, gradf_prev)
        pk = -gradf + Beta * pk

    x_prev = x.copy()
    f_prev = f(x_prev)
    gradf_prev = gradf.copy()

    sk = 0.01  # Sabit adım boyu (optimize edilebilir)
    x = x + sk * pk
    x_points.append(x.copy())

    gradf = gradF(x)

    # ✔️ Sonlandırma kriterleri
    deltaF = abs(f(x) - f_prev)
    deltaX = np.linalg.norm(x - x_prev)
    grad_norm = np.linalg.norm(gradf)

    print(f"İterasyon {k}: x = [{x[0]:.4f}, {x[1]:.4f}], f(x) = {f(x):.4f}, ||∇f|| = {grad_norm:.4e}, Δf = {deltaF:.4e}, Δx = {deltaX:.4e}")

    if deltaF < eps1 and deltaX < eps2 and grad_norm < eps3:
        print("\nSonlandırma kriterleri sağlandı!")
        break

    k += 1

# 📊 Sonuçları grafiğe dök
x_points = np.array(x_points)
plt.plot(x_points[:, 0], x_points[:, 1], 'r.-', label='İlerleyiş', markersize=2)
plt.plot(x_points[0, 0], x_points[0, 1], 'go', label='Başlangıç')
plt.plot(3, 2, 'r*', markersize=15, label='Minimum (3,2)')
plt.legend()
plt.show()

# 📢 Sonuç çıktısı
print("\nSonuç:")
print(f"Son nokta: [{x[0]:.4f}, {x[1]:.4f}]")
print(f"Minimum değer: {f(x):.4f}")
print(f"İterasyon sayısı: {k}")
