import numpy as np

"""
Удалите строку и столбец, на пересечении которых находится минимальный элемент массива. 
После этого отсортируйте столбцы массива по неубыванию минимальных элементов в них.
"""

arr = np.random.randint(0, 10, (5, 5))
print(arr)
min_elem = np.min(arr)
print(min_elem)
x, y = np.where(arr == min_elem)
print(x[0], y[0])
arr = np.delete(arr, x[0], axis=0)
arr = np.delete(arr, y[0], axis=1)
print(arr)

sorted_arr = sorted(np.rot90(arr), key=lambda x: min(x), reverse=True)
print(sorted_arr)
print(np.rot90(sorted_arr, k=3))
