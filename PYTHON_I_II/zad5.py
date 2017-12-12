import os

list=[]
path="/home"
list.append(path)

while len(list):
	next=list.pop()+'/'
	print(next)
	for i in os.listdir(next):
		if os.path.isdir(next+i):
			list.append(next+i)
