import random
n=8
mat1=[[0]*n for i in range(n)]
mat2=[[0]*n for i in range(n)]
mat3=[[0]*n for i in range(n)]

for i in range(n):
	for j in range(n):
		mat1[i][j]=random.randint(0,9)
		mat2[i][j]=random.randint(0,9)
for i in range(n):
	for j in range(n):
		for k in range(n):
			mat3[i][j]=mat3[i][j]+mat1[i][k]*mat2[k][j]
print(mat1)
print(mat2)
print(mat3)
