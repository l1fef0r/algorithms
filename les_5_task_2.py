import collections
import copy

hexDecNumbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
decHexNumbers = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

number_one = collections.deque(input("Введите первое число в 16и ричном виде ").upper())
number_two = collections.deque(input("Введите второе число в 16и ричном виде ").upper())
number_1_mul = copy.copy(number_one) #копируем числа введение пользователем для умножений
number_2_mul = copy.copy(number_two)

def sum(number_one, number_two): #функция суммы двух HEX чисел
    n_one = copy.copy(number_one)
    n_two = copy.copy(number_two)
    n_one.reverse()
    n_two.reverse()
    number_min = None #ссылки, чтобы не запутаться
    number_max = None
    number_res = None
    minL = None

    if len(n_one) > len(n_two):
        number_max = n_one
        number_min = n_two
        minL = len(n_two)
    else:
        number_max = n_two
        number_min = n_one
        minL = len(n_one)

    number_res = copy.copy(number_max) #определяем большее число к которому будем прибавлять второе число
    i = 0
    decNum = 0
    tmp = 0
    while i < minL:
        decNum = tmp + hexDecNumbers[number_max[i]] + hexDecNumbers[number_min[i]]
        if decNum < 16:
            number_res[i] = decHexNumbers[decNum]
            tmp = 0
        else:
            tmp = 1
            number_res[i] = decHexNumbers[decNum % 16]
        i += 1
    if tmp == 1 and i == len(number_res):
        number_res.append('1')
    elif tmp == 1:
        while i < len(number_res):
            if (hexDecNumbers[number_res[i]] + 1) < 16:
                number_res[i] = decHexNumbers[(hexDecNumbers[number_res[i]] + 1) % 16]
                tmp = 0
                break
            else:
                number_res[i] = '0'
                tmp = 1
            i += 1
        if tmp == 1:
            number_res.append('1')

    number_res.reverse()
    return number_res

number_sum = sum(number_one, number_two)

print(f"Результат сложения двух HEX чисел будет {number_sum}")

def multiHexNum(a, b): #функция получения остатка от деления 16и ричного числа и его целой части
    n1 = hexDecNumbers[a]
    n2 = hexDecNumbers[b]
    n_m = n1 * n2
    return int(n_m / 16), n_m % 16 #получаем остаток от деление, которая будет HEX числом и целая часть которую нужно запомнить и прибавить к следуюзему числу

minL = 0
maxL = 0
number_max = None
number_min = None


if len(number_1_mul) > len(number_2_mul): #определяем величину прохождений цикла для его остановки
    number_max = number_1_mul #создание ссылки для удобства
    number_min = number_2_mul
    minL = len(number_2_mul)
    maxL = len(number_1_mul)
else:
    number_max = number_2_mul
    number_min = number_1_mul
    minL = len(number_1_mul)
    maxL = len(number_2_mul)

number_max.reverse() #разворачиваем для удобства, чтобы проходил от меньшего числа к большему
number_min.reverse()
numbers_res = collections.deque()  # здесь записывается текущее умножение первого числа на элемент второго числа
numbers_res_prev = collections.deque() #складываем числа циклично и сохраняем в эту очередь
numbers_res_prev.append('0') #для удобства, определяем очередь

i = 0
while i < minL:
    tmp = 0
    j = 0
    numbers_res = collections.deque() #после каждого прохода пересоздаем очередь, чтобы умножить первое число на следующий элемент второго числа и сохранить в него

    while j < maxL:
        n1, n2 = multiHexNum(number_min[i], number_max[j])
        tmp = tmp + n2
        if tmp < 16:
            numbers_res.append(decHexNumbers[tmp])
            tmp = 0
        else:
            numbers_res.append(decHexNumbers[tmp % 16])
            tmp = int(tmp / 16)
        tmp = tmp + n1
        j += 1
    if tmp != 0:
        numbers_res.append(decHexNumbers[tmp]) #не забываем про остаток после вычислений
    for _ in range(i):
        numbers_res.appendleft('0')

    numbers_res.reverse()
    print(f'+ {numbers_res}')
    numbers_res_prev = sum(numbers_res_prev, numbers_res)  # запоминаем текущий результат вычислений
    i += 1

print(f'Результатом умножения двух HEX чисел будет {numbers_res_prev}')