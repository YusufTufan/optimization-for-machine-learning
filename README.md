# Numerical Optimization Techniques for Machine Learning

This repository contains a structured collection of numerical optimization algorithms used in machine learning and mathematical modeling. The materials are based on core concepts covered in numerical methods courses, focusing on **unconstrained optimization**, **nonlinear modeling**, and **curve fitting**.

## 📚 Overview

**Numerical optimization** involves iterative procedures to find optimal solutions when analytical solutions are not possible or practical. It includes both deterministic and approximate methods for:

- Unconstrained optimization  
- Solving nonlinear equations  
- Fitting data to analytical models  
- Gradient-based and derivative-free search methods

These techniques are foundational for machine learning, engineering, and scientific computing.

---

## 📁 Folder Structure and Algorithms

| Folder Name                             | Description                                                                 |
|----------------------------------------|-----------------------------------------------------------------------------|
| `bisection_algorithm/`                 | Bisection method to find minima via root of first derivative               |
| `broydon-fletcher-goldfarb-shanno-algorithm/` | BFGS quasi-Newton algorithm for fast convergence in multivariable optimization |
| `conjugate_gradient_algorithm/`        | Fletcher-Reeves conjugate gradient method                                  |
| `davidon-fletcher-power-algorithm/`    | DFP quasi-Newton method with matrix approximation                          |
| `exponential-model/`                   | Exponential model for nonlinear curve fitting                              |
| `ffann_sklearn_classifier/`            | Feedforward Neural Network classifier using `sklearn`                      |
| `golden_section_algorithm/`           | Golden Section method for univariate optimization                          |
| `gradient_descent_algorithm/`          | Classical gradient descent for multivariate functions                      |
| `gs_steepest_descent_algorithm/`       | Steepest descent with golden section line search                           |
| `hyperbolic-model/`                    | Hyperbolic model for data fitting                                          |
| `levenberg-marquardt-algorithm/`       | LM method for nonlinear least squares fitting                              |
| `levenbergmarquardt_classification.py` | Levenberg–Marquardt adapted for classification tasks                       |
| `modified_newton_algorithm/`           | Modified Newton method for stable optimization                             |
| `newton-raphson-algorithm/`            | Newton–Raphson algorithm for local minimum search                          |
| `polynomial_model/`                    | Polynomial regression model for curve fitting                              |
| `rbf_model/`                           | Radial Basis Function model for nonlinear surface approximation            |

Each folder contains:
- A Python implementation of the algorithm or model  
- A `README.md` explaining the method in detail (with both English & Turkish versions)  
- Sample function definitions (in some folders)

---

## 🧠 Learning Goal

By studying these algorithms, you will gain a solid foundation in how numerical methods are applied in practice to train models, solve equations, and perform optimization in machine learning tasks.


# Makine Öğrenmesi için Sayısal Optimizasyon Teknikleri

Bu depo, makine öğrenmesi ve matematiksel modelleme alanında kullanılan **sayısal optimizasyon algoritmalarının** yapılandırılmış bir koleksiyonunu içerir. İçerikler, sayısal analiz derslerinin temel konularına dayanır ve şu alanlara odaklanır:

- Kısıtsız optimizasyon  
- Doğrusal olmayan denklemlerin çözümü  
- Veriye model uydurma (eğri uydurma)  
- Gradyan tabanlı ve türev gerektirmeyen arama yöntemleri

## 📚 Genel Bakış

**Sayısal optimizasyon**, analitik çözümlerin mümkün olmadığı durumlarda **iteratif** yaklaşımlarla en uygun sonucu bulmayı amaçlar. Bu teknikler:

- Mühendislik sistemlerinde parametre ayarlama  
- Makine öğrenmesinde model eğitimi  
- Deneysel veri analizleri

gibi birçok uygulamada temel rol oynar.

---

## 📁 Klasör Yapısı ve Algoritmalar

| Klasör Adı                              | Açıklama                                                                    |
|----------------------------------------|-----------------------------------------------------------------------------|
| `bisection_algorithm/`                 | Türev kökünden minimum arayan ikiye bölme yöntemi                          |
| `broydon-fletcher-goldfarb-shanno-algorithm/` | Çok değişkenli optimizasyonda kullanılan BFGS yöntemi                      |
| `conjugate_gradient_algorithm/`        | Fletcher-Reeves konjugat gradyan yöntemi                                   |
| `davidon-fletcher-power-algorithm/`    | DFP yöntemi, Hessian matrisi yaklaşımlı                                   |
| `exponential-model/`                   | Doğrusal olmayan üstel eğri uydurma modeli                                 |
| `ffann_sklearn_classifier/`            | `sklearn` ile beslemeli yapay sinir ağı sınıflandırıcısı                   |
| `golden_section_algorithm/`           | Altın oran yöntemi ile tek değişkenli minimum arama                        |
| `gradient_descent_algorithm/`          | Klasik gradyan iniş yöntemi                                                |
| `gs_steepest_descent_algorithm/`       | Altın oran ile birleştirilmiş en dik iniş yöntemi                         |
| `hyperbolic-model/`                    | Hiperbolik fonksiyon ile eğri uydurma modeli                              |
| `levenberg-marquardt-algorithm/`       | Doğrusal olmayan en küçük kareler için LM algoritması                      |
| `levenbergmarquardt_classification.py` | LM yönteminin sınıflandırma uygulaması                                    |
| `modified_newton_algorithm/`           | Kararlılaştırılmış Newton yöntemi                                          |
| `newton-raphson-algorithm/`            | Newton–Raphson algoritması ile lokal minimum arama                        |
| `polynomial_model/`                    | Polinomsal eğri uydurma modeli                                             |
| `rbf_model/`                           | Radyal Tabanlı Fonksiyon (RBF) ile modelleme                               |

Her klasörde:
- İlgili algoritmanın Python kodu  
- Hem İngilizce hem Türkçe detaylı açıklama içeren `README.md`  
- (Bazı klasörlerde) örnek fonksiyonlar ve çağrımlar bulunur

---

## 🧠 Öğrenme Amacı

Bu algoritmaları inceleyerek, makine öğrenmesi, veri bilimi ve mühendislik uygulamalarında **sayısal yöntemlerin nasıl kullanıldığını** anlamış olacaksınız.
