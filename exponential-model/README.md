# Exponential Model for Curve Fitting and Prediction

This repository provides an implementation of the **exponential model** used in curve fitting and predictive modeling tasks. The model aims to fit a mathematical curve to a given dataset using a nonlinear exponential form.

## 📌 Problem Definition

The objective is to fit a curve of the form:

```math
\hat{y}(t) = x_1 e^{x_2 t}
````

Here, `x₁` and `x₂` are parameters to be optimized, and `t` is the input (independent variable). The model is optimized to minimize the error between predicted values `ŷ(t)` and actual values `y(t)`.

## 🔍 Method Overview

Exponential models are a type of **nonlinear regression** where the response variable exhibits exponential growth or decay. These models are widely used in:

* Population dynamics
* Radioactive decay
* Finance (compound interest)
* Machine learning for learning nonlinear patterns

### Key Features:

* Nonlinear optimization problem
* May require initial guesses for parameters
* Typically solved using iterative methods like Gauss-Newton or Levenberg-Marquardt

**Objective Function**:

```math
\min_{x} \sum_{i=1}^{N} (y_i - x_1 e^{x_2 t_i})^2
```

This function measures the squared error between predicted and actual values.

## ⚙️ Algorithm Steps

1. Define the exponential model function
2. Provide initial guesses for `x₁`, `x₂`
3. Minimize the sum of squared errors using an optimizer
4. Evaluate model accuracy (optional)

---

# Eğri Uydurma ve Tahmin için Üstel Model

Bu repoda, **üstel model (exponential model)** kullanılarak bir veri kümesine matematiksel eğri uydurulmuştur. Model, doğrusal olmayan formda bir eğriyle veri noktaları arasında en iyi uyumu sağlamak için tasarlanmıştır.

## 📌 Problem Tanımı

Uydurulmak istenen eğri şu şekildedir:

```math
\hat{y}(t) = x_1 e^{x_2 t}
```

Burada `x₁` ve `x₂` modelin optimize edilmesi gereken parametreleridir; `t` ise bağımsız değişkendir. Amaç, `ŷ(t)` ile gerçek `y(t)` değerleri arasındaki hatayı en aza indirmektir.

## 🔍 Yöntem Özeti

Üstel modeller, tepki değişkeninin üstel şekilde arttığı ya da azaldığı **doğrusal olmayan regresyon** türleridir. Sıklıkla şu alanlarda kullanılır:

* Nüfus dinamiği
* Radyoaktif bozunma
* Finans (bileşik faiz hesaplamaları)
* Makine öğrenmesinde doğrusal olmayan desenlerin öğrenilmesi

### Temel Özellikler:

* Doğrusal olmayan optimizasyon problemidir
* Başlangıç parametre tahminleri gerekebilir
* Genellikle Gauss-Newton veya Levenberg-Marquardt gibi iteratif yöntemlerle çözülür

**Amaç Fonksiyonu**:

```math
\min_{x} \sum_{i=1}^{N} (y_i - x_1 e^{x_2 t_i})^2
```

Bu fonksiyon, tahmin edilen değerler ile gerçek değerler arasındaki karesel hatayı minimize eder.

## ⚙️ Algoritma Adımları

1. Üstel model fonksiyonu tanımlanır
2. `x₁`, `x₂` için başlangıç tahminleri yapılır
3. Karesel hata toplamı minimize edilir
4. (Opsiyonel) Model doğruluğu değerlendirilir
