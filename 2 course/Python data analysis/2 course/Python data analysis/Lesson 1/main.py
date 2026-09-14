a = input("Відстань маршруту в кілометрах: ")
a_num = float(a)

b = input("Середня витрата пального авто на 100 км у літрах: ")
b_num = float(b)

c = input("Вартість одного літра пального в гривнях: ")
c_num = float(c)

fuel = (a_num / 100) * b_num
cost = fuel * c_num 


print(f" {fuel:.2f} л пального, коштує {cost:.2f} грн")