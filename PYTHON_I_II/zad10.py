word_new=''
with open('text.txt','r') as f:
	for line in f:
		for word in line.split():
			if word == "i": 
				word="oraz"
			elif word == "I":
				word="Oraz"
			elif word == "oraz":
				word="i" 
			elif word == "Oraz":
				word="I"
			elif word ==  "nigdy":
				word="prawie nigdy"
			elif word == "Nigdy":
				word="Prawie nigdy"
			elif word == "dlaczego":
				word="czemu"
			elif word == "Dlaczego":
				word="Czemu"
			word_new=word_new+' '+word
		word_new=word_new+'\n'
print(word_new)
f=open('text.txt', 'w')
f.write(word_new)
f.close()
