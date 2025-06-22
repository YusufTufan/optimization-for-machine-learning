# 🌟 Golden Section Search Algorithm
# Bu yöntem, bir fonksiyonun minimum değerini bulmak için kullanılan sayısal bir optimizasyon tekniğidir.
# Fibonacci oranına dayalı olarak aralığı sürekli daraltarak çözüm arar.

import math

# 🎯 Hedef fonksiyon
def f(x):
    return (x - 1)**2 * (x - 2) * (x - 3)  # Çoklu kök içeren polinom

# 🔧 Başlangıç aralığı
xalt = 2      # Alt sınır
xust = 3      # Üst sınır

dx = 1e-7     # Hassasiyet (epsilon)
alpha = (1 + math.sqrt(5)) / 2   # Altın oran
tau = 1 - 1 / alpha              # Tamamlayıcı oran

# 🔢 Maksimum iterasyon sayısını hesapla (yakınsama tahmini)
epsilon = dx / (xust - xalt)
N = round(-2.078 * math.log(epsilon))

# Başlangıç noktalarının belirlenmesi
x1 = xalt + tau * (xust - xalt); f1 = f(x1)
x2 = xust - tau * (xust - xalt); f2 = f(x2)

# 🔁 Golden Section Döngüsü
for k in range(N):
    if f1 > f2:
        xalt = x1
        x1 = x2
        f1 = f2
        x2 = xust - tau * (xust - xalt)
        f2 = f(x2)
    else:
        xust = x2
        x2 = x1
        f2 = f1
        x1 = xalt + tau * (xust - xalt)
        f1 = f(x1)

    # İterasyon çıktısı
    print(f"{k+1:2d}: x1 = {x1:.4f}, x2 = {x2:.4f}, f1 = {f1:.4f}, f2 = {f2:.4f}")

# 🔚 Yaklaşık kökü hesapla (aralığın ortalaması)
x = 0.5 * (x1 + x2)
print(f"\nYaklaşık minimum nokta: x = {x:.4f}")
