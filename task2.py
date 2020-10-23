import numpy as np

"""
Найти максимальный элемент в одномерном массиве x среди элементов, перед которыми стоит нулевой. 
"""
fl = False
arr = np.array([0, 2])
nums = np.array([], dtype='int32')
for i in np.arange(1, np.size(arr)):
    if arr[i - 1] == 0:
        nums = np.append(nums, arr[i])
else:
    if np.size(nums) != 0:
        fl = True

if fl:
    print('Максимальны элемент: ', np.max(nums))
else:
    print('Нет подходящих элементов')