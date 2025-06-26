# Modified Newton Algorithm for Nonlinear Optimization

This repository contains a Python implementation of the **Modified Newton Algorithm**, an improved version of the classical Newton’s method used for unconstrained nonlinear optimization.

## 📌 Problem Definition

The objective is to find the local minimum of a twice-differentiable scalar function `f(x)`:

```math
\min_{x \in \mathbb{R}^n} f(x)
````

This method leverages second-order derivative information but applies modifications to improve stability and convergence in practical implementations.

## 🔍 Method Overview

The classical Newton method uses the inverse of the Hessian matrix for updating the solution. However, in cases where the Hessian is not positive definite, the classical method may fail or converge to a saddle point.

The **Modified Newton Method** addresses this by:

* Adjusting the Hessian to ensure it is positive definite (e.g., by adding a multiple of the identity matrix)
* Ensuring that the search direction is a descent direction

### Update Rule:

```math
x_{k+1} = x_k - \alpha_k H_k^{-1} \nabla f(x_k)
```

Where:

* `H_k` is a modified (positive definite) approximation of the Hessian
* `α_k` is step size, typically determined via line search

## ⚙️ Algorithm Steps

1. Choose initial point `x₀`
2. Compute gradient `∇f(xₖ)` and Hessian `∇²f(xₖ)`
3. Modify the Hessian if it’s not positive definite
4. Solve for the direction `dₖ = -H_k⁻¹ ∇f(xₖ)`
5. Use line search to find step size `αₖ`
6. Update: `xₖ₊₁ = xₖ + αₖ dₖ`
7. Repeat until convergence

# Doğrusal Olmayan Optimizasyon için Değiştirilmiş Newton (Modified Newton) Algoritması

Bu repoda, klasik Newton yönteminin daha kararlı ve uygulanabilir hale getirilmiş bir versiyonu olan **Değiştirilmiş Newton Algoritması** Python ile uygulanmıştır.

## 📌 Problem Tanımı

Amaç, iki kere türevlenebilir bir `f(x)` fonksiyonunun yerel minimumunu bulmaktır:

```math
\min_{x \in \mathbb{R}^n} f(x)
````

Yöntem, ikinci türev (Hessian) bilgisi kullanarak hızlı yakınsama sağlar ancak kararlılığı artırmak için bazı iyileştirmeler içerir.

## 🔍 Yöntem Özeti

Klasik Newton yöntemi, Hessian matrisinin tersini kullanarak çözüm üretir. Ancak Hessian pozitif tanımlı değilse, yöntem başarısız olabilir veya eyer noktasına yakınsayabilir.

**Değiştirilmiş Newton Yöntemi**, bu sorunları aşağıdaki yollarla çözer:

* Hessian matrisini pozitif tanımlı yapmak için gerekirse üzerine sabit birim matris eklenir
* Arama yönünün iniş yönü olması garanti altına alınır

### Güncelleme Kuralı:

```math
x_{k+1} = x_k - \alpha_k H_k^{-1} \nabla f(x_k)
```

Burada:

* `H_k`, pozitif tanımlı hale getirilmiş Hessian matrisidir
* `α_k`, adım büyüklüğüdür ve genelde çizgisel arama (line search) ile belirlenir

## ⚙️ Algoritma Adımları

1. Başlangıç noktası `x₀` seçilir
2. `∇f(xₖ)` gradyanı ve `∇²f(xₖ)` Hessian’ı hesaplanır
3. Hessian pozitif tanımlı değilse modifiye edilir
4. Yön vektörü çözülür: `dₖ = -H_k⁻¹ ∇f(xₖ)`
5. Çizgisel arama ile uygun `αₖ` bulunur
6. Güncelleme yapılır: `xₖ₊₁ = xₖ + αₖ dₖ`
7. Yakınsama sağlanana kadar devam edilir

