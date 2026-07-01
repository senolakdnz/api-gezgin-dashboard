# 🌍 Gezgin & Kültür Dashboard'u (API Projesi)

Bu proje, modern web geliştirmenin temel taşlarından biri olan **API (Application Programming Interface)** mantığını anlamak, uygulamak ve pekiştirmek amacıyla geliştirilmiş 10 günlük bir eğitim kampının final ürünüdür.

Uygulama, hem harici REST API'lerden veri çekme (**GET**) hem de sunucuya veri gönderme (**POST**) senaryolarını gerçekçi bir şekilde simüle eder.

## 🚀 Özellikler

- **Canlı Hava Durumu (GET):** Kullanıcının girdiği şehir ismine göre [OpenWeatherMap API](https://openweathermap.org/) entegrasyonu üzerinden anlık sıcaklık, gökyüzü durumu ve nem oranını dinamik olarak çeker.
- **Güvenlik ve Kimlik Doğrulama:** Gerçek dünya senaryolarına uygun olarak **API Key** kullanımını barındırır.
- **Hata Yönetimi (Error Handling):** `try-except` blokları sayesinde internet kesintileri veya hatalı şehir girişlerinde uygulamanın çökmesini engeller, kullanıcıya anlamlı uyarılar gösterir.
- **Seyahat Planlama & Listeleme (POST & Yerel Hafıza):** Kullanıcının seyahat etmek istediği şehirleri [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) kullanarak bulut sunucuya gönderir ve başarılı (`201 Created`) yanıtı aldığında yerel hafızaya kaydederek listeler.

## 🛠️ Kullanılan Teknolojiler

- **Programlama Dili:** Python 3
- **Kütüphaneler:** `requests` (HTTP istekleri yönetimi için)
- **Sürüm Kontrol Sistemi:** Git & GitHub

## ⚙️ Kurulum ve Çalıştırma

1. Projeyi bilgisayarınıza klonlayın veya indirin.
2. Terminal üzerinden gerekli kütüphaneyi yükleyin:
   ```bash
   pip install requests