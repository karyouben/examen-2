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
    



def main():
    fichero = ('../data/MX_Youtube_2017_utf8.csv')
    REGISTROS = test_lee_trending_videos(fichero)
    test_lee_trending_videos(fichero)
    test_media_visitas(REGISTROS,'11/1/2017')
if __name__=="__main__":
    main()
