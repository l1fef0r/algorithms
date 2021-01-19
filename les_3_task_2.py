import random

mass_size = 100
max_pos = 100
mass_1 = []
mass_2 = []

for i in range(1, mass_size+1):
    rand_item = random.randint(1, max_pos+1)
    mass_1.append(rand_item) #генерация массива натуральных чисел
    if(rand_item % 2 == 0):
        mass_2.append(i-1) #добавляем позиции четных элементов во второй массив

print(mass_1)
print(mass_2)


