def cihra(x):

    countr = 0

    while x > 0:
        x //= 10
        countr += 1
    return countr

x = int(input("Введите число:"))

result = cihra(x)
print(f"Количество цифр в числе:{result}")
    

