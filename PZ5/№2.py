def squar(a, b):
    return a * b

def perimetr(a, b):
    return a + b

a = int(input("Введите длину прямоугольника:"))
b = int(input("Введите ширину прямоугольника:"))

squ = squar(a, b)
per = perimetr(a, b)


print(f"Площадь={squ}²см")
print(f"Периметр={per}см")

