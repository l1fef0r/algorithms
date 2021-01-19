flag = True
x = 0
y = 0
result = None
s = '+'

while True:

    if flag == True:
        x, y, s = input("Введите через пробел два числа и знак операции (последнее) ").split()
    else:
        s = input("Введите знак операции ")

    if s == '0':
        break

    if s == '+':
        result = int(x) + int(y)
        flag = True
    elif s == '-':
        result = int(x) - int(y)
        flag = True
    elif s == '*':
        result = int(x) * int(y)
        flag = True

    elif s == '/':
        if y != '0':
            result = int(x) / int(y)
        else:
            result = 'Деление на ноль недопустимо!'
        flag = True
    else:
        result = "Недопустимый знак операции!"
        flag = False
    print(result)





