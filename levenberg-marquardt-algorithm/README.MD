# Levenberg–Marquardt Algorithm for Nonlinear Least Squares Optimization

This repository provides an implementation of the **Levenberg–Marquardt (LM)** algorithm, a widely used optimization technique for solving nonlinear least squares problems.

## 📌 Problem Definition

The goal is to minimize the sum of squared residuals between a nonlinear model `f(x, t)` and observed data `y(t)`:

```math
\min_{x} \sum_{i=1}^{N} \left(y_i - f(x, t_i)\right)^2
````

Here, `x` is the vector of model parameters, and `f(x, t)` is the nonlinear function being fitted.

## 🔍 Method Overview

The **Levenberg–Marquardt Algorithm** combines the advantages of:

* **Gradient Descent**: robust but slow
* **Gauss–Newton**: fast near the solution but unstable if far

LM dynamically balances between these two depending on the current error, via a damping factor `λ`.

### Key Characteristics:

* Used in nonlinear curve fitting and machine learning
* Adaptive update using Jacobian matrix `J`
* Well-suited for overdetermined systems (more equations than unknowns)

### Update Rule:

```math
x_{k+1} = x_k + \left(J^T J + \lambda I\right)^{-1} J^T r
```

Where:

* `J` is the Jacobian matrix of partial derivatives
* `r` is the residual vector: `r = y - f(x)`
* `λ` controls the blend between gradient descent and Gauss–Newton

## ⚙️ Algorithm Steps

1. Initialize parameter vector `x₀`, damping factor `λ`, and tolerance
2. While stopping criteria not met:

   * Compute residuals `r = y - f(x)`
   * Compute Jacobian matrix `J`
   * Update `x` using LM update rule
   * Adjust `λ` based on error improvement
3. Return optimized parameters `x`


# Doğrusal Olmayan En Küçük Kareler Optimizasyonu için Levenberg–Marquardt Algoritması

Bu repoda, **Levenberg–Marquardt (LM)** algoritmasının bir uygulaması yer almaktadır. Bu yöntem, doğrusal olmayan en küçük kareler problemlerini çözmek için yaygın olarak kullanılır.

## 📌 Problem Tanımı

Amaç, doğrusal olmayan bir `f(x, t)` model fonksiyonu ile gözlemler `y(t)` arasındaki hataların karesel toplamını minimize etmektir:

```math
\min_{x} \sum_{i=1}^{N} \left(y_i - f(x, t_i)\right)^2
````

Burada `x`, optimize edilecek parametre vektörüdür ve `f(x, t)` tahmin fonksiyonudur.

## 🔍 Yöntem Özeti

**Levenberg–Marquardt Algoritması**, iki yöntemin avantajlarını birleştirir:

* **Gradyan inişi**: Kararlıdır ancak yavaştır
* **Gauss–Newton**: Hızlıdır ancak başlangıçtan uzaksa dengesiz olabilir

LM yöntemi, bu iki yaklaşımı `λ` adı verilen bir sönümleme katsayısı ile dengeler.

### Temel Özellikler:

* Doğrusal olmayan eğri uydurma ve makine öğrenmesi uygulamalarında kullanılır
* Jacobian matrisi `J` ile hesaplama yapılır
* Bilinmeyenden fazla denklem (overdetermined) olan sistemler için uygundur

### Güncelleme Formülü:

```math
x_{k+1} = x_k + \left(J^T J + \lambda I\right)^{-1} J^T r
```

Burada:

* `J`, modelin türevlerinden oluşan Jacobian matrisidir
* `r`, artık (residual) vektörüdür: `r = y - f(x)`
* `λ`, yöntemin ne kadar Gauss–Newton veya gradyan iniş gibi çalışacağını belirler

## ⚙️ Algoritma Adımları

1. Parametre vektörü `x₀`, sönümleme katsayısı `λ` ve tolerans tanımlanır
2. Durma koşulu sağlanana kadar:

   * Artıklar `r = y - f(x)` hesaplanır
   * Jacobian matrisi `J` hesaplanır
   * Güncelleme formülü ile `x` yeni değeri bulunur
   * Hata azalmasına göre `λ` güncellenir
3. Optimize edilmiş parametreler `x` döndürülür
