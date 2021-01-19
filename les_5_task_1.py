from collections import namedtuple
from collections import deque

def year(q1, q2, q3, q4):
    return q1 + q2 + q3 + q4

NewFirm = namedtuple('NewFirm', 'name, quarter_1, quarter_2, quarter_3, quarter_4, func',
                       defaults=['NoName', 100, 100, 100, 100, year])


amount_firm = int(input("Введите количество предприятий "))

de = deque([])

for i in range(1, amount_firm + 1):
    firm = NewFirm(input("Введите название предприятия "), int(input("Введите доход за первый квартал ")), int(input("Введите доход за второй квартал ")), int(input("Введите доход за третий квартал ")), int(input("Введите доход за четвертый квартал ")), year)

    if(i % 2 != 0):
        de.append((firm.name, firm.func(firm.quarter_1, firm.quarter_2, firm.quarter_3, firm.quarter_4)))
    else:
        de.appendleft((firm.name, firm.func(firm.quarter_1, firm.quarter_2, firm.quarter_3, firm.quarter_4)))

avg = 0
for item in de:
   avg = (avg + item[1])

avg = avg / len(de)

print(f"Средняя прибыль равна {avg}")

for item in de:
    if item[1] > avg:
        print(f"Прибыль предприятия {item[0]} выше среднего")
    elif item[1] < avg:
        print(f"Прибыль предприятия {item[0]} ниже среднего")
    else:
        print(f"Прибыль предприятия {item[0]} равна среднему")