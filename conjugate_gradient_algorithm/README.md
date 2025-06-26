# Conjugate Gradient (Fletcher–Reeves) Algorithm for Unconstrained Optimization

This repository contains an implementation of the **Conjugate Gradient Method**, specifically the **Fletcher–Reeves variant**, for solving unconstrained nonlinear optimization problems.

## 📌 Problem Definition

The goal is to minimize a multivariable differentiable function `f(x)` without any constraints, using only first-order derivative (gradient) information.

Mathematically:

```math
\min f(x), \quad x \in \mathbb{R}^n
````

## 🔍 Method Overview

The **Conjugate Gradient (CG) Method** is a first-order optimization algorithm designed for large-scale unconstrained optimization. Unlike steepest descent, CG generates conjugate directions that lead to faster convergence.

The **Fletcher–Reeves version** of CG:

* Uses gradient vectors and updates the search direction based on previous gradient information
* Does not require Hessian matrix or its approximation
* Is efficient for quadratic or nearly quadratic functions

**Key update rule**:

* `d₀ = -∇f₀` (initial direction)
* `βₖ = (∇fₖ)ᵀ ∇fₖ / (∇fₖ₋₁)ᵀ ∇fₖ₋₁`
* `dₖ = -∇fₖ + βₖ * dₖ₋₁`

## ⚙️ Algorithm Steps

1. Initialize `x₀` and set initial direction `d₀ = -∇f₀`
2. For each iteration:

   * Perform line search to find optimal step size `αₖ`
   * Update position: `xₖ₊₁ = xₖ + αₖ * dₖ`
   * Compute new gradient `∇fₖ₊₁`
   * Compute `βₖ` using Fletcher–Reeves formula
   * Update direction: `dₖ = -∇fₖ + βₖ * dₖ₋₁`
3. Repeat until convergence

---

# Kısıtsız Optimizasyon için Conjugate Gradient (Fletcher–Reeves) Algoritması

Bu repoda, kısıtsız doğrusal olmayan optimizasyon problemleri için kullanılan **Conjugate Gradient (Konjugat Gradyan) Yöntemi**, özellikle **Fletcher–Reeves** varyantı uygulanmıştır.

## 📌 Problem Tanımı

Amaç, herhangi bir kısıt olmadan, türevlenebilir çok değişkenli bir fonksiyon `f(x)`'in minimumunu bulmaktır. Bu işlem yalnızca birinci dereceden türev (gradyan) bilgisi ile gerçekleştirilir.

Matematiksel ifade:

```math
\min f(x), \quad x \in \mathbb{R}^n
```

## 🔍 Yöntem Özeti

**Conjugate Gradient (CG) Yöntemi**, büyük boyutlu kısıtsız optimizasyon problemleri için geliştirilmiş bir birinci dereceden algoritmadır. En dik iniş yönteminden farklı olarak, her iterasyonda doğrultular birbirine konjugat olacak şekilde seçilir ve bu sayede daha hızlı yakınsama sağlanır.

**Fletcher–Reeves sürümü**:

* Gradyan bilgilerini kullanarak arama yönünü günceller
* Hessian matrisine veya yaklaşık hesaplamasına gerek duymaz
* Kuadratik veya kuadratiğe yakın fonksiyonlar için oldukça etkilidir

**Temel güncelleme formülü**:

* `d₀ = -∇f₀` (ilk yön)
* `βₖ = (∇fₖ)ᵀ ∇fₖ / (∇fₖ₋₁)ᵀ ∇fₖ₋₁`
* `dₖ = -∇fₖ + βₖ * dₖ₋₁`

## ⚙️ Algoritma Adımları

1. Başlangıç noktası `x₀` seçilir, yön `d₀ = -∇f₀` olarak belirlenir
2. Her iterasyonda:

   * Line search ile uygun `αₖ` adım büyüklüğü hesaplanır
   * Yeni nokta: `xₖ₊₁ = xₖ + αₖ * dₖ`
   * Yeni gradyan `∇fₖ₊₁` hesaplanır
   * Fletcher–Reeves formülüyle `βₖ` hesaplanır
   * Yeni yön: `dₖ = -∇fₖ + βₖ * dₖ₋₁`
3. Yakınsama sağlanana kadar devam edilir
