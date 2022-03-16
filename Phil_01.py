#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:05:14 2022

@author: alumno
"""

from multiprocessing import Process
from multiprocessing import Condition, Lock
from multiprocessing import Array, Manager
import time
import random

from monitor import Table
#hay un fichero que se llama asi.

Nphil = 5
K = 100

def delay(n):
    time.sleep(random.random()/n)

def philosopher_task(num:int, table: Table):
    table.set_current_phil(num)
    while True:
         print (f"Philosofer {num} thinking")
         print (f"Philosofer {num} wants to eat")
         table.wants_eat(num)
         print (f"Philosofer {num} eating")
         table.wants_think(num)
         print (f"Philosofer {num} stops eating")

def main():
   manager = Manager()
   table = Table(Nphil, manager)
   philosofers = [Process(target=philosopher_task, args=(i,table)) \
                  for i in range(Nphil)]
   for i in range(Nphil):
      philosofers[i].start()
   for i in range(Nphil):
      philosofers[i].join()

if __name__ == '__main__':    
     main()