import numpy as np

# with open('.\\input.txt', 'w') as f:
#     arr = np.random.randint(0, 9, size=(10, 10), dtype='int64')
#     np.savetxt(f, arr, delimiter=' ', fmt='%i')

matr = np.loadtxt('.\\input.txt', dtype='int64', delimiter=' ')
print(matr)

local_mins_counter = 0

for row in matr:
    for elem in row:
        print(elem)
