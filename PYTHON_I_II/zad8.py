import random
n=50
tab=[]
for i in range(n):
	tab.append(random.randint(0,9))

print(tab)
tab2=sorted(tab,reverse=True)

zmiana=1
while zmiana !=0:
	zmiana=0
	for i in range(n-1):
		if(tab[i]<tab[i+1]):
			zmiana=zmiana+1
			pomoc=tab[i]
			tab[i]=tab[i+1]
			tab[i+1]=pomoc
			
print("Po sortowaniu:")
print(tab)

for i in range(n):
	if tab[i]!=tab2[i]:
		print("BLAD")

print("OK")
