
# 📉 Gradient Descent Algorithm for Multivariable Optimization
# Bu algoritma, çok değişkenli bir fonksiyonun minimumunu bulmak için yalnızca gradyanı kullanarak iteratif olarak çözüm üretir.

import numpy as np
import matplotlib.pyplot as plt

# 🎯 Amaç fonksiyonu
def f(x): 
    return 3 + (x[0] - 1.5*x[1])**2 + (x[1] - 2)**2  # Paraboloid yapılı fonksiyon

# 📈 Gradyan (1. türev vektörü)
def gradF(x):
    # Manuel türevlenmiş hali
    return np.array([2 * (x[0] - 1.5 * x[1]), -3 * (x[0] - 1.5 * x[1]) + 2 * (x[1] - 2)])

# 📉 Hessian (2. türev matrisi) - Yalnızca analiz için
def hessianF(x):
    return np.array([[2, 0], [0, 2]])

# 🚩 Başlangıç noktası
x = np.array([4, 3])
i = 0
trajectory = [x.copy()]  # Adımların kaydı

print(f"i: {i}, f(x): {f(x):.5f}")

# 🔁 Gradient Descent Döngüsü
while True:
    i += 1
    x = x - 0.2 * gradF(x)  # Öğrenme oranı = 0.2
    trajectory.append(x.copy())  # Adımı kaydet

    normGradf = np.linalg.norm(gradF(x))  # Gradyan normu hesapla

    print(f"i: {i}, f(x): {f(x):.5f}, ||gradF(x)||: {normGradf:.8f}")

    if normGradf < 1e-8:  # Yakınsama kriteri
        break

# 🎯 Bulunan minimum noktayı yazdır
print(f"x* = {x}")

# 🧠 NOT: Hessian matrisi Gradient Descent yönteminde kullanılmaz.
# Ancak burada, elde edilen sonucun minimum olup olmadığını doğrulamak için kullanılmıştır.

H = hessianF(x)
ozdeger, _ = np.linalg.eig(H)

if min(ozdeger) > 0:
    print("x* noktası minimum")
elif max(ozdeger) < 0:
    print("x* noktası maksimum")
else:
    print("x* noktası semer noktası")

# 📊 Optimizasyon Yolunu Görselleştir
trajectory = np.array(trajectory)

plt.figure(figsize=(8, 6))
plt.plot(trajectory[:, 0], trajectory[:, 1], 'r.-', label="Gradient Descent Yolu")
plt.scatter(trajectory[:, 0], trajectory[:, 1], s=30, c='blue', label="Adımlar")
plt.scatter(trajectory[0, 0], trajectory[0, 1], s=100, c='red', label="Başlangıç")
plt.scatter(x[0], x[1], s=100, c='green', label="Minimum")

plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.title("Gradient Descent Optimizasyon Yolu")
plt.grid(True)
plt.show()
