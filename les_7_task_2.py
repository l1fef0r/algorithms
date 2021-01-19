import random


N = 8
R = 5
array = [round(random.random()*50, R) for i in range(N)]


def merge_sort(arr):

    if len(arr) > 1:
        l = arr[:len(arr) // 2]
        merge_sort(l) # делим спеисок до получение атомарного списка
        r = arr[len(arr) // 2:]
        merge_sort(r)

        #после делений возвращаемся вверх по стеку, где на кажлом уровне будет увеличиватья количество элементов справа и слева примерно по одному

        i = 0
        j = 0
        k = 0
        while i < len(l) and j < len(r): #здесь происходит слияние, на каждом уровне
            if l[i] < r[j]:
                arr[k] = l[i]
                i = i + 1
            else:
                arr[k] = r[j]
                j = j + 1
            k = k + 1

        while i < len(l): # добавляем оставшием после слияния числа
            arr[k] = l[i]
            i = i + 1
            k = k + 1

        while j < len(r):
            arr[k] = r[j]
            j = j + 1
            k = k + 1


print(array)
merge_sort(array)
print(array)