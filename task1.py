import numpy as np
import random

"""
Сформировать одномерный массив, состоящий из n вещественных элементов co значением от -10.0 до 10.0. 
Для числа y, такого, что минимальный элемент массива < y < максимальный элемент массива, вычислить: 
    a.	произведение элементов массива, значения модуля которых больше модуля y,
    b.	сумму модулей остальных элементов
"""

n = 10 # int(input('Введите n: '))
arr = np.array([(10 - random.random() * 20) for _ in np.arange(n)]) # np.linespace(-10, 10, n)
print(arr)
max_elem = arr.max()
min_elem = arr.min()
for elem in arr:
    if min_elem < elem < max_elem:
        tmp1 = np.array(list(filter(lambda x: min_elem < np.fabs(x) < max_elem and np.fabs(x) > np.fabs(elem), arr)))
        tmp2 = np.array(list(filter(lambda x: min_elem < np.fabs(x) < max_elem and np.fabs(x) <= np.fabs(elem), arr)))
        print(f'{min_elem} < {elem} < {max_elem} \t Произведение: {np.prod(tmp1)} Сумма: {np.sum(tmp2)}')
