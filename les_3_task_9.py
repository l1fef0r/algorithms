import random

matx_size_l = 5
matx_size_c = 6
max_pos = 9
min_pos = 0

matx = [[0] * matx_size_c for column in range(matx_size_l)]
# создаем матрицу



for line in range(1, matx_size_l+1):
    # заполняем матрицу случайными элементами
    for column in range(1, matx_size_c+1):
        tmp_rand_item = random.randint(min_pos, max_pos)
        matx[line-1][column-1] = tmp_rand_item



for line in matx:
    print(' '.join([str(column) for column in line]))
    # проверяем


min_el_in_col = matx[0][0]
max_el = matx[0][0]

tmp_max_el = max_el
i = 0
list_min_el = []
l = 0

while True:
    if(l < matx_size_l):
        if(matx[l][i] < min_el_in_col):
            min_el_in_col = matx[l][i] # определяем минимальный элемент в колонке
            tmp_max_el = min_el_in_col
        l += 1
    else:
        if i == 0:
            max_el = tmp_max_el  # определяем первый элемент, потенциально максимальный
        if max_el < min_el_in_col and i > 0:
            max_el = min_el_in_col
        list_min_el.append(min_el_in_col)
        if i < matx_size_c - 1:
            l = 0
            i += 1
            min_el_in_col = matx[0][i]
        else:
            break


print(f"Минимальные элементы в столбцах - {list_min_el}")
print(f"Максимальный элемент из минимальных элементов - {max_el}")
