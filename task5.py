import numpy as np

"""
Определите, является ли массив логическим квадратом (суммы по всем горизонталям, вертикалям и двум диагоналям равны).
"""

# with open('.\\input-task5.txt', 'w') as f:
#     arr = np.random.randint(0, 9, size=(5, 5), dtype='int64')
#     np.savetxt(f, arr, delimiter=' ', fmt='%i')

matr = np.loadtxt('.\\input-task5.txt', dtype='int64', delimiter=' ')
print(matr)
print()

print('Суммы по столбцам')
for i in np.arange(0, 5):
    t1 = matr[0:5, i]
    print(np.sum(t1), end=' ')

print('\nСуммы по строкам')
for i in np.arange(0, 5):
    t1 = matr[i]
    print(np.sum(t1), end=' ')

print('\nДиагональ главная')
t1 = np.diagonal(matr)
print(t1)

print('Диагональ не главная')
t1 = np.diagonal(np.transpose(matr))
print(t1)
