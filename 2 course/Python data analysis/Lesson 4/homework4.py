def calculate_discount(order_amount: float, client_status: str) -> float | None:
    """
    Розраховує суму комерційної знижки у гривнях.
    
    Аргументи:
        order_amount (float): Сума замовлення.
        client_status (str): Статус клієнта ("new", "silver", "gold").
        
    Повертає:
        float | None: Суму знижки у гривнях або None, якщо дані некоректні.
    """
    if order_amount <= 0 or client_status not in ("new", "silver", "gold"):
        return None
    
    if client_status == "new":
        discount_percent = 0.0
    elif client_status == "silver":
        discount_percent = 5.0
    elif client_status == "gold":
        discount_percent = 10.0
        
    if order_amount > 10000:
        discount_percent += 2.0
        
    discount_amount = order_amount * (discount_percent / 100)
    return round(discount_amount, 2)


def get_final_price(order_amount: float, discount_amount: float) -> float:
    """Обчислює фінальну ціну замовлення після застосування знижки."""
    return round(order_amount - discount_amount, 2)


amount = 12000.0
status = "gold"

discount = calculate_discount(amount, status)
if discount is not None:
    final_price = get_final_price(amount, discount)
    print(f"Знижка: {discount} грн")
    print(f"Фінальна ціна: {final_price} грн")
else:
    print("Помилка: невірні дані замовлення.")

invalid_amount = -500.0
invalid_discount = calculate_discount(invalid_amount, "new")

if invalid_discount is not None:
    print(get_final_price(invalid_amount, invalid_discount))
else:
    print("Не вдалося розрахувати знижку: сума або статус некоректні (отримано None).")