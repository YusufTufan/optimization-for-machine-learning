# Radial Basis Function (RBF) Model for Curve Fitting

This repository presents an implementation of the **Radial Basis Function (RBF) Model**, a nonlinear regression approach used to approximate relationships in scattered data using radial kernels.

## 📌 Problem Definition

The aim is to fit a nonlinear model to a set of input-output data using a weighted combination of radial basis functions centered at selected data points.

The general form of the model is:

```math
\hat{y}(t) = \sum_{i=1}^{N} x_i \cdot \phi(\|t - t_i\|)
````

Where:

* `xᵢ` are the weights to be learned
* `tᵢ` are the center points
* `φ(‖t − tᵢ‖)` is a radial basis function (e.g., Gaussian)

## 🔍 Method Overview

RBF models use basis functions that depend on the **distance** between the input and a set of fixed centers. They are especially powerful for approximating smooth nonlinear surfaces.

### Common radial functions:

* Gaussian: `φ(r) = e^{-(r^2)}`
* Multiquadric: `φ(r) = √(r² + c²)`
* Inverse quadratic: `φ(r) = 1 / (r² + c²)`

### Objective:

Minimize the squared error between the model's predictions and actual data:

```math
\min_x \sum_{i=1}^N \left(y_i - \hat{y}(t_i)\right)^2
```

## ⚙️ Algorithm Steps

1. Select the number and locations of centers `tᵢ`
2. Construct the design matrix using radial basis functions
3. Solve for weights `xᵢ` using least squares
4. Use the model to make predictions for new inputs

# Eğri Uydurma için Radyal Tabanlı Fonksiyon (RBF) Modeli

Bu repoda, dağınık verilere doğrusal olmayan bir model uydurmak için kullanılan **Radyal Tabanlı Fonksiyon (RBF)** modelinin bir uygulaması bulunmaktadır.

## 📌 Problem Tanımı

Amaç, belirli merkez noktalar etrafında tanımlanan radyal tabanlı fonksiyonların ağırlıklı birleşimi ile verilere eğri uydurmaktır.

Modelin genel formu:

```math
\hat{y}(t) = \sum_{i=1}^{N} x_i \cdot \phi(\|t - t_i\|)
````

Burada:

* `xᵢ`, öğrenilecek ağırlıklardır
* `tᵢ`, merkez noktalarıdır
* `φ(‖t − tᵢ‖)`, radyal tabanlı fonksiyondur (örneğin Gaussian)

## 🔍 Yöntem Özeti

RBF modelleri, girdiler ile sabit merkezler arasındaki **mesafeye** dayalı olarak tanımlanan fonksiyonları kullanır. Özellikle düzgün ve doğrusal olmayan yüzeyleri yaklaşık olarak ifade etmekte çok başarılıdır.

### Yaygın radyal fonksiyonlar:

* Gaussian: `φ(r) = e^{-(r^2)}`
* Multikvadratik: `φ(r) = √(r² + c²)`
* Ters kvadratik: `φ(r) = 1 / (r² + c²)`

### Amaç:

Model tahminleri ile gerçek veriler arasındaki hata karesini minimize etmektir:

```math
\min_x \sum_{i=1}^N \left(y_i - \hat{y}(t_i)\right)^2
```

## ⚙️ Algoritma Adımları

1. Merkezlerin sayısı ve konumları belirlenir (`tᵢ`)
2. Radyal fonksiyonlar kullanılarak tasarım matrisi oluşturulur
3. Ağırlıklar `xᵢ`, en küçük kareler yöntemiyle çözülür
4. Yeni girişler için model tahmin üretir

