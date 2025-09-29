# knn ile classication problemi çözümü çözümü
# 1 veri seti incelemesi
# 2 Model Seçilmesi
# 3 model train
# 4 sonuç değerlendirmesi
# 5 hiperparametre ayarlaması

import pandas as pd

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)

df.head()

df[target]= cancer.target

df.head()

X = cancer.data # X feature
y = cancer.target # y targets

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  #%30 test  %70 train hem y hem x için bölüyor

#ölçeklendirme preposition
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
#yani büyük sayılı verileri küçük sayılara ölçeklendiriyor 

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5, metric = 'euclidean')
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize = (8,6))
sns.heatmap(cm, annot = True, fmt = 'g')

print(cm)

from sklearn.model_selection import GridSearchCV
knn = KNeighborsClassifier()

param_grid = {'n_neighbors' range(1, 100), 'metric' ['euclidean', 'manhattan', 'minkowski']}

gs = GridSearchCV(knn, param_grid, cv=10)
gs.fit(X_train, y_train)

print(En iyi parametreler, gs.best_params_)
print(En iyi skor, gs.best_score_)

knn_tuned = KNeighborsClassifier(n_neighbors=13, metric='manhattan')
knn_tuned.fit(X_train, y_train)

y_pred_tuned = knn_tuned.predict(X_test)
accuracy_score(y_test, y_pred_tuned)

#REGRESSION
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

plt.style.use('fivethirtyeight')

# Datayı yeniden yarat
X = np.arange(0, 50, 0.1)[, np.newaxis]
y = np.sin(X).ravel()

# Gürültü ekle
noise = 0.8  np.random.randn(len(y))
y[10] += noise[10]

# Sadece 40 veri noktasını kullan
X = X[10]
y = y[10]


# Veriyi görselleştir
# plt.figure(figsize = (8,6))
# plt.scatter(X,y)

# Modelleri eğit ve sonuçları görselleştir
plt.figure(figsize=(10, 8))
# plt.scatter(X, y)
T = np.linspace(0, 5, 500)[, np.newaxis]

for i, weight in enumerate([uniform, distance])
    knn = KNeighborsRegressor(n_neighbors=5, weights=weight)
    y_pred = knn.fit(X,y).predict(T)
    plt.subplot(2,1,i+1)
    plt.scatter(X, y, color = green, label = data)
    plt.plot(T, y_pred, color = red, label = prediction)
    plt.title(K-NN Regressor (weight = {})  Score {.2f}.format(weight, knn.score(X,y)))
    plt.legend()

plt.tight_layout()
plt.show()