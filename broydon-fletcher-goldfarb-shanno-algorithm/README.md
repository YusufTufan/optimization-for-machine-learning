# Broyden–Fletcher–Goldfarb–Shanno (BFGS) Algorithm for Unconstrained Optimization

This repository contains a Python implementation of the **BFGS algorithm**, one of the most widely used **quasi-Newton methods** for solving unconstrained nonlinear optimization problems.

## 📌 Problem Definition

The BFGS algorithm aims to find the local minimum of a differentiable, unconstrained multivariable function `f(x)`. It does so by iteratively updating an estimate of the inverse Hessian matrix using gradient evaluations.

Mathematical Objective:

```math
\min f(x), \quad x \in \mathbb{R}^n
````

## 🔍 Method Overview

The BFGS algorithm is a **quasi-Newton method** that avoids computing the full Hessian matrix, making it computationally efficient. Instead, it builds up an approximation of the inverse Hessian matrix using gradient differences and step sizes.

**Core ideas**:

* Uses gradient vectors ∇f(x)
* Approximates the inverse of the Hessian matrix
* Updates direction using: `p_k = -H_k * ∇f_k`
* Performs line search along that direction
* Updates `H_k` using the BFGS formula

**Advantages**:

* Superlinear convergence
* No need to compute second derivatives
* More stable and accurate than DFP or steepest descent

## ⚙️ Algorithm Steps

1. Initialize `x₀`, `H₀ = I` (identity matrix)
2. While not converged:

   * Compute gradient `∇f_k`
   * Compute search direction `p_k = -H_k * ∇f_k`
   * Perform line search to find optimal step size `α_k`
   * Update position: `x_{k+1} = x_k + α_k * p_k`
   * Compute `s_k = x_{k+1} - x_k`, `y_k = ∇f_{k+1} - ∇f_k`
   * Update `H_k` using BFGS formula

# Broydon–Fletcher–Goldfarb–Shanno (BFGS) Algoritması ile Kısıtsız Optimizasyon

Bu repoda, **BFGS algoritmasının** Python ile gerçekleştirilmiş bir uygulaması bulunmaktadır. Bu yöntem, **kısıtsız doğrusal olmayan çok değişkenli fonksiyonların** optimizasyonu için yaygın olarak kullanılan bir **quasi-Newton yöntemidir**.

## 📌 Problem Tanımı

BFGS algoritmasının amacı, türevlenebilir bir çok değişkenli fonksiyonun yerel minimumunu bulmaktır. Bunu, Hessian matrisinin tersini yaklaşık olarak hesaplayarak ve gradyan bilgilerini kullanarak iteratif şekilde yapar.

Matematiksel ifade:

```math
\min f(x), \quad x \in \mathbb{R}^n
```

## 🔍 Yöntem Özeti

BFGS, tam Hessian matrisini hesaplamadan çalışan bir **quasi-Newton yöntemidir**. Gradyanlar ve adım farklarını kullanarak ters Hessian matrisin yaklaşık değerini günceller.

**Temel prensipler**:

* Gradyan vektörlerini (∇f) kullanır
* Hessian matrisin tersini yaklaşık hesaplar
* Yön: `p_k = -H_k * ∇f_k` ile hesaplanır
* Bu yönde bir adım büyüklüğü (line search) ile ilerlenir
* `H_k`, BFGS güncelleme formülüyle güncellenir

**Avantajları**:

* Süperlineer yakınsama
* İkinci türev hesaplaması gerektirmez
* DFP veya en dik iniş yöntemine göre daha kararlı ve doğrudur

## ⚙️ Algoritma Adımları

1. Başlangıç vektörü `x₀` ve `H₀ = I` olarak belirlenir
2. Yakınsama sağlanana kadar:

   * Gradyan `∇f_k` hesaplanır
   * Yön: `p_k = -H_k * ∇f_k`
   * Uygun adım büyüklüğü `α_k` için line search yapılır
   * Konum güncellenir: `x_{k+1} = x_k + α_k * p_k`
   * `s_k = x_{k+1} - x_k`, `y_k = ∇f_{k+1} - ∇f_k`
   * `H_k`, BFGS formülü ile güncellenir
