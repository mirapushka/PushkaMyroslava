try:
    balance = float(input("Поточний баланс: "))
    summa = float(input("Сума платежу: "))
    kat = input("Категорія акаунту ('1': standard, '2': gold, '3': platinum): ")

    if kat == "1":
        komisya = 0.02
    elif kat == "2":
        komisya = 0.01
    elif kat == "3":
        komisya = 0.0
    else:
        print("Помилка")
        komisya = None

    if komisya is not None:
        if summa <= 0:
            print("Сума має бути більшою за нуль")
        else:
            komisya_grn = summa * komisya
            vsego = summa + komisya_grn

            if vsego > balance:
                print("Недостатньо коштів")
            else:
                balance = balance - vsego
                print(f"Баланс: {balance:.2f} грн")

except ValueError:
    print("Введіть число")