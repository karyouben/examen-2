# -*- coding: utf-8 -*-
'''
Created on 24 ene 2022

@author: willi
'''
from collections import namedtuple
import csv
import statistics
from parsers import *
from collections import Counter

Videos = namedtuple('Videos','id,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes')

def lee_trending_videos(fichero):
    with open(fichero,encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=";")
        next(lector)
        res =[]
        for id_video,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes in lector:
            tupla_videos = Videos(id_video,parsea_fecha(fecha_trending),titulo,canal,categoria,int(visitas),int(likes),int(dislikes))
            res.append(tupla_videos)
    return res

    
def media_visitas(registros,fecha):
    visitas = [t.visitas for t in registros if t.fecha_trending== fecha]
    media = 0
    if len(visitas)>0:
        media= sum(visitas)/len(visitas)
    return media
    
                    
