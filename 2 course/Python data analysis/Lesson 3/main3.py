total_cash = 0 
sales_sum = 0  
returns_sum = 0 
receipts_count = 0 

while True:
    user_input = input("Введіть суму чека (або 'close' для завершення): ")

    if user_input.lower() == "close":
        break

    try:
        amount = float(user_input)
    except ValueError:
        print("Помилка! Введіть коректне число або 'close'.")
        continue

    if amount == 0:
        continue

    receipts_count += 1
    total_cash += amount

    if amount > 0:
        sales_sum += amount
    else:
        returns_sum += abs(amount)

print("Загальна кількість чеків:", receipts_count)
print("Загальна сума оплат:", sales_sum)
print("Загальна сума повернень:", returns_sum)
print("Баланс каси:", total_cash)