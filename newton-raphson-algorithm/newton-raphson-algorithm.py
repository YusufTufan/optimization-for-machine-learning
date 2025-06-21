# Newton-Raphson Yöntemi ile Sayısal Kök Bulma
# Bu algoritma, türevleri bilinen bir fonksiyonun köklerini iteratif olarak bulur.
# Burada hem birinci hem de ikinci türevler kullanılarak gelişmiş bir versiyonu uygulanmaktadır.

# 📌 Kökü bulunacak fonksiyon:
def f(x):
    return (x - 1)**2 * (x - 2) * (x - 3)  # Çoklu köke sahip polinomsal bir fonksiyon

# 📈 Birinci türev (manuel olarak alınmış):
def f1(x):
    # Zincir ve çarpım kuralları kullanılarak alınmıştır
    return 2 * (x - 1) * (x - 2) * (x - 3) + (x - 1)**2 * ((x - 3) + (x - 2))

# 📉 İkinci türev (manuel olarak alınmış):
def f2(x):
    # Fonksiyonun eğimindeki değişimi gösterir
    return 2 * ((x - 2)*(x - 3) + (x - 1)*(x - 3) + (x - 1)*(x - 2)) + 4*(x - 1)

# 🔁 Newton-Raphson Algoritması
def newton_raphson(x0, tol=1e-10, max_iter=100):
    """
    x0:        Başlangıç değeri
    tol:       Hata toleransı (yakınsama kriteri)
    max_iter:  Maksimum iterasyon sayısı
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        f1x = f1(x)
        f2x = f2(x)

        # Eğer türev çok küçükse (yaklaşık sıfır), işlem durdurulur
        if abs(f1x) < tol:
            print("Türevin sıfıra çok yakın olduğu nokta bulundu.")
            break

        # Newton-Raphson güncellemesi: x = x - f'(x)/f''(x)
        dx = -f1x / f2x
        x += dx

        # Her iterasyonda güncel değerleri yazdır
        print(f"{i+1}. iterasyon | x = {x:.4f}, f(x) = {fx:.4f}, f'(x) = {f1x:.4f}, f''(x) = {f2x:.4f}, Δx = {dx:.4f}")

        # Δx toleransın altına düştüyse yakınsama sağlanmıştır
        if abs(dx) < tol:
            break

    return x  # Yaklaşık kök değeri döndürülür

# ▶️ Çalıştırma örneği
if __name__ == "__main__":
    x0 = 3.5  # İlk tahmin (başlangıç noktası)
    root = newton_raphson(x0)
    print(f"\nYaklaşık kök: {root:.10f}")
