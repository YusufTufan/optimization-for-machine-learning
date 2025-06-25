import  numpy as np
import math
from dataSpiral import ti,yi
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------
# Eleman bazlı exp hesaplayan fonksiyon
def exp(x):
    return np.array([math.exp(i) for i in x])
#-----------------------------------------------------------------------------
# Tanh aktivasyon fonksiyonu (hem float hem array için)
def tanh(x):
    if isinstance(x, float):
        result = (math.exp(x)-math.exp(-x))/(math.exp(x)+math.exp(-x))
    else:
        result = ((np.array(exp(x))-np.array(exp(-x)))/(np.array(exp(x))+np.array(exp(-x)))).reshape(-1, 1)
    return result
#------------------------------------------------------------------------------
# MISO-YSA model çıktısı hesaplanıyor (tek çıkışlı yapay sinir ağı modeli)
def MISOYSAmodelIO(ti,Wg,bh,Wc,bc):
    S = Wg.shape[0]
    yhat = []
    for t in ti:
        t = t.reshape(-1,1)
        nn = Wc.dot(tanh(Wg.dot(t)+bh))+bc
        yhat.append(nn[0][0])
    return yhat
#------------------------------------------------------------------------------
# Gerçek çıkış ile tahmin edilen çıkış arasındaki hata
def error(Wg,bh,Wc,bc,ti,yi):
    yhat = MISOYSAmodelIO(ti,Wg,bh,Wc,bc)
    return np.array(yi) - np.array(yhat)
#------------------------------------------------------------------------------
# Jacobian matrisinin hesaplandığı fonksiyon (Levenberg-Marquardt için)
def findJacobian(traininginput,Wg,bh,Wc,bc):
    R = traininginput.shape[1]
    S = Wg.shape[0]
    numofdata = len(traininginput)
    J = np.matrix(np.zeros((numofdata, S*(R+2)+1)))
    for i in range(0,numofdata):
        for j in range(0,S*R):
            k = np.mod(j,S)
            n = int(j/S)
            J[i,j] = -Wc[0,k]*traininginput[i,n]*(1-tanh(Wg[k,:].dot(traininginput[i])+bh[k])**2)  
        for j in range(S*R,S*R+S):
            J[i,j] = -Wc[0,j-S*R]*(1-tanh(Wg[j-S*R,:].dot(traininginput[i])+bh[j-S*R])**2)
        for j in range(S*R+S, S*(R+2)):
            J[i,j] = -tanh(Wg[j-(R+1)*S,:].dot(traininginput[i])+bh[j-(R+1)*S])
        J[i,S*(R+2)] = -1
    return J
#------------------------------------------------------------------------------
# Ağırlık ve biasları vektör haline getirir (optimizasyon için)
def Matrix2Vector(Wg,bh,Wc,bc):
    x = np.array([],dtype=float).reshape(0,1)
    for i in range(0,Wg.shape[1]):
        x = np.vstack((x,Wg[:,i].reshape(-1,1)))
    x =  np.vstack((x,bh.reshape(-1,1)))
    x =  np.vstack((x,Wc.reshape(-1,1))) 
    x =  np.vstack((x,bc.reshape(-1,1))) 
    x = x.reshape(-1,)
    return x
#------------------------------------------------------------------------------
# Vektörü tekrar matris formuna çevirir
def Vector2Matrix(z,S,R):
    Wgz = np.array([],dtype=float).reshape(S,0)
    for i in range(0,R):
        T = (z[i*S:(i+1)*S]).reshape(-1,1)
        Wgz = np.hstack((Wgz,T))
    bhz = (z[R*S:S*(R+1)]).reshape(S,1)
    Wcz = (z[S*(R+1):S*(R+2)]).reshape(1,S)
    bcz = (z[S*(R+2)]).reshape(1,1)  
    return Wgz,bhz,Wcz,bcz
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# Eğitim ve doğrulama veri indekslerinin ayrılması
trainingindices = np.arange(0,len(ti),2)
traininginput = np.array(ti)[trainingindices]
trainingoutput = np.array(yi)[trainingindices]
validationindices = np.arange(1,len(ti),2)
validationinput = np.array(ti)[validationindices]
validationoutput = np.array(yi)[validationindices]       
    
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Levenberg-Marquardt parametrelerinin tanımı
MaxIter = 500
epsilon1 = 1e-9
epsilon2 = 1e-9
epsilon3 = 1e-9
mumax = 1e99
R = ti.shape[1]
#------------------------------------------------------------------------------
# Gizli katman boyutu (manuel tanımlanmış)
S = 50
#Wg = np.random.random((S,R)) - 0.5
#bh = np.random.random((S,1)) - 0.5
#Wc = np.random.random((1,S)) - 0.5        
#bc = np.random.random((1,1)) - 0.5  

# Ağ başlangıç ağırlıklarının manuel olarak atanması
Wg = np.array([[0.5, -1], [1.2, 0.3]])
bh = np.array([[0.0], [0.1]])
Wc = np.array([[10, -0.5]])
bc = np.array([[0.2]])

S = Wg.shape[0]  # Bu gerekli çünkü S değişkeni aşağıda kullanılıyor    
# İlk parametre vektörü oluşturuluyor
xk = Matrix2Vector(Wg,bh,Wc,bc)  
k = 0; C1 = True; C2 = True; C3 = True; C4 = True; fvalidationBest = 1e99; kbest = 0

# Başlangıç eğitim hatası hesaplanıyor
ek = error(Wg,bh,Wc,bc,traininginput,trainingoutput) 
ftraining = sum(ek**2)
FTRA = [math.log10(ftraining)]
evalidation = error(Wg,bh,Wc,bc,traininginput,trainingoutput)
fvalidation = sum(evalidation**2)
FVAL = [math.log10(fvalidation)]
ITERATION = [k]
print('k:',k,'f',format(ftraining,'f'))
mu = 1; muscal= 10; I = np.identity(S*(R+2)+1)
# Levenberg-Marquardt algoritması döngüsü başlatılıyor
while C1 & C2 & C3 & C4:
# Başlangıç eğitim hatası hesaplanıyor
    ek = error(Wg,bh,Wc,bc,traininginput,trainingoutput)
    Jk = findJacobian(traininginput,Wg,bh,Wc,bc)
    gk = np.array(2*Jk.transpose().dot(ek)).reshape(-1)
    Hk = 2*Jk.transpose().dot(Jk) + 1e-8*I
    Hk = np.array(Hk, dtype=np.float64)
    I = np.identity(Hk.shape[0], dtype=np.float64)
    ftraining = sum(ek**2)
    sk = 1
    loop = True
    while loop:
        zk = -np.linalg.inv(Hk+mu*I).dot(gk)
        zk = np.array(zk).flatten()
        z = xk + zk
        Wgz,bhz,Wcz,bcz = Vector2Matrix(z,S,R)
        ez = error(Wgz,bhz,Wcz,bcz,traininginput,trainingoutput)
        fz = sum(ez**2)
        if fz<ftraining:
            pk = 1*zk
            mu = mu/muscal
            k += 1
            xk = xk + sk*pk
            Wg = Wgz; bh = bhz; Wc = Wcz; bc= bcz;
            loop = False;
            print('k:',k,'ftre',format(fz,'f'),'fval', format(fvalidation,'f'),'fval*',format(fvalidationBest,'f'))
        else:
            mu = mu*muscal
            if mu>mumax:
                loop = False
                C2 = False
    evalidation = error(Wg,bh,Wc,bc,validationinput,validationoutput)
    fvalidation = sum(evalidation**2)
    if fvalidation< fvalidationBest:
        fvalidationBest = 1* fvalidation
        xkbest = 1*xk
        kbest =1*k
    FTRA.append(math.log10(ftraining))
    FVAL.append(math.log10(fvalidation))
    ITERATION.append(k) 
#------------------------------------------------------------------------------
    C1 = k<MaxIter
    C2 = epsilon1<abs(ftraining-fz)
    C3 = epsilon2<np.linalg.norm(sk*pk)
    C4 = epsilon3<np.linalg.norm(gk)
#------------------------------------------------------------------------------
# Algoritmanın hangi koşulda durduğunu yazdırır
if not C1:
    print('max. iterasyona ulaşıldı.')
if not C2:
    print('fonksiyonun değeri değişmiyor.')
if not C3:
    print('ilerleme yönü bulunamıyor.')
if not C4:
    print('gradyant sıfıra çok yakın')
#------------------------------------------------------------------------------
# Eğitim ve doğrulama hatalarının logaritmik grafiği çiziliyor
plt.plot(ITERATION, FTRA, color='green', linestyle='solid', linewidth=1)
# Eğitim ve doğrulama hatalarının logaritmik grafiği çiziliyor
plt.plot(ITERATION, FVAL, color='red', linestyle='solid', linewidth=1)
plt.axvline(x =kbest, color='b', linestyle='dashed', linewidth=1)
plt.xlabel('iterasyon')
plt.ylabel('performanslar')
plt.title('performanslar',fontstyle='italic')
plt.grid(color ='green', linestyle='--', linewidth=0.1)
plt.legend(['training', 'validation'])
plt.show()
#------------------------------------------------------------------------------
# En iyi bulunan model parametreleri ile tahmin yapılıyor
Wgbest,bhbest,Wcbest,bcbest = Vector2Matrix(xkbest,S,R)
yhat = MISOYSAmodelIO(validationinput,Wgbest,bhbest,Wcbest,bcbest)
TP = 0; TN = 0; FP = 0; FN = 0;
for i in range(0,len(validationinput)):
    if validationinput[i].any() > 0:
        if yhat[i] > 0:
            TP += 1
        else:  
            FP += 1
    else:
        if yhat[i] < 0: 
            TN += 1
        else: 
            FN += 1
# Doğruluk, hassasiyet, geri çağırma ve F1 skoru hesaplanıyor
Accuracy = (TP+TN)/(TP+TN+FP+FN)
Precision = TP/(TP+FP)
Recall = TP/(TP+FN)
Fiscore = (2*Recall*Precision)/(Recall+Precision)
#------------------------------------------------------------------------------       
# Sınıflandırma sınırlarının çizimi için grid oluşturuluyor
T = []
xaxis = np.arange(min(ti[:,0]),max(ti[:,0]),abs(max(ti[:,0])-min(ti[:,0]))/400)
yaxis = np.arange(min(ti[:,1]),max(ti[:,1]),abs(max(ti[:,1])-min(ti[:,1]))/400)
for xp in xaxis:
    for yp in yaxis:
        T.append([xp,yp])
T = np.array(T)
yhat = MISOYSAmodelIO(T,Wgbest,bhbest,Wcbest,bcbest)
Iminus = np.nonzero(np.array(yhat)<0)[0]
Iplus = np.nonzero(np.array(yhat)>0)[0]
# Sınıflandırma yüzeyi ve veri noktaları çiziliyor
plt.scatter(T[Iminus,0],T[Iminus,1], color='r', s=3, marker='s', alpha=0.01 )   
plt.scatter(T[Iplus,0],T[Iplus,1], color='g', s=3, marker='s', alpha=0.01 )  

Iminus = np.nonzero(np.array(yi)<0)[0]
Iplus = np.nonzero(np.array(yi)>0)[0]
plt.scatter(ti[Iminus,0],ti[Iminus,1], color='g', s=1, marker='o', alpha=0.99 )   
plt.scatter(ti[Iplus,0],ti[Iplus,1], color='r', s=1, marker='x', alpha=0.99 ) 

plt.xlabel('$ÖLÇÜM_1$')
plt.ylabel('$ÖLÇÜM_2$')
title = 'VSA Modeli' + ' | TP:' + str(TP) + ' | TN:' + str(TN) + ' | FP:' + str(FP) + ' | FN:' + str(FN)    
confmat = ' | Recall:' + str(Recall) + ' | Precision:' + str(Precision) + ' | Accuracy:' + str(Accuracy) + ' | Fiscore:' + str(Fiscore)
plt.title(title+confmat,fontstyle='italic',fontsize=8)
plt.grid(color = 'green', linestyle = '--',linewidth = 0.1)
plt.show()
#------------------------------------------------------------------------------

            
            