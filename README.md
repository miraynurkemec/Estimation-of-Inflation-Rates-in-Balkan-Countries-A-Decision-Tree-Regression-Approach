# Balkan Ülkeleri Enflasyon Tahmini: Karar Ağacı Regresyonu

## Proje Özeti

Bu çalışma, Balkan ülkelerinin enflasyon oranlarını temel makroekonomik göstergelerle tahmin etmeyi amaçlamaktadır. 2021–2023 dönemi çeyreklik verileri ($\text{N=18}$) kullanılarak bir **Karar Ağacı Regresyon modeli** geliştirilmiştir.

Model, yüksek performans metrikleriyle ($\text{R}^2 \approx 0.94$) enflasyonu tahmin etmede başarılı olmuş ve özellikle **Döviz Kuru ($\text{döviz}$)** değişkeninin enflasyon üzerindeki en kritik etken olduğunu ortaya koymuştur.

---

## 📊 Veri Seti ve İstatistikler

Veri seti, 2021-2023 yıllarına ait 18 gözlemden oluşmaktadır.

### Değişkenler (Sütun Bilgileri)

| \# | Sütun | $\text{Dtype}$ | Açıklama |
|---|---|---|---|
| 0 | $\text{year}$ | $\text{int64}$ | Yıl |
| 1 | $\text{paraarzı}$ | $\text{float64}$ | Para Arzı |
| 2 | $\text{faiz}$ | $\text{float64}$ | Faiz Oranı |
| 3 | $\text{döviz}$ | $\text{float64}$ | Döviz Kuru |
| 4 | $\text{güvenendeksi}$ | $\text{float64}$ | Tüketici Güven Endeksi |
| 5 | *Hedef* | $\text{float64}$ | Enflasyon Oranı ($\mathbf{y}$) |

### Önemli İstatistikler

| Metrik | $\text{döviz}$ | $\text{paraarzı}$ | $\text{faiz}$ |
|---|---|---|---|
| $\text{count}$ | $18.00$ | $18.00$ | $18.00$ |
| $\text{mean}$ | $28.42$ | $9.82$ | $5.40$ |
| $\text{std}$ | $40.98$ | $4.94$ | $1.56$ |
| $\text{min}$ | $0.85$ | $2.35$ | $3.20$ |
| $\text{max}$ | $113.04$ | $22.95$ | $9.32$ |

---

##  Korelasyon Analizi

### Görsel: [`korelasyonkarar.png`](korelasyonkarar.png)

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
| Kriter | $\text{squared\_error}$ (Varyans) | Regresyon için standart hata fonksiyonu. |

### 2. Ağaç Yapısı ve Bölünme Kriterleri

### Görsel: [`ikinciagac.png`](ikinciagac.png)

Karar Ağacı analizi, enflasyonu belirlemede değişkenlerin önem sırasını gösterir:

1.  **Kök Düğüm (En Önemli Değişken):**
    -   **Kural:** $\text{döviz} \le 81.047$
    -   **Bilgi Kazancı:** $\mathbf{2.6743}$
    -   *Yorum:* Enflasyonu tahmin etmede ilk ve en güçlü ayrımı **döviz kuru** yapmaktadır.

2.  **En Yüksek Bilgi Kazancı:**
    -   **Bölünme:** Yüksek döviz kuru durumunda ($\text{döviz} > 81.047$) $\text{year} \le 2021.5$ kuralı.
    -   **Kazanç:** $\mathbf{11.9017}$
    -   *Yorum:* Yüksek kur rejimlerinde, **zaman faktörünün** (yılın) enflasyon üzerindeki etkisi *diğer tüm bölmelerden* çok daha kritiktir.

---

## Kullanılan Teknolojiler

-   `Python`
-   `scikit-learn` (Decision Tree Regressor)
-   `pandas`
-   `matplotlib` / `seaborn`

---

## Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına bakabilirsiniz.
