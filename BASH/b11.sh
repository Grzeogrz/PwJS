#!/bin/bash

for i in *.jpg
do convert "$i" "${i%.*}.png"
done
