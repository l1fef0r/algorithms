import random

mass_size = 10
max_pos = 10
min_pos = -10
mass = []
dict_items = {}


for i in range(1, mass_size):
    tmp_rand_item = random.randint(min_pos, max_pos)
    if ((tmp_rand_item in dict_items) == False):
        dict_items[tmp_rand_item] = 1
    else:
        dict_items[tmp_rand_item] = dict_items.get(tmp_rand_item) + 1 #добавляем элементы в словарь, если этот элемент уже есть, то прибавляем на единицу
    mass.append(tmp_rand_item)

max_freq = 0
list_numbers_with_max_freq = []

for key, val in dict_items.items(): #достаем числа с повторами из словаря

    if(val > max_freq):
        list_max_freq = []
        list_numbers_with_max_freq = []

        max_freq = val

        list_numbers_with_max_freq.append(key)

    elif(val == max_freq): #если несколько чисел имеет одинаковое число повторений, то добавляем его в лист
        list_numbers_with_max_freq.append(key)

    print(key, val)

print(f"Числа которые имеют наибольшую частоту повторений {list_numbers_with_max_freq}")
