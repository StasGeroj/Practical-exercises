while True:
    try:

        A = int(input('Введите число:'))

        if A > 0: 
            print(A + 20)

        else:
            print(A - 5)

    except ValueError:
        print('Неверное значеине')