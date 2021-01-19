import random

#поиск медианы без сортировки

def find_min_index(arr):
    min_val = float("inf")
    i = 0

    for index, val in enumerate(arr):
        if val < min_val:
            min_val = val
            i = index
    print("Minimum item:", min_val)
    return i #индекс минимального элемента

m = 50
array = [random.randint(-100, 100) for i in range(2*m + 1)]
print(array)

l = len(array)//2 #определяем сколько раз нам нужно искать минимальный элемент, после удаления из списка предыдущего миним ального чтобы следующий был медианой
i = 0
while i < l:
    array.pop(find_min_index(array))
    i = i + 1

print()
print(f"Медианой является элемент {array[find_min_index(array)]}") #в формулем 2m + 1 медианой будет являеться всегда средний элемент поэтому следующий найденный минирмальный из исходного массива будет медианой