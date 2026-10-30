import re

def parse_order(raw_message: str):
    cleaned_message = raw_message.strip()
    
    pattern = r"\[ORDER\]:\s*ID_(\d+)\s+Promo:\s+(\S+)\s+Sum:\s+([\d.]+UAH|[\d.]+)"
    
    match = re.search(pattern, cleaned_message)
    
    if not match:
        return None

    order_id = int(match.group(1))
    promo_code = match.group(2)

    sum_str = match.group(3).replace("UAH", "")
    order_sum = float(sum_str)
    
    return order_id, promo_code, order_sum

if __name__ == "__main__":
    raw_message = " [ORDER]: ID_84920 Promo: SUMMER2026 Sum: 1250.00UAH Status: PAID "
    
    result = parse_order(raw_message)
    
    if result is None:
        print("Формат повідомлення не підтримується")
    else:
        order_id, promo_code, order_sum = result
        print(f"Номер замовлення: {order_id} (тип: {type(order_id).__name__})")
        print(f"Промокод: {promo_code} (тип: {type(promo_code).__name__})")
        print(f"Сума: {order_sum} (тип: {type(order_sum).__name__})")