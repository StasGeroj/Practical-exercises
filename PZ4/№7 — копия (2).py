A = int(input("Введите число A:"))
B = int(input("Введите число B:"))

if A >= B:
    print("Ошибка: должно быть A < B")
else:

    
    s = 0
    i = B

while i >= A:
    print(i)

    i -= 1
    s += 1

print(f'количество числ:{s}')
    