# Davidon–Fletcher–Powell (DFP) Algorithm for Unconstrained Optimization

This repository includes a Python implementation of the **DFP algorithm**, a quasi-Newton method used to solve unconstrained nonlinear optimization problems by approximating the inverse Hessian matrix.

## 📌 Problem Definition

The objective is to minimize a multivariable, continuously differentiable function `f(x)` using only first-order derivative information.

Mathematically:

```math
\min f(x), \quad x \in \mathbb{R}^n
````

## 🔍 Method Overview

The **DFP algorithm** is one of the earliest quasi-Newton methods. Instead of computing the Hessian matrix directly, it maintains and updates an approximation of the **inverse Hessian** in each iteration using gradient differences and step vectors.

### Core Concepts:

* Iterative approximation of inverse Hessian matrix `Hₖ`
* Uses gradient vectors `∇fₖ` at each step
* Update rule uses `sₖ = xₖ₊₁ - xₖ` and `yₖ = ∇fₖ₊₁ - ∇fₖ`

**Update formula**:

```math
H_{k+1} = H_k + \frac{s_k s_k^T}{s_k^T y_k} - \frac{H_k y_k y_k^T H_k}{y_k^T H_k y_k}
```

**Advantages**:

* Faster convergence than steepest descent
* No need to compute the true Hessian
* Suitable for large-scale optimization problems

## ⚙️ Algorithm Steps

1. Initialize starting point `x₀` and set `H₀ = I` (identity matrix)
2. While not converged:

   * Compute gradient `∇fₖ`
   * Determine search direction `dₖ = -Hₖ * ∇fₖ`
   * Perform line search to compute step size `αₖ`
   * Update position: `xₖ₊₁ = xₖ + αₖ * dₖ`
   * Compute `sₖ = xₖ₊₁ - xₖ`, `yₖ = ∇fₖ₊₁ - ∇fₖ`
   * Update inverse Hessian approximation `Hₖ` using DFP formula

---

# Davidon–Fletcher–Powell (DFP) Algoritması ile Kısıtsız Optimizasyon

Bu repoda, **DFP algoritmasının** Python ile gerçekleştirilmiş bir uygulaması bulunmaktadır. DFP, Hessian matrisini yaklaşık olarak hesaplayarak **kısıtsız doğrusal olmayan fonksiyonların** minimizasyonunda kullanılan bir **quasi-Newton yöntemidir**.

## 📌 Problem Tanımı

Amaç, sürekli türevlenebilir çok değişkenli bir `f(x)` fonksiyonunun minimumunu, yalnızca birinci türev bilgisi kullanarak bulmaktır.

Matematiksel ifade:

```math
\min f(x), \quad x \in \mathbb{R}^n
```

## 🔍 Yöntem Özeti

**DFP algoritması**, en eski quasi-Newton yöntemlerinden biridir. Gerçek Hessian matrisini doğrudan hesaplamak yerine, onun tersinin yaklaşık değerini iteratif olarak günceller. Bu işlem, gradyan ve adım farklarına dayanır.

### Temel Kavramlar:

* `Hₖ` ile ters Hessian matrisi yaklaşık olarak tutulur
* Her adımda gradyan `∇fₖ` kullanılır
* Güncelleme: `sₖ = xₖ₊₁ - xₖ`, `yₖ = ∇fₖ₊₁ - ∇fₖ`

**Güncelleme formülü**:

```math
H_{k+1} = H_k + \frac{s_k s_k^T}{s_k^T y_k} - \frac{H_k y_k y_k^T H_k}{y_k^T H_k y_k}
```

**Avantajları**:

* En dik inişe göre daha hızlı yakınsar
* Gerçek Hessian matrisine ihtiyaç duymaz
* Büyük ölçekli problemlerde kullanılabilir

## ⚙️ Algoritma Adımları

1. Başlangıç noktası `x₀` ve başlangıç matris `H₀ = I` seçilir
2. Yakınsama sağlanana kadar:

   * Gradyan `∇fₖ` hesaplanır
   * Arama yönü: `dₖ = -Hₖ * ∇fₖ`
   * Line search ile `αₖ` adımı hesaplanır
   * Yeni nokta: `xₖ₊₁ = xₖ + αₖ * dₖ`
   * `sₖ = xₖ₊₁ - xₖ`, `yₖ = ∇fₖ₊₁ - ∇fₖ` hesaplanır
   * DFP formülüyle `Hₖ` güncellenir
