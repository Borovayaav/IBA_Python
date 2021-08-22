import numpy as np
import random
n=int(input("Введите количество строк и столбцов:\n"))
rmat = [[random.randint(0,9) for j in range(n)] for i in range(n)]
sim=("  ")
A=np.array(rmat)
print(A)
for k in range(0, n-1):
    for l in range(k+1,n):
        if A[k][l]!=A[l][k]:
            sim=("False")
            break
if sim==("False"):
    print("Введенная матрица несиметрична")
else:
    print("Матрица симметрична")

    

   