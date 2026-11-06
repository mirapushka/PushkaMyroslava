inventory = [
    {"item": "Ноутбук", "supplier": "TechCorp", "qty": 10, "price": 25000.0},
    {"item": "Мишка", "supplier": "AccsCo", "qty": 50, "price": 450.0},
    {"item": "Клавіатура", "supplier": "TechCorp", "qty": 20, "price": 1200.0},
    {"item": "Монітор", "supplier": "ScreenMaster", "qty": 8, "price": 8500.0},
    {"item": "Ноутбук", "supplier": "MegaDist", "qty": 5, "price": 26000.0},
]

unique_suppliers = {row["supplier"] for row in inventory}

total_stock = {}
for row in inventory:
    item_name = row["item"]
    quantity = row["qty"]
    total_stock[item_name] = total_stock.get(item_name, 0) + quantity

total_inventory_value = sum(row["qty"] * row["price"] for row in inventory)

print(f"Унікальні постачальники: {unique_suppliers}")
print(f"Загальна кількість товарів на складі: {total_stock}")
print(f"Загальна вартість усього складу: {total_inventory_value:,.2f} грн")