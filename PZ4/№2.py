a = 0
countr = 0

while a < 4:
    num = int(input(f"Введите {a + 1} число:"))

    b = num % 2
    if b == 0:
        countr += 1
    a += 1


print(f"Кол-ов чётных ччисел: {countr} ")
