#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 16 20:40:21 2025

@author: miray
"""
# Gerekli kütüphaneler
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor, plot_tree  # Karar ağacı regresyon modeli ve görselleştirme fonksiyonu
from sklearn.model_selection import train_test_split  # Eğitim/test verisi bölme
import matplotlib.pyplot as plt  # Görselleştirme için
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, explained_variance_score #gerekli metrikler


# Excel dosyasını oku
# Veri seti Excel dosyasından read_excel() fonksiyonu ile yüklenmiştir.
# Bu dosya içinde enflasyon tahmini için kullanılacak ekonomik veriler yer almaktadır.
df = pd.read_excel("/Users/miray/Desktop/miraydataset.xlsx")

# Özellikler (X) ve hedef değişken (y) tanımla
X = df.drop(columns=["enflasyon", "country"])  # Sayısal özellikler
y = df["enflasyon"]  # Tahmin etmek istediğimiz değişken

# Veri setini DataFrame formatında inceleme
df_X = pd.DataFrame(X, columns=X.columns)
# X verisindeki sütunları kullanarak yeni bir pandas DataFrame oluşturulur
# bu adım veri analizi sırasında daha okunabilir bir yapı sağlar
print("Veri setindeki ilk 5 kayıt:")
print(df_X.head())
# df_X.head() fonksiyonu, veri setinin ilk 5 satırını ekrana yazdırır
# veri yapısını ve içerikleri hızlıca görmek için kullanılır

print("\nVeri setindeki sütun bilgileri:")
print(df_X.info())
# df_X.info() fonksiyonu, sütun adları, veri tipleri ve eksik veri durumu gibi bilgileri gösterir
# her sütunun kaç tane boş (null) değeri olduğu da burada görülebilir

print("\nİstatistiksel bilgiler:")
print(df_X.describe())
# df_X.describe() fonksiyonu, sayısal sütunlara ait temel istatistikleri verir
# ortalama, standart sapma, min-max ve çeyreklik değerler bu çıktıda yer alır


# 2. Veriyi eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# test_size=0.33, verilerin %33’ünün test, %67’sinin eğitim için kullanılacağını belirtir
# y_train ve X_train modelin öğrenmesi için; y_test ve X_test modeli test etmek için kullanılır
# random_state=42 yazılması, verinin her çalıştırmada aynı şekilde bölünmesini sağlar (sonuçların tekrarlanabilirliği için önemlidir)

# 3. Karar ağacı modelini oluşturma ve eğitme
clf = DecisionTreeRegressor(random_state=42)  # Modelin kararlı olması için random_state
clf = clf.fit(X_train, y_train)  # Modeli eğitim verileriyle eğit
#criterion değeri	Açıklaması
#'squared_error'	Ortalama Kare Hata (Mean Squared Error) — default -  Outlier'lara karşı duyarlıdır 
#'friedman_mse'	Friedman’ın geliştirdiği varyasyonlu hata — özellikle Gradient Boosted Trees için- Outlier'lara karşı dayanıklı 
#'absolute_error'	Ortalama Mutlak Hata (Mean Absolute Error) — daha az sapmalara duyarlı
#'poisson'	Poisson regresyonu — sayma verileri için

# 4. Test seti ile modelin doğruluğunu ölç
y_pred = clf.predict(X_test)
# test verileri X_test kullanılarak modelden tahminler alınır
# y_pred, modelin enflasyon için yaptığı tahmin değerlerini içerir
# Modelin doğruluğunu ölçen metrikler
mse = mean_squared_error(y_test, y_pred)
# ortalama kare hata (Mean Squared Error): gerçek ve tahmin değerleri arasındaki farkların karelerinin ortalamasıdır
# hata büyüklüğünü verir, küçük olması istenir
rmse = mse ** 0.5  # Root Mean Squared Error
# ortalama kare hatanın karekökü alınarak hata değeri daha anlaşılır bir ölçeğe getirilir
# birimi doğrudan hedef değişken (enflasyon) ile aynı olur
mae = mean_absolute_error(y_test, y_pred)
# ortalama mutlak hata: her bir tahminin gerçek değerden ortalama ne kadar saptığını gösterir
# mutlak farkların ortalamasıdır, yorumlaması kolaydır
r2 = r2_score(y_test, y_pred)
# R-kare skoru: modelin verideki toplam değişkenliği ne kadar açıkladığını gösterir
# 1'e yakınsa model iyi, 0’a yakınsa kötü tahmin yapıyordur
explained_variance = explained_variance_score(y_test, y_pred)
# açıklanan varyans skoru: modelin ne kadar varyansı başarılı şekilde açıkladığını ölçer
# R^2’ye benzer ama daha az cezalandırıcıdır; 1’e yakınsa model güçlüdür
# Sonuçları yazdır

print(f"\nİlk Model - Mean Squared Error (MSE): {mse:.2f}")
print(f"İlk Model - Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"İlk Model - Mean Absolute Error (MAE): {mae:.2f}")
print(f"İlk Model - R^2 Skoru: {r2:.2f}")
print(f"İlk Model - Explained Variance Score: {explained_variance:.2f}")


# 5. Karar ağacını görselleştirme
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=X.columns, rounded=True)
plt.title("Karar Ağacı (Regresyon) - Miray Dataset")
plt.show()

# 6. Modelin hiperparametrelerini sınırlama
clf = DecisionTreeRegressor(
    random_state=42,
    max_depth=5,  # Karar ağacının maksimum derinliği 5 ile sınırlandırılıyor.
#Bu, modelin aşırı karmaşık hale gelmesini ve aşırı öğrenmesini (overfitting) engeller.
    min_samples_split=4,  # Bir iç düğümün daha küçük alt düğümlere bölünebilmesi için en az 4 veri örneği olması gerekir.
#Bu sayede ağaç, çok küçük örneklerle bölünme yapmaz.
    min_samples_leaf=2,  # Her yaprakta en az 2 örnek olması şartı getirilmiştir.
#Bu da yine modelin genelleme yeteneğini artırır.
    max_features='sqrt'  # Her düğümde bölme yaparken kullanılacak maksimum özellik sayısını √(toplam özellik sayısı) olarak sınırlar.
#Bu, özellikle çok sayıda özelliğin olduğu durumlarda ağacın daha dengeli ve hızlı çalışmasını sağlar. 
)


#Bir karar ağacı, kökten (başlangıç düğümü) başlayarak veriyi dallara ayırır. 
#Bu ayrımların her bir seviyesi bir derinlik seviyesi olarak kabul edilir.
#Kök düğüm (root node) → Derinlik: 0
#İlk ayrım (ilk split) → Derinlik: 1
#İkinci ayrım → Derinlik: 2

# Modeli tekrar eğitelim
clf = clf.fit(X_train, y_train)

# 7. Test setiyle modelin doğruluğunu ölçme
y_pred = clf.predict(X_test)
# Modelin doğruluğunu ölçen metrikler
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5  # Root Mean Squared Error
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
explained_variance = explained_variance_score(y_test, y_pred)

# Sonuçları yazdır
print(f"\nİlk Model - Mean Squared Error (MSE): {mse:.2f}")
print(f"İlk Model - Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"İlk Model - Mean Absolute Error (MAE): {mae:.2f}")
print(f"İlk Model - R^2 Skoru: {r2:.2f}")
print(f"İlk Model - Explained Variance Score: {explained_variance:.2f}")

# 8. Karar ağacını görselleştirme (Sınırlı Derinlik ve Diğer Parametrelerle)
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=X.columns, rounded=True)
plt.title("Karar Ağacı (Sınırlı Derinlik ve Diğer Parametrelerle) - Miray Dataset")
plt.show()

# 9. Her düğümdeki varyans (impurity) değerlerini yazdır
print(f"\nModelde kullanılan kriter: {clf.criterion}")
#Yani her bir bölünmede, ortalama karesel hata (Mean Squared Error - MSE) en aza indirilmeye çalışılıyor.
#Ağaç, her bir düğümde veriyi ikiye ayırırken hangi bölmenin toplam hatayı (mse'yi) en çok azaltacağını hesaplıyor.
print("\nHer düğümdeki impurity (Varyans):")
print(clf.tree_.impurity)

#Daha düşük bir varyans, verilerin daha homojen olduğunu ve modelin bu düğümde daha iyi bir tahmin yapabileceğini gösterir. 
#Daha yüksek bir varyans, düğümde daha fazla belirsizlik olduğunu ve modelin bu düğümde daha fazla hata yapma potansiyeline sahip olduğunu gösterir.
#Düşük Varyans Değerleri: Örneğin, -3.63797881e-12 veya 0.00000000e+00 gibi sıfır ya da sıfıra yakın değerler, bu düğümlerin neredeyse homojen olduğunu ve modelin bu noktada güçlü bir tahmin yaptığını gösterir. 
#Bu, bölme işleminin iyi sonuç verdiğini ve o bölgedeki verilerin çok fazla çeşitliliğe sahip olmadığını gösterir.
#Yüksek Varyans Değerleri: Örneğin, 1.93210000e+02 gibi yüksek varyanslar, bu düğümlerin daha heterojen (farklı) veriler içerdiğini ve modelin burada daha fazla hata yapma potansiyeline sahip olduğunu gösterir. 
#Düğüm Derinliği: Varyans değerlerinin genellikle azalma eğiliminde olduğunu görüyorsanız, bu, ağacın her seviyesinde daha homojen veriler elde edildiğini ve ağacın doğru bir şekilde dallandığını gösterebilir. 
#Ancak, bazı düğümlerde hala yüksek varyanslar görüyorsanız, modelin aşırı uydurma yapıyor olabileceğini veya daha fazla veri noktasıyla daha iyi genel bir model oluşturulması gerektiğini düşünebilirsiniz.
# 10. Her düğümde hangi özellik kullanılmış onu yazdır
print("\nHer düğümdeki özellik indeksleri (split feature):")
print(clf.tree_.feature)

#Örneğin, ilk düğümde özellik 5 seçilmiş, yani model bu özelliği kullanarak veriyi bölmüş. 
#Sonraki düğümde, özellik 10 veya 0 seçilmiş olabilir. Bu, modelin önceki düğümlerde hangi özelliklerin daha fazla bilgi sunduğunu ve veri setini daha iyi böldüğünü gösterir.
#Yaprak Düğümler: -2 değeri, düğümde daha fazla bölme yapılmadığını, yani o düğümün yaprak düğüm olduğunu ifade eder. Yaprak düğümlerde model, verilere dayanarak tahminler yapar. Eğer çok fazla -2 değeri görüyorsanız, bu, modelin derinliğinin arttığını ve birçok yaprak düğüm bulunduğunu gösterir.
#Örneğin, 12. özellik birkaç kez kullanılmış (örneğin, 2., 10. ve 20. düğümler), bu, bu özelliğin model için önemli olduğunu ve veriyi doğru bir şekilde bölmede önemli bir rol oynadığını gösterir.
# 11. Her düğümdeki bilgi kazancı hesaplaması
print("\nHer düğümdeki Bilgi Kazancı:")
for node in range(clf.tree_.node_count):
    if clf.tree_.children_left[node] != clf.tree_.children_right[node]:
        impurity_before = clf.tree_.impurity[node]
        impurity_left = clf.tree_.impurity[clf.tree_.children_left[node]]                          
        impurity_right = clf.tree_.impurity[clf.tree_.children_right[node]]

        n_samples_left = clf.tree_.n_node_samples[clf.tree_.children_left[node]]
        n_samples_right = clf.tree_.n_node_samples[clf.tree_.children_right[node]]

        weighted_impurity = (n_samples_left / (n_samples_left + n_samples_right)) * impurity_left + \
                            (n_samples_right / (n_samples_left + n_samples_right)) * impurity_right
        information_gain = impurity_before - weighted_impurity

        print(f"Düğüm {node}: Bilgi Kazancı = {information_gain:.4f}")
        
        # Gerçek ve Tahmin Edilen Değerlerin Çizgi Grafiği
import matplotlib.pyplot as plt
import numpy as np

# y_test: Gerçek değerler
# y_pred: Modelin tahmin ettiği değerler

plt.figure(figsize=(10, 6))
plt.plot(np.arange(len(y_test)), y_test, label='Gerçek Değerler', linestyle='-', marker='o')
plt.plot(np.arange(len(y_pred)), y_pred, label='Tahmin Edilen Değerler', linestyle='--', marker='x')
plt.title('Gerçek vs Tahmin Edilen Enflasyon Değerleri')
plt.xlabel('Gözlem Sırası')
plt.ylabel('Enflasyon Oranı')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Excel dosyasını oku
df = pd.read_excel("/Users/miray/Desktop/miraydataset.xlsx")

# 'year' sütununu ve sayısal olmayan sütunları çıkar
df_corr = df.drop(columns=["year"])
df_corr = df_corr.select_dtypes(include=["number"])  # sadece sayısal veriler kalsın

# Korelasyon matrisini oluştur
corr_matrix = df_corr.corr()

# Korelasyon matrisini görselleştir
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", square=True)
plt.title("Değişkenler Arası Korelasyon Matrisi (Yalnızca Sayısal Veriler)")
plt.tight_layout()
plt.show()

        
