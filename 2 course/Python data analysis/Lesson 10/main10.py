import requests

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
TARGET_CODES = {"USD", "EUR"}


def get_rates() -> list[dict]:
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code != 200:
            print(f"Помилка сервера. Код статусу: {response.status_code}")
            return []

        data = response.json()
        return [item for item in data if item.get("cc") in TARGET_CODES]

    except requests.exceptions.RequestException as e:
        print(f"Помилка запиту до API НБУ: {e}")
        return []


def print_rates(rates: list[dict]) -> None:
    if not rates:
        print("Дані про валюти не отримано.")
        return

    print(f"{'Назва валюти':<22} | {'Код':<4} | {'Курс (грн)':<11} | {'Дата'}")
    print("-" * 55)
    for item in rates:
        txt = item.get("txt", "")
        cc = item.get("cc", "")
        rate = item.get("rate", "")
        date = item.get("exchangedate", "")
        print(f"{txt:<22} | {cc:<4} | {rate:<11} | {date}")


if __name__ == "__main__":
    filtered_rates = get_rates()
    print_rates(filtered_rates)