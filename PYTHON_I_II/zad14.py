import random
import numpy

a=random.randint(1,9)
matrix=[[0]*a for i in range(a)]

for i in range(a):
	for j in range(a):
		matrix[i][j]=random.randint(0,9)
print(matrix)

print("Wyznacznik macierzy rzędu ", a," wynosi: ",numpy.linalg.det(matrix))
