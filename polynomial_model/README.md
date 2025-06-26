# Polynomial Model for Nonlinear Curve Fitting

This repository provides an implementation of the **polynomial model**, commonly used in curve fitting tasks where the relationship between the variables follows a nonlinear polynomial form.

## 📌 Problem Definition

The goal is to fit a model to data using a polynomial function of degree `n`. The general form is:

```math
\hat{y}(t) = x_1 + x_2 t + x_3 t^2 + \dots + x_n t^{n-1}
````

Where:

* `x₁, x₂, ..., xₙ` are the model parameters
* `t` is the independent variable
* `ŷ(t)` is the predicted output

## 🔍 Method Overview

The polynomial model is a nonlinear function in `t` but **linear in parameters**, which allows it to be solved using least squares techniques.

### Applications:

* Data modeling and forecasting
* Engineering curve fitting
* Experimental data approximation

### Cost Function:

```math
\min_{x} \sum_{i=1}^{N} \left(y_i - \hat{y}(t_i)\right)^2
```

Where:

* `yᵢ` is the observed value
* `ŷ(tᵢ)` is the predicted value from the polynomial model

## ⚙️ Algorithm Steps

1. Choose the degree `n` of the polynomial
2. Build the design matrix using `t, t², ..., tⁿ⁻¹`
3. Solve the normal equations or apply least squares
4. Return the best-fit parameters

# Polinomsal Model ile Doğrusal Olmayan Eğri Uydurma

Bu repoda, değişkenler arasındaki ilişki **polinomsal** bir yapıda olan veriler için kullanılan **polinomsal modelin** uygulaması yer almaktadır.

## 📌 Problem Tanımı

Amaç, derecesi `n` olan bir polinom fonksiyon kullanarak verilere bir model uydurmaktır. Genel form:

```math
\hat{y}(t) = x_1 + x_2 t + x_3 t^2 + \dots + x_n t^{n-1}
````

Burada:

* `x₁, x₂, ..., xₙ` model parametreleridir
* `t` bağımsız değişkendir
* `ŷ(t)` tahmin edilen çıktıdır

## 🔍 Yöntem Özeti

Polinomsal model, `t` açısından doğrusal olmayan bir fonksiyon olsa da, **parametreler açısından doğrusaldır**, bu sayede en küçük kareler yöntemiyle kolayca çözülebilir.

### Kullanım Alanları:

* Veri modelleme ve tahmin
* Mühendislikte eğri uydurma
* Deneysel verilerin yaklaşık modellenmesi

### Hata Fonksiyonu:

```math
\min_{x} \sum_{i=1}^{N} \left(y_i - \hat{y}(t_i)\right)^2
```

Burada:

* `yᵢ` gözlemlenen değeri
* `ŷ(tᵢ)` polinomsal modelin tahminini temsil eder

## ⚙️ Algoritma Adımları

1. Polinomun derecesi `n` belirlenir
2. Tasarım matrisi `t, t², ..., tⁿ⁻¹` içerecek şekilde oluşturulur
3. Normal denklemler çözülür veya en küçük kareler yöntemi uygulanır
4. En iyi parametreler elde edilir
