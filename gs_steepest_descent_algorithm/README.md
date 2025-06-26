# Steepest Descent Method with Golden Section Line Search

This repository implements the **Steepest Descent Algorithm** combined with **Golden Section Line Search** to solve unconstrained nonlinear optimization problems more efficiently.

## 📌 Problem Definition

The goal is to minimize a differentiable scalar function `f(x)` without constraints by moving in the direction of steepest descent (i.e., negative gradient) and determining the optimal step size using golden section search.

Mathematically:

```math
\min_{x \in \mathbb{R}^n} f(x)
````

## 🔍 Method Overview

**Steepest Descent Method** is a first-order iterative optimization technique that updates the current solution by moving along the direction of the negative gradient.

To improve convergence, the step size (learning rate) at each iteration is computed using **Golden Section Search**, instead of using a fixed or arbitrary value.

### Key Features:

* Derivative-based method (requires gradient)
* Direction: `dₖ = -∇f(xₖ)`
* Step size `αₖ` is chosen via golden section line search
* Suitable for convex or smooth non-convex functions

## ⚙️ Algorithm Steps

1. Initialize `x₀`
2. While stopping criteria not met:
   a. Compute gradient `∇f(xₖ)`
   b. Set direction `dₖ = -∇f(xₖ)`
   c. Use Golden Section Search to find optimal `αₖ` along `dₖ`
   d. Update position: `xₖ₊₁ = xₖ + αₖ * dₖ`
3. Return the best solution found

---

# Altın Bölme ile En Dik İniş (Steepest Descent) Yöntemi

Bu repoda, **En Dik İniş (Steepest Descent)** algoritması ve **Altın Bölme (Golden Section)** çizgisel arama yöntemi birlikte kullanılarak türevlenebilir fonksiyonların daha verimli optimize edilmesi amaçlanmaktadır.

## 📌 Problem Tanımı

Amaç, herhangi bir kısıt olmaksızın, türevlenebilir bir skaler `f(x)` fonksiyonunu minimize etmektir. Bu, en hızlı azalma yönü olan negatif gradyan doğrultusunda ilerleyerek ve adım büyüklüğünü altın oranla belirleyerek gerçekleştirilir.

Matematiksel ifade:

```math
\min_{x \in \mathbb{R}^n} f(x)
```

## 🔍 Yöntem Özeti

**En Dik İniş Yöntemi**, mevcut çözümü, fonksiyonun negatif gradyanı yönünde güncelleyerek iteratif olarak en iyi çözüme yaklaşır.

Bu uygulamada, her adımda adım büyüklüğü (`αₖ`) sabit değil, **Altın Bölme Araması** ile en iyi değer olarak belirlenir.

### Temel Özellikler:

* Gradyan tabanlı bir optimizasyon yöntemidir
* Yön: `dₖ = -∇f(xₖ)`
* Adım büyüklüğü: Altın Bölme yöntemiyle hesaplanır
* Konveks ve düzgün doğrusal olmayan fonksiyonlar için uygundur

## ⚙️ Algoritma Adımları

1. Başlangıç noktası `x₀` seçilir
2. Durma kriteri sağlanana kadar:
   a. Gradyan `∇f(xₖ)` hesaplanır
   b. Yön `dₖ = -∇f(xₖ)` olarak belirlenir
   c. Bu yön boyunca optimum `αₖ`, Altın Bölme ile hesaplanır
   d. Güncelleme: `xₖ₊₁ = xₖ + αₖ * dₖ`
3. En iyi bulunan çözüm döndürülür

