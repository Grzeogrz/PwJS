import os
import _thread
import time
import random
import threading

class diningPhilo:
  def __init__(self, id, w1, w2):
    self.w1=w1
    self.w2=w2
    self.id=id
  def start(self):
    while True:
      time.sleep(random.randint(0,4))
      if self.w1.acquire(False):
        if self.w2.acquire(False):
          print("Filozof ", self.id, " zajada")
          time.sleep(random.randint(0,4))
          print("Filozof " ,self.id," skonczyl")
          self.w1.release()
          self.w2.release()
        else:
          self.w1.release()

           
          
if(__name__ == "__main__"):
  numOfPhil=5
  widelce=[threading.Lock() for i in range(numOfPhil)]
  philos=[diningPhilo(i,widelce[i],widelce[(i+1)%numOfPhil]) for i in range(numOfPhil)]
  for p in philos:  
    _thread.start_new_thread(p.start,())
  time.sleep(40)
