N = int(input("Введите N чисел:"))

if N <= 0:
    print("Введите положительное число.")
else:
    i = 0
    s = 0
    while i < N:
        zero = int(input(f"Введите число {i + 1}:"))
        if zero == 0:
            s += 1

        i += 1

print(f"Количество нулей: {s}")