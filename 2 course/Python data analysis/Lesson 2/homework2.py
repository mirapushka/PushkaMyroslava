try:
    kwh = float(input("Введіть кВт·год: "))

    if kwh < 0:
        print("Число має бути більше 0")
    else:
        if kwh <= 100:
            suma = kwh * 2.64
        elif kwh <= 300:
            suma = (100 * 2.64) + ((kwh - 100) * 4.32)
        else:
            suma = (100 * 2.64) + (200 * 4.32) + ((kwh - 300) * 6.00)

        print(f"До сплати: {suma:.2f} грн")

except ValueError:
    print("Введіть число")