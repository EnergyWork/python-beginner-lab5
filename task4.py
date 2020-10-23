import numpy as np
import colorama
from colorama import Fore, Back, Style

"""
Элемент матрицы называется локальным минимумом, 
    если он строго меньше всех имеющихся у него соседей. 
Соседями элемента Аij в матрице назовем элементы Аkl, 
    где i-1<=k<=i+1, j-1 < l <j+1, (k, l)  (i, j). 
Подсчитать количество локальных минимумов заданной в файле input.txt матрицы размером 10 на 10. 
"""

# with open('.\\input.txt', 'w') as f:
#     arr = np.random.randint(0, 9, size=(10, 10), dtype='int64')
#     np.savetxt(f, arr, delimiter=' ', fmt='%i')

matr = np.loadtxt('.\\input.txt', dtype='int64', delimiter=' ')
#print(matr)

def local_min(i, j, elem, left=False, right=False, top=False, bottom=False):
    if left:
        if elem >= matr[i][j - 1]:
            return False
    if right:
        if elem >= matr[i][j + 1]:
            return False
    if top:
        if elem >= matr[i - 1][j]:
            return False
    if bottom:
        if elem >= matr[i + 1][j]:
            return False
    return True

def check(i, j, elem):
    if i == 0:
        if j == 0:
            return 1 if local_min(i, j, elem, right=True, bottom=True) else 0
        elif j == matr.shape[1] - 1:
            return 1 if local_min(i, j, elem, left=True, bottom=True) else 0
        else:
            return 1 if local_min(i, j, elem, left=True, right=True, bottom=True) else 0
    elif j == 0:
        if i == matr.shape[0] - 1:
            return 1 if local_min(i, j, elem, right=True, top=True) else 0
        else:
            return 1 if local_min(i, j, elem, right=True, top=True, bottom=True) else 0
    elif i == matr.shape[0] - 1:
        if j == matr.shape[1] - 1:
            return 1 if local_min(i, j, elem, left=True, top=True) else 0
        else:
            return 1 if local_min(i, j, elem, left=True, right=True, top=True) else 0
    elif j == matr.shape[1] - 1:
        return 1 if local_min(i, j, elem, left=True, top=True, bottom=True) else 0
    else:
        return 1 if local_min(i, j, elem, left=True, right=True, top=True, bottom=True) else 0

colorama.init()
local_mins_counter = 0
for i, row in enumerate(matr):
    for j, elem in enumerate(row):
        if check(i, j, elem):
            local_mins_counter += 1
            print(Fore.GREEN + str(elem), end=' ')
        else:
            print(Fore.RED + str(elem), end=' ')
    print('\n')
print(f'Количество локальных минимумов: {local_mins_counter}')
