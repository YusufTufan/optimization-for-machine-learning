# FFANN Classifier using scikit-learn with custom forward pass
# Dataset: Spiral classification

import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from dataSpiral import ti, yi

# sklearn MLPClassifier ile FFANN modeli oluşturuluyor
ffannmodel = MLPClassifier(
    random_state=2,
    max_iter=500,
    hidden_layer_sizes=20,
    activation='tanh',
    solver='lbfgs',
    learning_rate='adaptive',
    early_stopping=True,
    validation_fraction=0.5
)
ffannmodel.fit(ti, yi)  # modeli eğit

# Manuel forward pass için yardımcı fonksiyonlar
def exp(x):
    return np.array([math.exp(i[0]) for i in x]).reshape(-1, 1)

def tanh(x):
    if isinstance(x, float):
        return (math.exp(x)-math.exp(-x))/(math.exp(x)+math.exp(-x))
    return ((exp(x)-exp(-x))/(exp(x)+exp(-x))).reshape(-1, 1)

# Giriş verisini FFANN'dan geçirerek çıktı üreten fonksiyon
def miso_ysa_io(ti, Wg, bh, Wc, bc, mode):
    yhat = []
    for t in ti:
        t = t.reshape(-1, 1)
        net = Wc.T @ tanh(Wg @ t + bh) + bc
        val = net[0][0]
        if mode == 'regressor':
            yhat.append(val)
        elif mode == 'classifier':
            yhat.append(np.sign(1 / (1 + math.exp(-val)) - 0.5))
    return yhat

# sklearn modelinden ağırlıkları al
Wg = ffannmodel.coefs_[0].T
bh = ffannmodel.coefs_[1].T
Wc = ffannmodel.intercepts_[0].reshape(-1, 1)
bc = ffannmodel.intercepts_[1].reshape(1, 1)

# Model özelliklerini yazdır
print("Loss:", ffannmodel.loss_)
print("Features:", ffannmodel.n_features_in_)
print("Iterations:", ffannmodel.n_iter_)
print("Layers:", ffannmodel.n_layers_)
print("Outputs:", ffannmodel.n_outputs_)
print("Activation:", ffannmodel.out_activation_)

# sklearn ile manuel forward sonucu karşılaştır
structure_test = ffannmodel.predict(ti) - np.array(miso_ysa_io(ti, Wg, bh, Wc, bc, 'classifier'))
print("Structural test error:", np.sum(np.abs(structure_test)))

# Sınıflandırma metriklerini hesapla
TP = TN = FP = FN = 0
yhat = ffannmodel.predict(ti)
for i in range(len(yi)):
    if yi[i] > 0:
        if yhat[i] > 0: TP += 1
        else: FP += 1
    else:
        if yhat[i] < 0: TN += 1
        else: FN += 1

acc = (TP + TN) / (TP + TN + FP + FN)
prec = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = 2 * recall * prec / (recall + prec)

# Karar sınırı çizimi için grid oluştur
xaxis = np.linspace(min(ti[:, 0]), max(ti[:, 0]), 400)
yaxis = np.linspace(min(ti[:, 1]), max(ti[:, 1]), 400)
T = np.array([[x, y] for x in xaxis for y in yaxis])
yhat_grid = ffannmodel.predict(T)

# Sınıflandırma sonuçlarını renklendir
Iminus = np.where(yhat_grid < 0)[0]
Iplus = np.where(yhat_grid > 0)[0]
plt.scatter(T[Iminus, 0], T[Iminus, 1], color='r', s=3, alpha=0.01)
plt.scatter(T[Iplus, 0], T[Iplus, 1], color='g', s=3, alpha=0.01)

# Eğitim verisini çiz
Iminus = np.where(yi < 0)[0]
Iplus = np.where(yi > 0)[0]
plt.scatter(ti[Iminus, 0], ti[Iminus, 1], color='g', s=1, marker='o')
plt.scatter(ti[Iplus, 0], ti[Iplus, 1], color='r', s=1, marker='x')

# Grafik ayarları
plt.xlabel("$ÖLÇÜM_1$")
plt.ylabel("$ÖLÇÜM_2$")
plt.title(f"FFANN | TP:{TP} TN:{TN} FP:{FP} FN:{FN} | Accuracy:{acc:.2f} Precision:{prec:.2f} Recall:{recall:.2f} F1:{f1:.2f}", fontsize=8)
plt.grid(True, linestyle='--', linewidth=0.1)
plt.show()
