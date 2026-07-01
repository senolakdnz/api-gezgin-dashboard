import requests

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