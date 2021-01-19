number = 0
even = 0
odd = 0

number = input("Введите любое натуральное число ")

numB = int(number)
numS = int(number) % 10

while (numB != 0):

    if numS % 2 == 0 or numS == 0:
        even += 1
    else:
        odd += 1
    numB = numB // 10
    numS = numB % 10
print(f"Количество четных - {even}. Количество нечетных {odd}")
