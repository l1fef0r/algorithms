import random

mass_size = 10
max_pos = 10
min_pos = -10
mass = []
pos_max_neg = 0
max_neg = 0

for i in range(1, mass_size):
    tmp_rand_item = random.randint(min_pos, max_pos)
    if(tmp_rand_item < 0):
        if(max_neg == 0): #нужно чтобы запомнить первую иттерацию с отрицательным числом и запомнить его значение
            pos_max_neg = i
            max_neg = tmp_rand_item
        elif(tmp_rand_item > max_neg):
            pos_max_neg = i
            max_neg = tmp_rand_item
    mass.append(tmp_rand_item)


print(mass)
print(max_neg)