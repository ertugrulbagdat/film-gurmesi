# 🎬 IMDb Top 1000 Film Öneri Asistanı

Bu Python projesi, Pandas kütüphanesi kullanarak IMDb'nin en iyi 1000 filminin verilerini çeker, temizler ve kullanıcıya genel analizler sunmanın yanı sıra, tercih ettiği film türüne göre rastgele ve yüksek puanlı (IMDb > 7.8) bir film önerisinde bulunur.

## 🌟 Özellikler

* **Veri Çekme (ETL):** GitHub'daki güncel IMDb Top 1000 listesini doğrudan URL üzerinden çeker.
* **Veri Temizleme:** Sütun isimlerini Türkçeleştirir (`Series_Title` -> `Film_Adi`), bozuk yıl verilerini temizler ve sayısal formata dönüştürür.
* **Genel Analiz:** Toplam film sayısı, ortalama puan ve en yüksek puanlı 5 filmi listeler.
* **Akıllı Öneri:** Kullanıcının Türkçe girdiği türe göre (Örn: Dram, Suç) İngilizce arama yapar ve yüksek kaliteli (7.8 üzeri) filmler arasından rastgele bir seçim sunar.
* **Kullanıcı Dostu Arayüz:** Terminalde basit, menü tabanlı bir etkileşim sunar.

## 🛠 Kurulum

Projeyi çalıştırmadan önce, Python'ın kurulu olduğundan emin olun. Bu proje sadece popüler **Pandas** kütüphanesini gerektirir.

### Gereksinimler

```bash
pip install pandas
