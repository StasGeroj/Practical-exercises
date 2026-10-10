while True:
    try:
        A = int(input('Введите число A:'))
        B = int(input('Введите число B:'))

        C = A + B

        X, Y = divmod(C, 5)

        if Y == 0:
            print(C + 1)

        else:
            print(C - 2)

        break

    except ValueError:
        print('неверное значение')
