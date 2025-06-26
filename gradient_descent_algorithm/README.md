# Gradient Descent Algorithm for Unconstrained Optimization

This repository contains a Python implementation of the **Gradient Descent Algorithm**, a fundamental first-order optimization technique used to minimize differentiable scalar functions.

## 📌 Problem Definition

The objective is to minimize a continuously differentiable function `f(x)` over ℝⁿ using only first-order derivative (gradient) information.

Mathematically:

```math
\min_{x \in \mathbb{R}^n} f(x)
````

## 🔍 Method Overview

**Gradient Descent** is an iterative method that updates the solution in the direction of the negative gradient of the function, which points toward the steepest descent.

### Key Concepts:

* Uses the gradient `∇f(x)` to guide updates
* Does not require second derivatives
* Step size (learning rate) `α` is crucial for convergence

### Update Rule:

```math
x_{k+1} = x_k - \alpha \nabla f(x_k)
```

* A small `α` causes slow convergence
* A large `α` may overshoot or diverge
* `α` may be fixed or determined via line search

## ⚙️ Algorithm Steps

1. Choose initial guess `x₀`
2. Set learning rate `α` and tolerance `ε`
3. While `‖∇f(xₖ)‖ > ε`:

   * Compute gradient `∇f(xₖ)`
   * Update: `xₖ₊₁ = xₖ - α ∇f(xₖ)`
4. Return final `x` as the estimated minimum

---

# Kısıtsız Optimizasyon için Gradyan İnişi (Gradient Descent) Algoritması

Bu repoda, sürekli türevlenebilir bir skaler fonksiyonun minimumunu bulmak için kullanılan temel bir birinci dereceden optimizasyon yöntemi olan **Gradyan İnişi (Gradient Descent)** algoritmasının Python implementasyonu yer almaktadır.

## 📌 Problem Tanımı

Amaç, sadece birinci türev bilgisi (gradyan) kullanarak sürekli türevlenebilir bir `f(x)` fonksiyonunu ℝⁿ uzayında minimize etmektir.

Matematiksel ifade:

```math
\min_{x \in \mathbb{R}^n} f(x)
```

## 🔍 Yöntem Özeti

**Gradyan İnişi** algoritması, çözümü, fonksiyonun en hızlı azalma yönü olan negatif gradyan doğrultusunda güncelleyerek iteratif olarak yaklaştırır.

### Temel Kavramlar:

* Güncellemelerde `∇f(x)` gradyanı kullanılır
* İkinci türev bilgisine ihtiyaç duymaz
* Adım büyüklüğü (learning rate) `α`, yakınsama için kritik önemdedir

### Güncelleme Kuralı:

```math
x_{k+1} = x_k - \alpha \nabla f(x_k)
```

* `α` çok küçükse yakınsama yavaş olur
* `α` çok büyükse sapma veya patlama olabilir
* `α`, sabit tutulabilir ya da line search ile ayarlanabilir

## ⚙️ Algoritma Adımları

1. Başlangıç noktası `x₀` seçilir
2. Öğrenme oranı `α` ve tolerans `ε` belirlenir
3. `‖∇f(xₖ)‖ > ε` olduğu sürece:

   * Gradyan `∇f(xₖ)` hesaplanır
   * Güncelleme yapılır: `xₖ₊₁ = xₖ - α ∇f(xₖ)`
4. Minimum olarak `x` döndürülür
