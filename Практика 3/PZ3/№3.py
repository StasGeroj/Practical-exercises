while True:
    try:
        A = int(input('Введите двузначное число: '))

        if not (10 <= abs(A) <= 99):
            print('Число не двузначное, попробуйте снова')
            continue

        X, Y = divmod(abs(A), 10)
        B = X + Y

        if B % 2 == 0:
            print(abs(A + 2))
        else:
            print(abs(A - 2))
        break

    except ValueError:
        print('Неверное значение')