ascii = 31
str = ""

while ascii != 127:
    ascii += 1

    if ascii % 10 == 2: # разбика по 10
        print(str)
        str = ""

    if len(f"{ascii}") < 3: # не совсем хорошее решение для хорошего отображения по 10 чисел, если число имеет меньше трех символов
        str = str + " " + f" {ascii}:" + " " + chr(ascii)
    else:
        str = str + " " + f"{ascii}:" + " " + chr(ascii)

print(str) #Вывод остатка, нет 10 чисел