lim_in_range = 99
lim_mult = 9
amount_number = 0

for i in range(2, lim_in_range + 1):
    for ii in range(2, lim_mult + 1):
        if(i%ii != 0):
            break
        elif(ii == lim_mult):
            amount_number += 1
            print(i)

print(f"Всего чисел кратных от 2 до {lim_mult} в диапазоне от 2 до {lim_in_range} - {amount_number}") # первое число начинается от 2520