#!/bin/bash

echo "Podaj cztero cyfrowy kod:"
read -s  haslo
echo "Podaj haslo: "
read -s pasword
if [ $haslo = $pasword ]
then
	echo "Haslo poprawne, zapraszamy!"
else
	echo "Haslo błędne."
fi
