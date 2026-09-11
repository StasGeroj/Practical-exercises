import math

A=int(input("Введите значение A: "))
B=int(input("Введите значение B: "))

while True:
    if A < B:
        print("A должно быть больше или равно B. Пожалуйста, введите значение B снова.")
        B = int(input("Введите значение B: "))
        

    else:
        
           print(A % B)
           break
            
        
        
       
