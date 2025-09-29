# Makine Öğrenmesi Dersi 1 - KNN

Bu notebook'ta katıldım bootcampten öğrendiğim bilgiler ışında ve yaptığımız pratikleri paylaşacağım. İlk olarak gözetimli öpğrenme algoritmalarından sınıflandırma kısmından başlıyorum. İlk algoritmamız K-En Yakın Komşu (KNN) algoritmaası. Bu projede iki problem çözdüm: meme kanseri teşhisi ve fonksiyon tahmini.

## 🎯 Ne Yaptım?

### 1. Meme Kanseri Teşhisi
Wisconsin Breast Cancer veri setini kullandım. 30 farklı özellik var (hücre çapı, doku kalınlığı gibi). Hücrelerin iyi huylu mu kötü huylu mu olduğunu tahmin etmeye çalıştım.

### 2. Fonksiyon Tahmini
Sinüs fonksiyonu verisi oluşturdum ve gürültü ekledim. KNN'in bu gürültülü verilerden orijinal fonksiyonu ne kadar iyi tahmin edebileceğini test ettim.

İki ağırlık stratejisi denedim: Uniform (eşit ağırlık) ve Distance (yakın komşular daha etkili).

## 🛠️ Kullandığım Araçlar

Python kütüphaneleri: Pandas (veri düzenleme), NumPy (hesaplamalar), Scikit-learn (KNN algoritması), Matplotlib (görselleştirme).

## 📊 Sonuçlar

### Meme Kanseri Teşhisi
K=3 ile başladım, **%95.9 doğruluk** aldım. 100 hastadan 96'sını doğru teşhis ettim.

**Hata analizi**: İyi huylu 59 doğru, 3 yanlış. Kötü huylu 105 doğru, 4 yanlış. Yanlış teşhisler çoğunlukla "güvenli tarafta" - yani iyi huylu olanları kötü huylu olarak teşhis etmek.

**K değeri optimizasyonu**: K=1'den K=20'ye kadar test ettim. **K=9 en iyi performansı** verdi.

<img width="621" height="468" alt="image" src="https://github.com/user-attachments/assets/cba76a63-f487-4bb5-b6c8-015b006f3a88" />


### Fonksiyon Tahmini
Distance weights daha düzgün sonuçlar verdi. Uniform weights sert tahminler yaparken, distance weights gerçek fonksiyona çok daha yakın sonuçlar üretti. Gürültülü verilerde bile KNN regresyonu iyi performans gösterdi.

<img width="643" height="487" alt="Ekran görüntüsü 2025-09-29 184634" src="https://github.com/user-attachments/assets/61c3ba00-6509-406a-91f3-d4cb2030023e" />


## Kısacası

KNN algoritması basit ama etkili. En yakın K komşuya bakıp, çoğunluğun sınıfını tahmin ediyor.

**Nasıl çalışır?** Yeni bir veri geldiğinde, ona en yakın K tane komşuyu buluyor. Bu komşuların çoğunluğu hangi sınıftaysa, yeni veri de o sınıfa ait oluyor.

**Önemli detaylar**: Öklid mesafesi kullanıyor. K değeri kritik - çok küçükse gürültüye hassas, çok büyükse detayları kaçırıyor.

**Parametreler**: 
- n_neighbors (K) - kaç komşuya bakacağım
- Weights - komşuları nasıl ağırlıklandıracağım (eşit/mesafeye göre)
- Metric - mesafeyi nasıl hesaplayacağım

**Veri hazırlığı**: StandardScaler çok önemli. Train-test split ile modelin ezberleyip ezberlemediğini test ettim.

