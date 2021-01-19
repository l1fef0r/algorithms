import cProfile
from math import sqrt

def noterat2(n):

    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5
    lst = [2]
    for i in range(3, n*n//2 + 1, 2): #элемент на нужной нам позиции не будет больше в списке натуральных чисел от 1 до n*n//2, формула эмпирическая
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j > int((sqrt(i)) + 1):
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst[n-1]


def noterat(n):
# в этом алгоритме последнее простое число будет является тем которое мы ищем,
# его принцип, каждое следующее число делится на числа от 2 до самого себя,
# если без остатка делится только на самого себя, алгоритм останавливается и выводит простое число на заданной позиции
    i = 2
    p = 0
    tmp = 1
    if n == 1:
        return 2
    p = 1
    while p != n:
        i += 1
        for ii in range(2, i+1):
            if i % ii == 0:
                if i == ii:
                    tmp = i
                    p += 1
                else:
                    break
    return tmp


#Сначала отметим все числа от 2 до n простыми
#Пройдёмся по каждому из них
#Если текущее число i отмечено простым, то все числа от 2 * i до n, которые делятся на i отметим непростыми.
def erat(n): #алгоритм Эратосфена, (n*n//2) - эмпирическая формула, чтобы наверняка число по заданной позиции находилось в этом списке просты
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5
    is_prime = [True] * ((n*n//2) + 1)  # Отметим все числа простыми
    is_prime[0], is_prime[1] = False, False  # Убираем 0 и 1 из простых
    for i in range(2, (n*n//2) + 1):
        if is_prime[i]:
            for j in range(2 * i, (n*n//2) + 1, i):   # Убираем числа, которые делятся на i
                is_prime[j] = False
    primes = []   # Формируем список простых
    for i in range(2, (n*n//2) + 1):
        if is_prime[i]:
            primes.append(i)
    return primes[n-1]


n = int(input("Введите позицию простого числа, которое хотите получить, от 1 до n "))
print(noterat2(n))
print(noterat(n))
print(erat(n))

cProfile.run('noterat2(n)')
cProfile.run('noterat(n)')
cProfile.run('erat(n)')

# Замеры были сделаны при поиске простого числа на позиции 500, данные проанализированы с помощью библиотеки cProfile
#Первый алгоритм показал, то что он очень медленно рабоает, это связанно с тем что у него очень много
# иттераций в цикле с операцией добавления в список и использование математической библиотеки, также это связанно с эмпирической формулой n*n//2 которая небоходима для поиска значения по позиции
#а также увеличивает затраты памяти, оценка сложности О(N*N) (содержит вложенный цикл)
#второй алгорит работает значительно быстрее поскольку он не использует списки работа и завершается сразуже по нахождению нужного числа, при этом он затрачивает немного памяти
# оценка сложности О((n*n//2)*(n*n//2)) (содержит вложенный цикл с формированием последовательности n*n//2)
#третий алгоритм (Эратосфена) немного быстрее, это связанно с тем что он использует логипу поиска с оценкой скорости О(n) + O(N log log n)
# медленней работает, потому что он использует много памяти, с формированием большого в списке размером n*n//2 в в котором мы находим искомое значение позиции
#оценка сложности О(n*n//2)+ O(n*n//2 log log (n*n//2)), алгоритм эратосфена + работа со списком с формированием последовательности n*n//2
#Рассматривая три реализиации подобных алгоритмов, можно прийти к выводу
#Первый алгоритм из трех абсолютно не пригоден для работы, второй будет полезен для экономии памяти при этом оставаясь достаточно быстрым, третий быстро выполняет основную задачу, хотя использует много памяти

# 3571
# 3571
# 3571
#          912914 function calls in 0.694 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.694    0.694 <string>:1(<module>)
#         1    0.477    0.477    0.694    0.694 les_4_task_2.py:5(noterat2)
#         1    0.000    0.000    0.694    0.694 {built-in method builtins.exec}
#    901177    0.215    0.000    0.215    0.000 {built-in method math.sqrt}
#     11733    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          5 function calls in 0.082 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.082    0.082 <string>:1(<module>)
#         1    0.082    0.082    0.082    0.082 les_4_task_2.py:36(noterat)
#         1    0.000    0.000    0.082    0.082 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          11738 function calls in 0.054 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.054    0.054 <string>:1(<module>)
#         1    0.052    0.052    0.053    0.053 les_4_task_2.py:23(erat)
#         1    0.000    0.000    0.054    0.054 {built-in method builtins.exec}
#     11734    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

