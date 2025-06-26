# Classification Using Levenberg–Marquardt Algorithm

This repository provides a Python implementation of a **classification model** trained using the **Levenberg–Marquardt (LM)** algorithm. While traditionally used for nonlinear regression, LM can be adapted to classification problems by minimizing error over class outputs.

## 📌 Problem Definition

The objective is to classify input samples into predefined categories by training a model that minimizes the squared error between predicted outputs and actual class labels.

The cost function is:

```math
\min_{x} \sum_{i=1}^{N} \left(y_i - f(x, t_i)\right)^2
````

Where:

* `x` is the model parameter vector
* `f(x, t_i)` is the predicted output (class probability or label)
* `y_i` is the true label (often one-hot encoded for multi-class)

## 🔍 Method Overview

The LM algorithm updates model parameters to minimize the squared classification error, using the Jacobian matrix and a damping factor λ to balance between:

* **Gradient descent** (for stability)
* **Gauss–Newton** (for speed near solution)

Although it’s less common than gradient-based methods like Adam or SGD, LM can achieve fast convergence in small-to-medium classification tasks.

### Key Features:

* Nonlinear classification support
* Fast convergence for smooth cost surfaces
* Good performance when class outputs are modeled continuously

## ⚙️ Algorithm Steps

1. Prepare input data and one-hot encoded labels
2. Initialize parameters and damping factor `λ`
3. While not converged:

   * Compute output and residuals
   * Compute Jacobian
   * Update parameters using LM rule
   * Adjust `λ` based on performance
4. Output class predictions

# Levenberg–Marquardt Algoritması ile Sınıflandırma

Bu repoda, **Levenberg–Marquardt (LM)** algoritması kullanılarak eğitilmiş bir **sınıflandırma modeli** Python ile uygulanmıştır. LM yöntemi genellikle regresyon için kullanılsa da, sınıflandırma problemlerinde de hata fonksiyonunu minimize etmek için uyarlanabilir.

## 📌 Problem Tanımı

Amaç, girdi verilerini belirli sınıflara ayırmak ve modelin çıktısı ile gerçek etiketler (label) arasındaki hatayı en aza indirmektir.

Maliyet (cost) fonksiyonu şu şekildedir:

```math
\min_{x} \sum_{i=1}^{N} \left(y_i - f(x, t_i)\right)^2
````

Burada:

* `x`, modelin parametre vektörüdür
* `f(x, t_i)`, tahmin edilen çıktı (olasılık ya da etiket)
* `y_i`, gerçek sınıf etiketidir (çok sınıflı için genelde one-hot encoded kullanılır)

## 🔍 Yöntem Özeti

LM algoritması, sınıflandırma hatasını azaltmak için model parametrelerini günceller. Güncelleme sırasında Jacobian matrisi ve sönümleme faktörü `λ` kullanılır. Böylece:

* **Gradyan iniş** ile kararlılık sağlanır
* **Gauss–Newton** ile hız kazandırılır

Her ne kadar SGD veya Adam kadar yaygın olmasa da, LM algoritması küçük ve orta ölçekli sınıflandırma problemlerinde hızlı yakınsama sağlayabilir.

### Temel Özellikler:

* Doğrusal olmayan sınıflandırma destekler
* Düzgün maliyet yüzeylerinde hızlı yakınsar
* Sürekli çıktı veren sınıflandırıcı yapılar için uygundur

## ⚙️ Algoritma Adımları

1. Girdi verisi ve one-hot etiketler hazırlanır
2. Parametreler ve sönümleme katsayısı `λ` tanımlanır
3. Yakınsama sağlanana kadar:

   * Çıktılar ve artıklar hesaplanır
   * Jacobian matrisi oluşturulur
   * Parametreler LM güncellemesi ile yenilenir
   * `λ` hata durumuna göre güncellenir
4. Sınıf tahminleri üretilir
