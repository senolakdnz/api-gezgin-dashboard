import requests
import os
from dotenv import load_dotenv

load_dotenv()  # .env dosyasını yükle

planlanan_rotalar = []

def get_weather_data(city, api_key):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            print(f"--- {city} Icin Hava Durumu ---")
            print(f"Sicaklik: {data['main']['temp']}°C")
            print(f"Hissedilen Sicaklik: {data['main']['feels_like']}°C")
            print(f"Nem Orani: %{data['main']['humidity']}")
            print(f"Durum: {data['weather'][0]['description']}".title())
            return True
        elif response.status_code == 404:
            print("Veri bulunamadi. Lutfen sehir adini kontrol edin.")
            return False
        else:
            print(f"API Hatasi: {data.get('message')}")
            return False
        
    except requests.exceptions.ConnectionError:
        print("Baglanti hatasi. Lutfen internet baglantinizi kontrol edin.")
        return False


def add_to_travelList(city):
    url="https://jsonplaceholder.typicode.com/posts"
    kargo = {
        "title": "Yeni Seyahat Rotasi",
        "body": f"{city} icin seyahat planlama basariyla eklendi.",
        "userId": 1
    }

    try:
        response = requests.post(url, json=kargo)
        if response.status_code == 201:
            print(f"{city} icin seyahat planlamasi basariyla eklendi.")
            print(f"Sunucu Onay Kodu: {response.status_code} (Olusturuldu) | Kayit ID: {response.json()['id']}")
            planlanan_rotalar.append(city.strip().capitalize())
    except Exception as e:
        print(f"Veri ekleme hatasi: {e}")

def get_travelList():
    print("--- SEYAHAT PLANLAMA LİSTEMİZ ---")

    if not planlanan_rotalar:
        print("Henüz planlanmis bir seyahat rotaniz bulunmuyor. Önce sehir ekleyin!")
        return

    for sira, sehir_ismi in enumerate(planlanan_rotalar, 1):
        print(f"{sira}. Rota: {sehir_ismi.upper()}")
        print(f"   Aciklama: {sehir_ismi} seyahat planlama listeme basariyla eklendi.")
        print("-" * 30)

def remove_from_travelList(city):
    rota_id=1
    url = f"https://jsonplaceholder.typicode.com/posts/{rota_id}"
    sehir_uyumlu = city.strip().lower()
    bulunan_sehir = None

    for r in planlanan_rotalar:
        if r.lower() == sehir_uyumlu:
            bulunan_sehir = r
            break
    
    if not bulunan_sehir:
        print(f"{city} listede bulunamadi. Lutfen dogru sehir adini giriniz.")
        return
    
    try:
        response =requests.delete(url)
        if response.status_code in [200,202,204]:
            planlanan_rotalar.remove(bulunan_sehir)
            print(f"{bulunan_sehir} listeden basariyla silindi.")
            print(f"Sunucu Onay Kodu: {response.status_code} (Silindi)")
        else:
            print(f"Silme hatasi: Sunucu onay kodu {response.status_code}")
    except Exception as e:
        print(f"Veri silme hatasi: {e}")

def main():
    API_KEY = os.getenv("WEATHER_API_KEY")

    if not API_KEY:
        print("API anahtari bulunamadi. Lutfen .env dosyasini kontrol edin.")
        return
    print("--- HOS GELDINIZ ---")
    while True:
        secilen_sehir = input("Lutfen sehir adini giriniz (Cikis icin 'q' tusuna basin. Rota Listelemek Icin 'l' tusuna basin. Silmek Icin 's' tusuna basin. ): ").strip()
        if secilen_sehir.lower() == 'q':
            print("Programdan cikiliyor...")
            break
        if secilen_sehir.lower() == 'l':
            get_travelList()
            continue
        if secilen_sehir.lower() == 's':
            silinecek_sehir = input("Lutfen silmek istediginiz sehir adini giriniz: ").strip()
            if silinecek_sehir:
                remove_from_travelList(silinecek_sehir)
            continue
        if not secilen_sehir:
            print("Lutfen gecerli bir sehir adi giriniz.")
            continue
        basarili_Mi = get_weather_data(secilen_sehir, API_KEY)
        if basarili_Mi:
            cevap = input(f"{secilen_sehir} icin seyahat planlamasi yapmak ister misiniz? (E/H): ").strip().lower()
            if cevap == 'e':
                add_to_travelList(secilen_sehir)
            elif cevap == 'h':
                print("Seyahat planlamasi yapilmadi.")
            else:
                print("Gecersiz secim. Lutfen 'E' veya 'H' giriniz.")

if __name__ == "__main__":  
    main()
