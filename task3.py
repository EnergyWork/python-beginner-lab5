import numpy as np

"""
Дана целочисленная прямоугольная матрица. Определить: количество строк, 
не содержащих ни одного нулевого элемента, а также максимальное значение из чисел, 
встречающихся в заданной матрице более одного раза.
"""

matr = np.random.randint(-5, 5, size=(5, 5), dtype='int64')
print(matr)
print('Количество строк без нулей:', np.size(matr, axis=1) - np.count_nonzero(np.any(matr == 0, axis=1)))

uniq = np.unique(matr, return_counts=True)
print(uniq)
tmp = np.array([], dtype='int64')
for i in np.arange(np.size(uniq[1])):
    if uniq[1][i] > 1:
        tmp = np.append(tmp, uniq[0][i])
print(tmp, 'Максимальный элмент из неуникальных:', np.max(tmp))
