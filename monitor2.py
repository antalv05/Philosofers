#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:10:22 2022

@author: antalv05
"""

#para garantizar la exclusión mutua nos fijaremos en los usuarios en vez de en
#los tenedores.
#solo puede pensar cuando el otro este comiendo.
#hasta que esten dos tenedores libres no comer. otra posibilidad.

from multiprocessing import Process
from multiprocessing import Condition, Lock
from multiprocessing import Array, Manager,Value
import time
import random

Nphil = 5
K = 100

class Table:
    def __init__(self,NPhil,manager):
        self.fforks=manager.list([True for i in range (Nphil)])
        self.mutex=Lock()
        self.free_fork=Condition(self.mutex)
        self.current_phil=None
        self.NPhil=Nphil
        
    def set_current_phil(self,NPhil):
        #sirve para saber que filosofo esta comiendo.
        self.current_phil=NPhil #filosofo en cuestión

    def get_current_phil(self):
        return self.current_phil #me devuelve el filosofo.
    
    def no_comen_lados(self):
        phil=self.current_phil
        return self.fforks[phil] and self.fforks[(phil+1)%self.NPhil]
    def wants_eat(self,phil):
        #inv y ¬phil[i]
        self.mutex.acquire()
        self.free_fork.wait_for(self.no_comen_lados)
        self.fforks[phil]=False 
        self.fforks[(phil+1)%self.NPhil]=False 
        self.mutex.release()
           #el phil i pasa a comer
    def wants_think(self,phil):
        #inv y phil[i]
        self.mutex.acquire()
        self.fforks[phil]=True
        self.fforks[(phil+1)%self.NPhil]=True
        self.free_fork.notify_all()
        self.mutex.release()
#con el problema de filosofos resuelto con semaforos se quedaba bloqueado
#aqui no, pues cada vez miro si los demás están comiendo.
        
class CheatMonitor:
    def __init__(self):
        #manager=Manager()
        #self.hungry=manager.list(True for i in range (Nphil))
        self.eating=Value('i',0)
        self.mutex=Lock()
        self.other_eating=Condition(self.mutex)
    def wants_think(self,i):
        self.mutex.acquire()
        self.other_eating.wait_for(lambda: self.eating.value==2)
        self.eating.value-=1
        self.mutex.release()
    def is_eating(self,i):
        self.mutex.acquire()
        self.eating.value+=1
        self.other.eating.notify()
        self.mutex.release()
"""
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
"""