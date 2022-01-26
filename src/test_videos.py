# -*- coding: utf-8 -*-
'''
Created on 24 ene 2022

@author: willi
'''

from videos import *

def test_lee_trending_videos(fichero):
    res = lee_trending_videos(fichero)
    print(f"Leidos {len(res)} vídeos")
    print(f"los tres primeros vídeos son: ", res[:3])
    print(f"Los tres últimos vídeos son: ", res[-3:])
    print("")

def test_media_visitas(registros,fecha):
    res = media_visitas(registros,fecha)
    print(f"La media de visitas del dia {fecha} es {res}")
    print("")

def test_video_mayor_ratio_likes_dislikes(registros,categoria=None):
    res = video_mayor_ratio_likes_dislikes(registros,categoria)
    print(f"El video con mayor ratio de todos es: ")
    print(res)
    print(f"El video con mayor ratio de la categoria {categoria} es: ")
    print(res)
    print("")



def main():
    fichero = ('../data/MX_Youtube_2017_utf8.csv')
    REGISTROS = lee_trending_videos(fichero)
    test_lee_trending_videos(fichero)
    test_media_visitas(REGISTROS,'11/1/2017')
    #test_video_mayor_ratio_likes_dislikes(REGISTROS,'Education')
if __name__=="__main__":
    main()
