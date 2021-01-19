def sum(n):
    if n == 1:
        return 1
    else:
        return 1 + sum(n - 1)/(-2)


n = input("Введите конечный элемент n для получения суммы всего ряда 1, -0.5, 0.25, -0.125,... ")

print(sum(int(n)))

