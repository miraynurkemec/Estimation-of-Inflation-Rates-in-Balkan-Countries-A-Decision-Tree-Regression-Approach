# 📉 Balkan Ülkeleri Enflasyon Tahmini: Karar Ağacı Regresyonu

## 🌟 Proje Özeti

Bu çalışma, Balkan ülkelerinin enflasyon oranlarını temel makroekonomik göstergelerle tahmin etmeyi amaçlamaktadır. 2021–2023 dönemi çeyreklik verileri ($\text{N=18}$) kullanılarak bir **Karar Ağacı Regresyon modeli** geliştirilmiştir.

Model, yüksek performans metrikleriyle ($\text{R}^2 \approx 0.94$) enflasyonu tahmin etmede başarılı olmuş ve özellikle **Döviz Kuru ($\text{döviz}$)** değişkeninin enflasyon üzerindeki en kritik etken olduğunu ortaya koymuştur.

---

## 🔗 Korelasyon Analizi

### Görsel: Değişkenler Arası Korelasyon Matrisi
<img width="676" height="590" alt="image" src="https://github.com/user-attachments/assets/baff72dc-911c-45db-a7df-2a2317b7e285" />

Korelasyon matrisi, tahmin edilen değişken ($\text{enflasyon}$) ile diğer değişkenler arasındaki ilişkileri gösterir:

- $\text{enflasyon}$ ile en güçlü ilişki: **Döviz** ($\mathbf{-0.26}$) ve **Güven Endeksi** ($\mathbf{-0.19}$), her ikisi de negatif yönlüdür.
- Veri setindeki en güçlü ilişki **Para Arzı** ve **Döviz** arasındadır ($\mathbf{-0.57}$).

---

##  Karar Ağacı Model Sonuçları

### 1. Performans Metrikleri

Model, son derece yüksek tahmin gücüne sahiptir.

| Metrik | Değer | Yorum |
|---|---|---|
| $\mathbf{R^2\ Skoru}$ | $\mathbf{0.94}$ | Varyansın %94'ü model tarafından açıklanmaktadır. **Mükemmel uyum.** |
| $\text{RMSE}$ | $1.20$ | Ortalama tahmin hatası düşüktür. |
| $\text{MSE}$ | $1.44$ | Düşük hata karesi ortalaması. |

### 2. Ağaç Yapısı ve Bölünme Kriterleri

### Görsel: Karar Ağacı Yapısı
<img width="950" height="657" alt="image" src="https://github.com/user-attachments/assets/ff0e5080-a7ed-46ad-9e0d-6fbea3eb1fb4" />

-   **Kök Düğüm (En Önemli Değişken):** **Döviz** ($\text{döviz} \le 81.047$). Enflasyonu tahmin etmede ilk ve en güçlü ayrımı yapar.
-   **En Yüksek Bilgi Kazancı:** Yüksek döviz kuru durumunda ($\text{döviz} > 81.047$) $\text{year} \le 2021.5$ kuralı ($\mathbf{11.9017}$) ile elde edilmiştir. Bu, yüksek kur rejimlerinde **zaman faktörünün** kritik olduğunu gösterir.

---

## Kullanılan Teknolojiler

-   `Python`
-   `scikit-learn` (Decision Tree Regressor)
-   `pandas`
-   `matplotlib` / `seaborn`

---
