print("Prosze zaprogramowac zamek wpisując 4 cyfrowy kod")
kod=input("KOD:")
while len(kod) != 4: 
	kod=input("KOD:")
print("Hasło zostało ustawione")

proba=input("Podaj haslo:")

while proba != kod:
	proba=input("Bledne haslo! \n KOD:")
print("Haslo poprawne, ZAPRASZAMY!")
