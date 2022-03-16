#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:22:06 2022

@author: antalv05
"""
#para garantizar la exclusión mutua nos fijaremos en los usuarios en vez de en
#los tenedores.
#solo puede pensar cuando el otro este comiendo.
#hasta que esten dos tenedores libres no comer. otra posibilidad.

from multiprocessing import Process
from multiprocessing import Condition, Lock
from multiprocessing import Array, Manager
import time
import random

Nphil = 5
K = 100

class Table:
    def __init__(self,freefork,set_current_phil):
        manager=Manager()
        self.phil=manager.list(True for i in range (Nphil))
        self.mutex=lock()
        self.freefork=Condition(self.mutex)
        self.set_current_phil=None
        
    def set_current_phil(self,set_current_phil):
        #sirve para saber que filosofo esta comiendo.
        return self.set_current_phil
    def no_comen_lados(self):
        if phil[i+1]==False and phil[i-1]==False:
            phil[i]=True
            return i
        
    def wants_eat(self,i,phil):
        #inv y ¬phil[i]
        if 0<=self.eating<=Nphil and phil[i]==False:
           #freefork.wait (¬phil[i-1]^¬phil[i+1])
           self.freefork(set_current_phil)
           phil[i]=True
           eating+=1
           #el phil i pasa a comer
    def wants_think(self,i):
        #inv y phil[i]
        if 0<=self.eating<=Nphil and phil[i]==False:
           #no rompe el invariante no hace falta poner wait.
           phil[i]=False
           eating-=1
           freefork.signal(no_comen_lados(self))
#con el problema de filosofos resuelto con semaforos se quedaba bloqueado
#aqui no, pues cada vez miro si los demás están comiendo.
        
class CheatMonitor:
    def __init__(self):
        manager=Manager()
        self.hungry=manager.list(True for i in range (Nphil))
        self.eating=Value('i',0)
        self.mutex=lock()
        self.other_eating=condition(self.mutex)
    def wants_think(self,i):
        self.mutex.acquire()
        eating-=1
    def is_eating(self,i):
        self.mutex.acquire()
        self.eating.value+=1
        self.other.eating.notify()
        self.mutex.release()
    def want_eat():
        if hungry[i]==True:
            phil[i]==False
        else:
            phil[i]==True
        if 0<=self.eating<=Nphil and phil[i]==False:
            hungry.acquire(hungry[i+1]==False)
            hungry[i]=True
            freefork.wait(phil[i+1]==False and phil[i-1]==False)
            phil[i]=True
            eating+=1
            hungry[i]=False
            hungry.signal()