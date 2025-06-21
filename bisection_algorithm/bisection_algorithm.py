
# 🔍 Bisection Method for Finding Roots
# Bu yöntem, türevin işaret değiştirdiği aralıkta kök arar. Temel mantığı aralığı sürekli ikiye bölerek köke yaklaşmaktır.

# 🎯 Hedef fonksiyon
def f(x):
    return (x - 1)**2 * (x - 2) * (x - 3)  # Çoklu kök içeren polinom

# 📈 Türev fonksiyonu (manuel türetilmiş)
def f1(x):
    return 2 * (x - 1) * (x - 2) * (x - 3) + (x - 1)**2 * ((x - 3) + (x - 2))

# 🔧 Başlangıç aralığı [xa, xb]
xa = 0.5
xb = 50
iterations = 0  # İterasyon sayacı

# 🔁 Bisection algoritması döngüsü
while True:
    # Eğer başlangıç aralığında türev işaret değiştiriyorsa kök var demektir
    if (f1(xa) * f1(xb)) < 0:
        # Ortadaki nokta (xk) hesaplanır
        xk = xa + (xb - xa) / 2
        iterations += 1

        # Anlık durumu yazdır
        print(f"i: {iterations}: xa = {xa:.4f}, xb = {xb:.4f}, xk = {xk:.4f}")

        # Durdurma koşulları: türev sıfıra çok yakınsa ya da aralık yeterince küçükse
        if f1(xk) == 0 or (xb - xa) < 1e-4:
            break
        else:
            # Kök hangi yarım aralıkta ise o yönde daraltma yapılır
            if f1(xa) * f1(xk) > 0:
                xa = xk
            else:
                xb = xk
    else:
        # Başlangıç aralığında işaret değişimi yoksa kök bulunmaz
        print('Kök yok!')
        break

# 🔚 Sonuçların çıktısı
print(f"Kök yaklaşık olarak: {xa:.4f}")
print(f"Toplam iterasyon sayısı: {iterations}")
