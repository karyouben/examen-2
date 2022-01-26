# -*- coding: utf-8 -*-
'''
Created on 24 ene 2022

@author: willi
'''
from datetime import datetime

def parsea_fecha(cadena):
    return datetime.strptime(cadena, '%d/%m/%Y').date()