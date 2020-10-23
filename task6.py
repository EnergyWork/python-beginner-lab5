import numpy as np

"""
Программным образом заполните массив одним из двух следующих способов. 
Размерность n и m, а также номер способа заполнения вводится пользователем при запуске программы.
Способ 1.
	1		3		4		10		11		21
	2		5		9		12		20		22
	6		8		13		19		23		30
	7		14		18		24		29		31
	15		17		25		28		32		35
	16		26		27		33		34		36
Способ 2
	1		2		3		4		5		6
	20		21		22		23		24		7
	19		32		33		34		25		8
	18		31		36		35		26		9
	17		30		29		28		27		10
	16		15		14		13		12		11
Результат записать в файл.
"""

n = int(input("Введите кол-во строк: "))
m = int(input("Введите кол-во столбцов: "))
method = int(input("Введите способ заполнения матрицы(1, 2): "))
if n == m == 1:
    print('Всего один элемент\n', 1)
    exit(0)

matr = np.zeros((n, m), dtype=np.int32)
arr = np.linspace(1, n * m, n * m, dtype=np.int32)

def side_swith(side, right=False, left=False, top=False, bottom=False):
    side['right'] = right
    side['left'] = left
    side['top'] = top
    side['bottom'] = bottom

def method1():
    i, j, ii = 0, 0, 0 # начальные значения в матрице и индекс зачения, которое берем(последовательно друг за другом)
    top = False # напрвление заполнения по диагонали
    while True:
        matr[i][j] = arr[ii]
        # начинаем с верхнего леваого угла
        if i == j == 0:
            i += 1
            top = True
        # если в нижнем правом углу, то конец и выходим из цикла
        elif i == n - 1 and j == m - 1:
            break
        # дошли до границы сверху
        elif i == 0 and j != m - 1:
            if top:
                j += 1
                top = False
            else: # if not top
                i += 1
                j -= 1
        # дошли до границы слева
        elif j == 0:
            if top:
                i -= 1
                j += 1
            else: # if not top
                i += 1
                top = True
        # дошли до границы снизу
        elif i == n - 1:
            if top:
                i -= 1
                j += 1
            else:
                j += 1
                top = True
        # дошли до границы справа
        elif j == m - 1:
            if top:
                i += 1
                top = False
            else:
                i += 1
                j -= 1
        # инче не граничное условие
        else:
            if top:
                i -= 1
                j += 1
            else:
                i += 1
                j -= 1
        ii += 1
    print(matr)

def method2():
    nn, mm = n, m
    i, j, ii = 0, 0, 0
    side = {
        'left' : False,
        'right' : True,
        'top' : False,
        'bottom' : False
    }
    while ii != np.size(arr):
        # если налево
        while j < mm and side['right']:
            matr[i][j] = arr[ii]
            j += 1
            ii += 1
        else:
            j -= 1
            i += 1
            side_swith(side, bottom=True)
        # если вниз
        while i < nn and side['bottom']:
            matr[i][j] = arr[ii]
            i += 1
            ii += 1
        else:
            nn -= 1
            i -= 1
            j -= 1
            side_swith(side, left=True)
        # если направо
        while j >= m - mm and side['left']:
            matr[i][j] = arr[ii]
            j -= 1
            ii += 1
        else:
            mm -= 1
            j += 1
            i -= 1
            side_swith(side, top=True)
        # если вверх
        while i >= n - nn and side['top']:
            matr[i][j] = arr[ii]
            i -= 1
            ii += 1
        else:
            i += 1
            j += 1
            side_swith(side, right=True)
    print(matr)

def save():
    np.savetxt('.\\output-task6.txt', matr, fmt='%i', encoding='utf-8')

if method == 1:
    method1()
    save()
elif method == 2:
    method2()
    save()
else:
    print('Такого метода нет')
