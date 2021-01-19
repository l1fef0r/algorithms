
number = input("Введите любое натуральное число ")

numB = int(number)
result = numB % 10

while (numB // 10) != 0:
    numB = numB // 10
    result = result * 10 + numB % 10

print(f"Его инверсией будет число {result}")