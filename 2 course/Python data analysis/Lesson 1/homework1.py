a = input(" вага вантажу (кг): ")
a_num = float(a)

b = input("відстань перевезення (км): ")
b_num = float(b)

c = input("вартість вантажу (грн): ")
c_num = float(c)

base_fare = 100
weight_rate = 20
distance_rate = 15

delivery_cost = base_fare + (a_num * weight_rate) + (b_num * distance_rate)

print("\n            ЧЕК ")
print(f"Вартість: {c_num:.2f} грн")
print(f"Вага вантажу:       {a_num:.2f} кг")
print(f"Відстань:           {b_num:.2f} км")
print("---------------------------------")
print(f"Вартість доставки:  {delivery_cost:.2f} грн")
