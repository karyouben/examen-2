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
        for id,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes in lector:
            fecha = datetime.strptime(fecha_trending, '%d/%m/%Y')
            visitas=int(visitas)
            likes=int(likes)
            dislikes=int(dislikes)
            tupla_videos = Videos(id,fecha,titulo,canal,categoria,visitas,likes,dislikes)
            res.append(tupla_videos)
    return res

    
def media_visitas(registros,fecha_dada):
    fecha_dada = datetime.strptime(fecha_dada, '%d/%m/%Y').date()
    visitas = [r.visitas for r in registros if r.fecha_trending==fecha_dada]
    media = 0
    if len(visitas)>0:
        media = sum(visitas)/len(visitas)
    return media

def video_mayor_ratio_likes_dislikes(registros,categoria=None):
    res = [t for t in registros if (t.categoria == categoria or categoria == None) and t.dislikes>0]
    return max(res, key=lambda x:x.likes/x.dislikes)

def videos_por_canal(registros):
    dicc= {}
    for t in registros:
        clave = t.canal
        if clave in dicc:
            dicc[clave]+= 1
        else:
            dicc[clave] = 1
    return dicc
def videos_por_canal_2(registros):
    return Counter(t.canal for t in registros)

def canales_top(registros,n=3):
    dicc= videos_por_canal(registros)
    return sorted(dicc.items(), key=lambda x:x[1],reverse= True)[:n]

def canales_top_2(registros,n=3):
    dicc = videos_por_canal_2(registros)
    return dicc.most_common(n)

def videos_por_categoria(registros):
    dicc ={}
    for t in registros:
        clave = t.categoria
        if clave in dicc:
            dicc[clave].append(t)
        else:
            dicc[clave]= [t]   
    return dicc
def likeability(t,k):
    return(k*t.likes -t.dislikes)/(k*t.visitas)
def video_mas_likeability_por_categoria(registros,k=20):
    dicc= videos_por_categoria(registros)
    res = {}
    for clave,valor in dicc.items():
        tupla_max = max(valor, key=lambda x:likeability(x,k))
        res[clave]= tupla_max.id_video
    return res

def incrementos_visitas(registros,canal):
    diccionario = agrupa_por_fecha(registros, canal)
    lista_ordenada = sorted(diccionario.items())
    lista_incremento = incremento_visitas_por_fecha(lista_ordenada, diccionario)
    return lista_incremento


def agrupa_por_fecha(registros,canal):
    dicc={}
    for t in registros:
        if t.canal==canal:
            clave= t.fecha_trending
            if clave in dicc:
                dicc[clave]+= t.visitas
            else:
                dicc[clave] = t.visitas
    return dicc

def incremento_visitas_por_fecha(registros,canal):
    res= []
    for indx in range(len(registros)-1):
        visitas1= registros[indx][1]
        visitas2= registros[indx+1][1]
        incremento = (visitas2-visitas1)/visitas1
        fecha_ref = registros[indx+1][0]
        res.append((fecha_ref,incremento))
    return res