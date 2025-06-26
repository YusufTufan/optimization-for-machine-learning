# Newton–Raphson Method for Unconstrained Optimization

This repository presents an implementation of the **Newton–Raphson Algorithm**, a second-order optimization method used to find the local minimum of differentiable scalar functions.

## 📌 Problem Definition

The goal is to minimize a twice-differentiable objective function `f(x)` over ℝⁿ:

```math
\min_{x \in \mathbb{R}^n} f(x)
````

The method utilizes both the gradient and the Hessian matrix to determine the search direction and step size.

## 🔍 Method Overview

The **Newton–Raphson method** is a root-finding approach adapted for optimization by setting the gradient to zero:

```math
\nabla f(x) = 0
```

A second-order Taylor expansion of `f(x)` is used to construct a quadratic model around the current point. The next point is then found by solving:

```math
x_{k+1} = x_k - H^{-1} \nabla f(x_k)
```

Where:

* `∇f(xₖ)` is the gradient vector
* `H` is the Hessian matrix of second derivatives

### Key Features:

* Fast local convergence if the Hessian is well-behaved
* Requires second-order derivatives
* Can converge to saddle points if not carefully handled

## ⚙️ Algorithm Steps

1. Choose an initial guess `x₀`
2. While stopping criterion not met:

   * Compute gradient `∇f(xₖ)`
   * Compute Hessian matrix `H`
   * Solve: `xₖ₊₁ = xₖ - H⁻¹ ∇f(xₖ)`
3. Return estimated minimum point `x`

````

---

```markdown
# Kısıtsız Optimizasyon için Newton–Raphson Yöntemi

Bu repoda, iki kere türevlenebilir fonksiyonların minimumunu bulmak için kullanılan ikinci dereceden bir yöntem olan **Newton–Raphson Algoritması** uygulanmaktadır.

## 📌 Problem Tanımı

Amaç, aşağıdaki gibi bir `f(x)` fonksiyonunu ℝⁿ uzayında minimize etmektir:

```math
\min_{x \in \mathbb{R}^n} f(x)
````

Yöntem, hem gradyan hem de Hessian (ikinci türev matrisini) kullanarak arama yönünü ve adım büyüklüğünü belirler.

## 🔍 Yöntem Özeti

**Newton–Raphson yöntemi**, orijinalde kök bulma amacıyla geliştirilmiştir. Optimizasyonda, `∇f(x) = 0` eşitliği çözülerek lokal minimum noktası aranır.

Fonksiyonun ikinci dereceden Taylor açılımı ile çevresindeki yaklaşık model kurulur. Sonraki nokta şu şekilde hesaplanır:

```math
x_{k+1} = x_k - H^{-1} \nabla f(x_k)
```

Burada:

* `∇f(xₖ)` gradyan vektörüdür
* `H`, fonksiyonun Hessian matrisidir (ikinci türevler)

### Temel Özellikler:

* Eğer Hessian düzgünse hızlı yakınsama sağlar
* İkinci türev bilgisi gerektirir
* Uygun kontrol yapılmazsa eyer noktalarına yakınsama riski vardır

## ⚙️ Algoritma Adımları

1. Başlangıç noktası `x₀` seçilir
2. Durma koşulu sağlanana kadar:

   * Gradyan `∇f(xₖ)` hesaplanır
   * Hessian matrisi `H` bulunur
   * Yeni nokta hesaplanır: `xₖ₊₁ = xₖ - H⁻¹ ∇f(xₖ)`
3. Minimum noktası `x` döndürülür
