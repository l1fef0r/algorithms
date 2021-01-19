import platform
import random
import sys
from collections import deque


print(platform.python_implementation()) #CPython
print(platform.architecture()) #('32bit', 'WindowsPE'), хотя ОС 64-разрядная
print(platform.processor()) #Intel64 Family 6 Model 60 Stepping 3, GenuineIntel
print(sys.version) #3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]




#Особенность реализации с помощью getsizeof заключается в том, что мы кладет все переменные в ОДИН список или очередь,
# размер которых по завершению работы выводится на экран функцией getsizeof

list_sizes = [] # массив в который будет складываться ссылки, для подсчета размера, актуально для первой и третьей программы
deq_sizes = deque() #2-я программа использует очередь, для упрощения подсчета памяти все данные будут складироваться такде в очередь
MAX = 0 #будет хранится максимальное значение использования памяти в пике

SIZE = 1000 #количество замеров
MIN_ITEM = -7500000000000
MAX_ITEM = -75


list_sizes.append(SIZE)
list_sizes.append(MIN_ITEM)
list_sizes.append(MAX_ITEM)

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

list_sizes.extend(array)

# вариант 1, со списком
i = 0
index = -1

list_sizes.append(i)
list_sizes.append(index)
list_sizes.append(len(array))

MAX = sys.getsizeof(list_sizes)


while i < len(array):
    if array[i] < 0 and index == -1:
        index = i

    elif 0 > array[i] > array[index]:
        index = i

    list_sizes.pop()
    list_sizes.pop()

    i += 1

    list_sizes.append(i)
    list_sizes.append(index)
    if(MAX < sys.getsizeof(list_sizes)):
        MAX = sys.getsizeof(list_sizes)


if index != -1:
    print(f'Максимальное отрицательное число {array[index]} ')

list_sizes.remove(len(array))
print(f"Первая программа использует {sys.getsizeof(list_sizes)} байт(а)") #учитываем что мы уже использовали списко для генерации чисел
print(f"Пиковое значение {MAX} байт(а)")



# вариант 2, с -inf с использованием очереди вместо списка


deq = deque(random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)) #для примера взята очередь вместо списка
deq_sizes.append(SIZE)
deq_sizes.append(MIN_ITEM)
deq_sizes.append(MAX_ITEM)
deq_sizes.extend(deq)

num = float('-inf')

deq_sizes.append(num)
deq_sizes.append(index)
MAX = sys.getsizeof(deq_sizes)

for i, item in enumerate(deq):
    if 0 > item > num:
        deq_sizes.pop()
        deq_sizes.pop()

        num = item
        index = i

        deq_sizes.append(num)
        deq_sizes.append(index)

        if (MAX < sys.getsizeof(deq_sizes)):
            MAX = sys.getsizeof(deq_sizes)

    deq_sizes.append(item)
    deq_sizes.append(i)

    if(MAX < sys.getsizeof(deq_sizes)):
        MAX = sys.getsizeof(deq_sizes)

    deq_sizes.pop()
    deq_sizes.pop()

if num != float('-inf'):
    print(f'Максимальное отрицательное число {num} ')

print(f"Вторая программа использует {sys.getsizeof(deq_sizes)} байт(а)")#учитываем что мы уже использовали очередь для генерации чисел
print(f"Пиковое значение {MAX} байт(а)")


#вариант без списков и очереди

list_sizes.clear()

list_sizes.append(MIN_ITEM)
list_sizes.append(MAX_ITEM)
list_sizes.append(SIZE)

max_neg = 0
list_sizes.append(max_neg)
MAX = sys.getsizeof(list_sizes)

for i in range(1, SIZE):

    tmp_rand_item = random.randint(MIN_ITEM, MAX_ITEM)

    list_sizes.append(tmp_rand_item)
    list_sizes.append(i)

    if(MAX < sys.getsizeof(list_sizes)):
        MAX = sys.getsizeof(list_sizes)

    if(tmp_rand_item < 0):

        if(max_neg == 0): #нужно чтобы запомнить первую иттерацию с отрицательным числом и запомнить его значение
            list_sizes.remove(max_neg)
            max_neg = tmp_rand_item
            list_sizes.append(max_neg)
        elif(tmp_rand_item > max_neg):
            list_sizes.remove(max_neg)
            max_neg = tmp_rand_item
            list_sizes.append(max_neg)

        if (MAX < sys.getsizeof(list_sizes)):
            MAX = sys.getsizeof(list_sizes)
        list_sizes.pop()
        list_sizes.pop()
    else:
        list_sizes.pop()
        list_sizes.pop()

print(f'Максимальное отрицательное число {max_neg} ')
print(f"Третья программа использует {sys.getsizeof(list_sizes) - sys.getsizeof([])} байт(а)") #вычетаем список т.к. он не нужен для работы этой программы
print(f"Пиковое значение {MAX - sys.getsizeof([])} байт(а)")

# Результат работы программы при значении SIZE = 10
# Максимальное отрицательное число -215075692257
# Первая программа использует 108 байт(а)
# Пиковое значение 108 байт(а)
# Максимальное отрицательное число -1823510344609
# Вторая программа использует 312 байт(а)
# Пиковое значение 312 байт(а)
# Максимальное отрицательное число -42237105212
# Третья программа использует 32 байт(а)
# Пиковое значение 32 байт(а)

# Результат работы программы при значении SIZE = 100
# Максимальное отрицательное число -84393847754
# Первая программа использует 512 байт(а)
# Пиковое значение 512 байт(а)
# Максимальное отрицательное число -167618077771
# Вторая программа использует 840 байт(а)
# Пиковое значение 840 байт(а)
# Максимальное отрицательное число -47813666282
# Третья программа использует 32 байт(а)
# Пиковое значение 32 байт(а)

# Результат работы программы при значении SIZE = 1000
# Максимальное отрицательное число -3917072820
# Первая программа использует 4564 байт(а)
# Пиковое значение 4564 байт(а)
# Максимальное отрицательное число -5495202442
# Вторая программа использует 4536 байт(а)
# Пиковое значение 4536 байт(а)
# Максимальное отрицательное число -9610836817
# Третья программа использует 32 байт(а)
# Пиковое значение 32 байт(а)

# Для отработки задания была взята 5-я задача 3-го урока
# Выполено три реализации поиска максимальо отрицательного числа.
# 1-я программа выполняет поиск максмимального отрицательного числа в сгенерированном списке
# 2-я программа выполняет поиск максмимального отрицательного числа в сгенерированной очереди
# 3-я программа выполняет поиск максмимального отрицательного числа на лету, т.е. значения в цикле приходят случайно, где сразу же отсеиваются
# неудовлетворяющие условию результаты
# В результате работы программы было выявленно, что третья программа использует наименьшее количества памяти,
# причем объем памяти не изменеяем и является константой вне зависимости от размера поиска для любого количества имзерений и равен 32 - байта
# 2-я использует очередь, примерно до 1000 измерений она использует больше памяти чем первая, но при увеличении
# количества необходимых измерений программа использует незначительно меньше памяти в сравнении с третьей программой
# при очень малом количестве измерений, например SIZE = 10 2-я программа использует значительно больше памяти
# в сравнении с другими программами, что по всей видимости является особенностью реализации внутренней структуры очереди.
# Для 1-й программы от 10 измерений и выше зависимость от использования памяти и количество замеров линейная
# Для 2-й программы от 1000 измерений и выше зависимость от использования памяти и количество замеров линейная
# В результате анализа использования памяти, то из трех приведенных программ третья является наиболее предпочтительной в качестве экономии памяти

