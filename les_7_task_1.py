import random


N = 10
array = [random.randint(-100, 100) for i in range(N)]

def selection_sort(arr):
    n = 1
    while n < len(array):
        i = n #модификация
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1


print(array)
selection_sort(array)
print(array)