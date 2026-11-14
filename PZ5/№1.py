def cifra(x):

    x = abs(x)
    sum = 0
    while x > 0:
 
        sum += x % 10
        x //= 10

    return sum


a = int(input("Введите  число 1:"))
b = int(input("Введите  число 2:"))
c = int(input("Введите  число 3:"))

cifra(a)
cifra(b)
cifra(c)

if cifra(a) > cifra(b) and cifra(c):
    print("самма числа 'a' нибольшее")
elif cifra(b) > cifra(a) and cifra(c):
    print("самма числа 'b' нибольшее")     
elif cifra(c) > cifra(a) and cifra(b):
    print("самма числа 'c' нибольшее") 
else:
    print("сумма каждого числа равна")