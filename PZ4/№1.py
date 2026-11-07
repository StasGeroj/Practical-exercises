a = 0
sum_num = 0
countr_num = 0

while a < 4:
    num = float(input(f"Введите число {a+1}:"))
    if num < 0:
        sum_num += num
        countr_num += 1

    a += 1

    print(f"Сумма отрицательнных чисел: {sum_num}")
    print(f"Кол-ов отрицательнных чисед: {countr_num}")


