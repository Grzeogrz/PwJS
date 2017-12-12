import random
n=128
matrix1=[[0]*n for i in range(n)]
matrix2=[[0]*n for i in range(n)]
matrix3=[[0]*n for i in range(n)]

for i in range(n):
	for j in range(n):
		matrix1[i][j]=random.randint(0,9)
		matrix2[i][j]=random.randint(0,9)

for i in range(n):
	for j in range(n):
		matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
print(matrix1)
print(matrix2)
print(matrix3)
