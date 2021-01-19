import random

mass_size = 10
max_pos = 10
min_pos = -10
mass = []

p_max = 0
p_min = 0

rand_item = random.randint(min_pos, max_pos)
max_item = rand_item
min_item = rand_item
mass.append(rand_item)

for i in range(1, mass_size): #определяем минимальный и максимальный элементы массива и его позицию во время генерации массива
    tmp_rand_item = random.randint(min_pos, max_pos)
    if(tmp_rand_item > max_item):
        p_max = i
        max_item = tmp_rand_item
    if(tmp_rand_item < min_item):
        p_min = i
        min_item = tmp_rand_item

    mass.append(tmp_rand_item)

print(mass)

mass[p_max], mass[p_min] = mass[p_min], mass[p_max] #средствами языка пайтон менянию местами элементы
print(mass)

