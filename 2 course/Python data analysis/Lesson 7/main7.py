import csv
import json

filtered_data = []

try:
    with open("data.csv", "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        
        for row in reader:
            if row["status"] == "1":
                price = float(row["price"])
                quantity = int(row["quantity"])
                row["total_cost"] = price * quantity

                filtered_data.append(row)

    with open("data.json", "w", encoding="utf-8") as json_file:
        json.dump(filtered_data, json_file, ensure_ascii=False, indent=4)
        
    print("Файл збережено у data.json!")

except FileNotFoundError:
    print("файл data.csv не знайдено.")
except Exception as e:
    print(f"Сталася помилка {e}")