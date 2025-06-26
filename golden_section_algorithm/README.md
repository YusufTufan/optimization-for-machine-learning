# Golden Section Method for Univariate Optimization

This repository includes a Python implementation of the **Golden Section Method**, a bracketing optimization algorithm used for finding the minimum of a unimodal function in a closed interval.

## 📌 Problem Definition

The goal is to minimize a **unimodal** function `f(x)` over a closed interval `[a, b]` without using derivatives.

Mathematically:

```math
\min_{x \in [a, b]} f(x)
````

This method assumes that `f(x)` has a single minimum within the interval `[a, b]`.

## 🔍 Method Overview

The **Golden Section Search** is an efficient algorithm that reduces the interval of uncertainty at each step using the **golden ratio (ϕ ≈ 1.618)**.

### Key Characteristics:

* Derivative-free method
* Guaranteed convergence for unimodal functions
* Uses fixed ratio to avoid recomputation
* More efficient than uniform sampling or exhaustive search

The interval is reduced by evaluating `f(x)` at two interior points:

```math
x₁ = b - (b - a) / ϕ  
x₂ = a + (b - a) / ϕ
```

Depending on `f(x₁)` and `f(x₂)`, the interval is updated to eliminate the less promising side.

## ⚙️ Algorithm Steps

1. Define initial interval `[a, b]` and tolerance `ε`
2. Compute golden ratio `ϕ = (1 + √5) / 2`
3. Calculate `x₁` and `x₂`
4. Evaluate `f(x₁)` and `f(x₂)`
5. If `f(x₁) < f(x₂)`, update `b = x₂`, else update `a = x₁`
6. Repeat until interval width is less than `ε`

---

# Tek Değişkenli Optimizasyon için Altın Bölme Yöntemi

Bu repoda, kapalı bir aralıkta **tek minimuma sahip (unimodal)** bir fonksiyonun minimumunu türev kullanmadan bulmak için kullanılan **Altın Bölme (Golden Section)** yönteminin Python implementasyonu yer almaktadır.

## 📌 Problem Tanımı

Amaç, kapalı bir `[a, b]` aralığında tanımlı tek minimuma sahip bir `f(x)` fonksiyonunu türev kullanmadan minimize etmektir.

Matematiksel ifade:

```math
\min_{x \in [a, b]} f(x)
```

Burada `f(x)` fonksiyonunun verilen aralıkta yalnızca bir minimum noktası olduğu varsayılır.

## 🔍 Yöntem Özeti

**Altın Bölme Yöntemi**, her adımda aralık genişliğini **altın oran (ϕ ≈ 1.618)** kullanarak azaltan verimli bir optimizasyon algoritmasıdır.

### Temel Özellikler:

* Türeve ihtiyaç duymaz
* Tek minimumlu fonksiyonlar için yakınsamayı garanti eder
* Sabit oran kullandığı için hesaplamalar daha verimlidir
* Kaba örnekleme yöntemlerinden daha hızlıdır

İki iç nokta belirlenerek değerlendirme yapılır:

```math
x₁ = b - (b - a) / ϕ  
x₂ = a + (b - a) / ϕ
```

`f(x₁)` ve `f(x₂)` karşılaştırılır, daha yüksek olan tarafın aralık dışına atılmasıyla aralık daraltılır.

## ⚙️ Algoritma Adımları

1. Başlangıç aralığı `[a, b]` ve tolerans `ε` tanımlanır
2. Altın oran `ϕ = (1 + √5) / 2` hesaplanır
3. `x₁` ve `x₂` bulunur
4. `f(x₁)` ve `f(x₂)` hesaplanır
5. Eğer `f(x₁) < f(x₂)` ise `b = x₂`, aksi takdirde `a = x₁` yapılır
6. Aralık genişliği `ε`'den küçük olana kadar tekrar edilir

