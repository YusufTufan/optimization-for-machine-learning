# Feedforward Artificial Neural Network (FFANN) Classifier with Scikit-learn

This repository presents an implementation of a **Feedforward Artificial Neural Network (FFANN)** classifier using the `scikit-learn` library. FFANNs are foundational models in machine learning, particularly used for supervised learning tasks such as classification and regression.

## 📌 Problem Definition

The objective is to train a neural network to classify input data into predefined categories using labeled training data. The model learns by adjusting weights based on error between predicted and actual outputs.

## 🔍 Method Overview

A **Feedforward Neural Network** consists of:
- Input layer  
- One or more hidden layers  
- Output layer

In a feedforward architecture:
- Data flows in one direction: from input to output  
- There are no cycles or feedback loops  
- Activation functions (e.g., sigmoid, ReLU) introduce non-linearity

### Key Characteristics:
- Supervised learning algorithm  
- Trained via backpropagation and gradient descent  
- Suitable for multi-class classification tasks

The implementation uses `MLPClassifier` from `scikit-learn`, which supports:
- Multiple hidden layers
- Various solvers (SGD, Adam, LBFGS)
- Regularization and early stopping

## ⚙️ Algorithm Steps

1. Preprocess and normalize dataset  
2. Initialize FFANN model with desired parameters  
3. Train the model on labeled training data  
4. Evaluate performance using accuracy, confusion matrix, etc.

---

# Scikit-learn ile Feedforward Yapay Sinir Ağı (FFANN) Sınıflandırıcısı

Bu repoda, `scikit-learn` kütüphanesi kullanılarak geliştirilmiş bir **Feedforward Yapay Sinir Ağı (FFANN)** sınıflandırıcısı yer almaktadır. FFANN'ler, makine öğrenmesinin temel modellerindendir ve genellikle sınıflandırma ve regresyon gibi denetimli öğrenme görevlerinde kullanılır.

## 📌 Problem Tanımı

Amaç, etiketli verilerle eğitilen bir yapay sinir ağı ile verilen girdilerin ait olduğu sınıfları doğru şekilde tahmin etmektir. Model, tahmin edilen ve gerçek değerler arasındaki hataya göre ağırlıkları güncelleyerek öğrenir.

## 🔍 Yöntem Özeti

Bir **Feedforward Sinir Ağı**, şu katmanlardan oluşur:
- Girdi (input) katmanı  
- Bir veya daha fazla gizli (hidden) katman  
- Çıktı (output) katmanı

Feedforward mimaride:
- Veri yalnızca ileri yönde akar (girdi → çıktı)  
- Döngü (geri besleme) içermez  
- Aktivasyon fonksiyonları (sigmoid, ReLU vb.) sayesinde doğrusal olmayan yapılar öğrenilebilir

### Temel Özellikler:
- Denetimli öğrenme algoritmasıdır  
- Geri yayılım (backpropagation) ve gradyan inişi ile eğitilir  
- Çok sınıflı sınıflandırma problemleri için uygundur

Uygulamada `scikit-learn` kütüphanesinden `MLPClassifier` kullanılmıştır. Bu sınıf:
- Çok katmanlı yapıları destekler  
- Farklı çözümleyiciler (SGD, Adam, LBFGS) ile çalışabilir  
- Regularizasyon ve erken durdurma (early stopping) özellikleri içerir

## ⚙️ Algoritma Adımları

1. Veri kümesi ön işleme ve normalleştirme yapılır  
2. FFANN modeli istenilen parametrelerle başlatılır  
3. Model etiketli verilerle eğitilir  
4. Performans değerlendirmesi (doğruluk, karmaşıklık matrisi vb.) yapılır
```
