while True:
    try:
    
        A = int(input('Введдите число A:'))
        B = int(input('Введдите число B:'))

        C = A + B 

        if C < 0:
            print(C * 8)

        else:
            print(C * 1.5)
        break
       

    except ValueError:
        print('Невенроне значение')


