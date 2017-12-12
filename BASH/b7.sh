#!/bin/bash
echo "Podaj dzialanie"
rownanie=""
while [[ $rownanie != "q" ]]
do
read rownanie
echo "$rownanie = $((rownanie))"
done

