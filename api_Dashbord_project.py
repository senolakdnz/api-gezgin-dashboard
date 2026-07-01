import requests

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
            planlanan_rotalar.append(city)
    except Exception as e:
        print(f"Veri ekleme hatasi: {e}")

def get_travelList():
    print("--- SEYAHAT PLANLAMA LİSTEMİZ ---")
    
    # Eğer listemiz boşsa kullanıcıyı bilgilendiriyoruz
    if not planlanan_rotalar:
        print("Henüz planlanmış bir seyahat rotanız bulunmuyor. Önce şehir ekleyin!")
        return
        
    # Listemizde şehirler varsa sadece bizim eklediklerimizi sırayla basıyoruz
    for sira, sehir_ismi in enumerate(planlanan_rotalar, 1):
        print(f"{sira}. Rota: {sehir_ismi.upper()}")
        print(f"   Aciklama: {sehir_ismi} seyahat planlama listeme basariyla eklendi.")
        print("-" * 30)


def main():
    api_key = "08be7741caf616ff4b1d27f4e83b17d5"
    print("--- HOŞ GELDİNİZ ---")
    while True:
        secilen_sehir = input("Lutfen sehir adini giriniz (Cikis icin 'q' tusuna basin. Rota Listelemek Icin 'l' tusuna basin.): ").strip()
        if secilen_sehir.lower() == 'q':
            print("Programdan cikiliyor...")
            break
        if secilen_sehir.lower() == 'l':
            get_travelList()
            continue
        if not secilen_sehir:
            print("Lutfen gecerli bir sehir adi giriniz.")
            continue
        basarili_Mi = get_weather_data(secilen_sehir, api_key)
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