import numpy as np

"""
Найти максимальный элемент в одномерном массиве x среди элементов, перед которыми стоит нулевой. 
"""

arr = np.array([0, 1, 0, 2, 10, 0, 3]) # max -> 3
nums = np.array([], dtype='int64')
for i in np.arange(1, np.size(arr)):
    if arr[i - 1] == 0:
        nums = np.append(nums, arr[i])
print('Максимальный элемент: ', np.max(nums))
