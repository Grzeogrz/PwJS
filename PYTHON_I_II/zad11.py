
a=[1,2,12,4]
b=[2,3,2,8]

def iloczyn(a, b):
	c=0
	for i in range(len(a)):
		c=c+a[i]*b[i]
	return c

print("Iloczyn skalarny wynosi: ", iloczyn(a,b))
