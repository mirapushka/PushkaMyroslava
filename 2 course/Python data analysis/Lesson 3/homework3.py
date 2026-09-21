total_count = 0
total_weight = 0.0
max_weight = None

while True:
    user_input = input("Введіть вагу деталі (або 'stop'): ")

    if user_input.lower() == "stop":
        break

    try:
        weight = float(user_input)
    except ValueError:
        print("Помилка! Введіть число або 'stop'.")
        continue

    if weight < 10 or weight > 1000:
        print("Дефект! Вага поза нормою (10-1000 г).")
        continue

    total_count += 1
    total_weight += weight

    if max_weight is None or weight > max_weight:
        max_weight = weight

print("\n--- Звіт контроля якості ---")
print("Прийнято деталей:", total_count)
print("Загальна вага:", total_weight, "г")

try:
    avg_weight = total_weight / total_count
    print("Середня вага деталі:", avg_weight, "г")
except ZeroDivisionError:
    print("Середня вага: немає даних (деталі не приймалися)")

if max_weight is not None:
    print("Найважча деталь:", max_weight, "г")
else:
    print("Найважча деталь: немає даних")