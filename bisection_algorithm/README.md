# Bisection Algorithm for Univariate Optimization

This repository contains a Python implementation of the **Bisection Method**, a simple yet effective numerical optimization algorithm. The method is used to find the minimum point of a **single-variable nonlinear function** by locating the root of its first derivative.

## 📌 Problem Definition

The goal is to minimize a univariate objective function by solving:

```math
f'(x) = 0
````

This approach transforms the optimization task into a root-finding problem.

## 🔍 Method Overview

The **Bisection Method** is a bracketing technique for finding a root of a continuous function. It requires an initial interval `[a, b]` such that `f'(a) * f'(b) < 0`, ensuring the existence of a root within the interval. In each iteration, the interval is halved, and the subinterval containing the root is selected.

**Advantages**:

* Simple to implement
* Guaranteed convergence
* No need for derivatives of higher order

**Disadvantages**:

* Slow convergence compared to other methods (e.g., Newton-Raphson)

## ⚙️ Algorithm Steps

1. Choose an initial interval `[a, b]` where `f'(a) * f'(b) < 0`
2. Compute midpoint `c = (a + b) / 2`
3. Evaluate `f'(c)`
4. Update the interval:

   * If `f'(a) * f'(c) < 0`, root is in `[a, c]`
   * Else, root is in `[c, b]`
5. Repeat until convergence (i.e., until the interval width is sufficiently small)

# Tek Değişkenli Optimizasyon için Bisection (İkiye Bölme) Algoritması

Bu repoda, **Bisection (İkiye Bölme) Yöntemi** ile yazılmış bir Python uygulaması bulunmaktadır. Bu yöntem, **tek değişkenli doğrusal olmayan bir fonksiyonun** türevini sıfırlayarak minimum noktasını bulmak için kullanılır.

## 📌 Problem Tanımı

Amaç fonksiyonu şu şekilde optimize edilir:

```math
f'(x) = 0
```

Bu yaklaşım, optimizasyon problemini bir kök bulma problemine dönüştürür.

## 🔍 Yöntem Özeti

**İkiye Bölme Yöntemi**, sürekli bir fonksiyonun kökünü bulmak için kullanılan bir braketleme tekniğidir. `f'(a) * f'(b) < 0` koşulunu sağlayan bir `[a, b]` aralığı ile başlanır. Bu koşul, aralık içinde bir kök olduğunu garanti eder. Her iterasyonda aralık ikiye bölünür ve kökün bulunduğu alt aralık seçilir.

**Avantajları**:

* Uygulaması kolaydır
* Yakınsamayı garanti eder
* Yüksek dereceden türevlere ihtiyaç duymaz

**Dezavantajları**:

* Diğer yöntemlere kıyasla (örn. Newton-Raphson) yavaş yakınsar

## ⚙️ Algoritma Adımları

1. `f'(a) * f'(b) < 0` koşulunu sağlayan `[a, b]` aralığı seçilir
2. Ortanca nokta `c = (a + b) / 2` hesaplanır
3. `f'(c)` değeri hesaplanır
4. Aralık güncellenir:

   * Eğer `f'(a) * f'(c) < 0` ise kök `[a, c]` içindedir
   * Aksi halde kök `[c, b]` içindedir
5. Aralık yeterince küçülene kadar işlem tekrarlanır


## 🧾 Gereksinimler

* Python 3.x
* NumPy (opsiyonel)

## 👨‍💻 Geliştirici

[Yusuf Tufan](https://github.com/YusufTufan)

```

