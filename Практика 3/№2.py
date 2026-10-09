while True:
    try:


        A = int(input('Введите число:'))

        if A % 2 == 0:
            print(A / 4)

        else: 
            print(A * 5)

    except ValueError:
        print('неверное значение:')