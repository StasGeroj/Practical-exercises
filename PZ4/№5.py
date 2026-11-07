N = int(input("Введите N чисел:"))

if N <= 0:
    print("Введите положительное число.")

else:
    i = 0
    s = 0

    while i < N:
        sum = int(input(f"Введите число {i + 1}:"))
        s += sum
        i += 1

average = s / N
print(f"Среднее значение: {average}")