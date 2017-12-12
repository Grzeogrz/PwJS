#/bin/bash

echo "Podaj dowolna liczbe: "
read a
if [ $a -gt 20 ]
then
	echo $(lscpu | head -1) 
fi
