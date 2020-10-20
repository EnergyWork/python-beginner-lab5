import numpy as np
import timeit

"""
Определите, является ли массив логическим квадратом (суммы по всем горизонталям, вертикалям и двум диагоналям равны).
"""

# with open('.\\input-task5.txt', 'w') as f:
#     arr = np.random.randint(0, 9, size=(5, 5), dtype='int64')
#     np.savetxt(f, arr, delimiter=' ', fmt='%i')

matr = np.loadtxt('.\\input-task5.txt', dtype='int64', delimiter=' ')
tmp = matr[0:matr.shape[1], 0]
print(matr)

def check_columns():
    for i in np.arange(1, matr.shape[1]):
        t1 = matr[0:matr.shape[1], i]
        if np.sum(t1) != np.sum(tmp):
            return False
    else:
        return True

def check_rows():
    for i in np.arange(1, matr.shape[0]):
        t1 = matr[i]
        if np.sum(t1) != np.sum(tmp):
            return False
    else:
        return True

def check_diagonals():
    t1 = np.sum(np.diagonal(matr))
    t2 = np.sum(np.diagonal(np.rot90(matr)))
    if np.sum(t1) != np.sum(t2) != np.sum(tmp):
        return False
    else:
        return True

if check_columns() and check_rows() and check_diagonals():
    print('Матрица является логическим квадратом')
else:
    print('Матрица не является логическим квадратом')
 
print(timeit.timeit(setup="""import numpy as np""", stmt="""np.sum(np.diagonal(np.rot90(matr)))""", number=1000, globals=globals()))
print(timeit.timeit(setup="""import numpy as np""", stmt="""np.rot90(matr).trace()""", number=1000, globals=globals()))
print(timeit.timeit(setup="""import numpy as np""", stmt="""matr[:,::-1].trace()""", number=1000, globals=globals()))
print(timeit.timeit(setup="""import numpy as np""", stmt="""matr[:][::-1].trace()""", number=1000, globals=globals()))
