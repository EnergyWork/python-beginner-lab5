import numpy as np
import random

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
