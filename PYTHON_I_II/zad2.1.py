f=open('file.txt', 'r')
print("Zawartosc pliku: ", f.read())
f.close()

f=open('file.txt', 'w')
content=input("Co wpisac do pliku: ")
f.write(content)
f.close()

f=open('file.txt', 'r')
print("Zawartosc po wpisaniu: ", f.read())
f.close()
