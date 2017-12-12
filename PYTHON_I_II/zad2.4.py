#!/usr/bin/python

import random
from multiprocessing import Pool
import multiprocessing as mp
from multiprocessing import Process
from multiprocessing import Lock, Array



def dohist(size):
    lista = [0]*40
    return lista

def hist(lista, histogram, lk):
    for l in lista:
        histogram[l] = histogram[l] + 1
    return histogram

def dolist(size):
    lista = []
    for i in range(0,100):
        lista.append(random.randint(0, 39))
    return lista
    
l = Lock()
pool = Pool(processes=2) 
lista = dolist(100)
histogram = dohist(40)
hist(lista, histogram, l)

arr = Array('i', range(40))
for k in range(0,40):
    arr[k] = 0

p1 = Process(target=hist, args=(lista[0:50], arr, l))
p2 = Process(target=hist, args=(lista[50:100], arr, l)) 
p1.start()
p2.start()

p1.join()
p2.join()

for i in range(0,40):
    print(arr[i] - histogram[i])

for i in range(0,40):
    print(arr[i])

