# -*- coding: utf-8 -*-
'''
Created on 24 ene 2022

@author: willi
'''
from datetime import datetime

def parsea_booleano(cadena):
    res=None
    cadena=cadena.upper()
    if cadena=='VERDADER':
        res =True
    elif cadena =='FALSO':
        res =False
    return res

def parsea_fecha(cadena):
    return datetime.strptime(cadena, '%d/%m/%Y').date()