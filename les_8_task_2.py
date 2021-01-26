from collections import Counter  # словарь в котором для каждого объекта поддерживается счетчик

def huffman_encode(sentence):

    symbols = Counter(sentence)  # определяем частотность символов, для удобства использовал коллекцию каунтер

    sym = []
    for letter in symbols:
        sym.append([letter, symbols.get(letter), ""]) #создаем двухмерный массив для удобства расчетов

    sym.sort(key=lambda x: x[1], reverse=True) #сортируем массив по убыванию, по второму аргументу, частотности, для быстрого определние ветки и удаление методом поп

    temp_sym = []
    temp_sym.extend(sym)

    pr_min = None
    pr_min = sym[len(sym)-1]

    while (len(temp_sym) > 0):
        min_1 = temp_sym.pop() #в отсартированном списке - это всегда левая ветка т.е. - 0, т.к. самый меньший элемент всегда "последний" в списке, за исключением последнеего элемента
        if(len(temp_sym) == 0): #обработка ситуации когда у нас остался только один минимальный элемент, то нужно будет использоватать предыдущий
            i = 0
            while (i < len(pr_min[0])):
                el = pr_min[0][i]
                for ii in sym:
                    if (el == ii[0]):
                        if(pr_min[1] >= min_1[1]):
                            ii[2] = "1" + ii[2]
                        else:
                            ii[2] = "0" + ii[2]
                            break
                i = i + 1

            if(len(sym)>1): #надо учесть что в тексте может быть только один символ, тогда игнорирует этот цикл
                i = 0
                while (i < len(min_1[0])):
                    el = min_1[0][i]
                    for ii in sym:
                        if (el == ii[0]):
                            if (min_1[1] >= pr_min[1]):
                                ii[2] = "1" + ii[2]
                            else:
                                ii[2] = "0" + ii[2]
                                break
                    i = i + 1
            return sym

        pr_min = []
        i = 0
        while (i < len(min_1[0])):
            el = min_1[0][i]
            for ii in sym:
                if (el == ii[0]):
                    ii[2] = "0" + ii[2]
                    break
            i = i + 1
        if (len(temp_sym) > 0):
            min_2 = temp_sym.pop()#в отсартированном списке - это всегда правая ветка т.е. - 1
            temp_sym.append([min_1[0] + min_2[0], min_1[1] + min_2[1]])
            temp_sym.sort(key=lambda x: x[1], reverse=True)
            
            pr_min.append(min_1[0] + min_2[0]) #необъодимо для проверки конечного случая, если самый последний элемент будет больше суммы всех остальных
            pr_min.append(min_1[1] + min_2[1])
            i = 0
            while (i < len(min_2[0])):
                el = min_2[0][i]
                for ii in sym:
                    if (el == ii[0]):
                        ii[2] = "1" + ii[2]
                        break
                i = i + 1
    return sym

def huffman_decode(encoded, sym):  # функция декодирования исходной строки по кодам Хаффмана
    sx = []  # инициализируем массив символов раскодированной строки
    enc_ch = ""  # инициализируем значение закодированного символа
    for ch in encoded:
        enc_ch += ch  # добавим текущий символ к строке закодированного символа
        for dec_ch in sym:  # постараемся найти закодированный символ в словаре кодов
            if sym.get(dec_ch) == enc_ch:
                sx.append(dec_ch)  # добавим значение раскодированного символа к массиву раскодированной строки
                enc_ch = ""
                break
    return "".join(sx)

sentence = input("Введите любое предложение ")
sym = huffman_encode(sentence)
print(sym)

haffmanstring = ""
for i in sentence:
    for ii in sym:
        if (i == ii[0]):
            haffmanstring = haffmanstring + ii[2]
            break
print(f'Текст: "{sentence}" в кодировке Хаффмана будет - "{haffmanstring}"')

code = {} #изначально словарь лежит в двухмерном списке, для удобства декодирование помещаем его в структуру СЛОВАРЬ
for i in sym:
    code.update({i[0]: i[2]})
print(code)
print(f"Раскодируем строку {haffmanstring}, где получаем {huffman_decode(haffmanstring, code)}")