word_new=''
with open('text.txt','r') as f:
	for line in f:
		for word in line.split():
			if(word.lower() == "się" or word.lower() =="i" or word.lower()=="oraz" or word.lower()=="nigdy" or word.lower() =="dlaczego"):
				word=""
			else:
				word_new=word_new+' '+word
		word_new=word_new+'\n'
print(word_new)
f=open('text.txt', 'w')
f.write(word_new)
f.close()
