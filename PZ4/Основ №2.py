n = int(input("Введите число N:"))

if n < 0:
    print("Ошибка введите N > 1")

k = 0

while 3**k < n:

    k += 1
print(k)


