import requests


def get_usd_rate() -> float | None:
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            for item in data:
                if item.get("cc") == "USD":
                    return item.get("rate")
            print("Курс USD не знайдено у відповіді.")
            return None
        else:
            print(f"Помилка сервера. Код відповіді: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Помилка підключення до API НБУ: {e}")
        return None


if __name__ == "__main__":
    usd_rate = get_usd_rate()

    if usd_rate is not None:
        dollars = 250
        uah_amount = dollars * usd_rate
        print(f"Актуальний курс USD: {usd_rate} грн")
        print(f"${dollars} коштують {uah_amount:.2f} грн")
    else:
        print("Не вдалося виконати розрахунок через відсутність курсу.")