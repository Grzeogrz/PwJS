#!/bin/bash
pass="1234"

for i in {1..3}
do
	echo "Podaj haslo: "
	read -s haslo
	if [ $haslo = $pass ]
	then
		ls -a ../
		break
	else
		if [ $i -eq 3 ]
		then 
			echo "Podano 3 razy niepoprawne hasło, blokada konta"
		else
			echo "Haslo błędne, spróbuj ponownie: "
		fi
	fi
done
