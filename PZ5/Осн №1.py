'''Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
получится нуль?'''
def zero(a):

    countr = 0

    while a > 0:
        suma = 0
        temp = a

        while temp > 0:
            suma += temp % 10
            temp //= 10
            
        a -= suma
        countr += 1
    return countr

a = int(input("Введите число:"))

x = zero(a)
print(f"{x}")

