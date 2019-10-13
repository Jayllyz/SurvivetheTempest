#coding:utf-8
"""
Modules pour la météo
Pourcentage sans la tempête : Soleil[20% de chance], Pluie[20% de chance], Nuageux[50% de chance], Canicule[10% de chance]
Avec tempête possible : Pluie[20%], Soleil[20%], Canicule[20%], Nuageux[20%] et Tempête[20%]

"""

from modules.aleatoire import nombre_alea


def gen_meteo(jour):
     meteo = nombre_alea(1,100)
     if jour  <= 93:
          if  1 <= meteo <= 10:
               meteo = "Canicule"
          elif 10 < meteo <= 35:
               meteo = "Pluie"
          elif 35 < meteo <= 60:
               meteo = "Soleil"
          else:
               meteo = "Nuageux"
     if jour > 93:
          if   1 <= meteo <= 20:
               meteo = "Canicule"
          elif 20 < meteo <= 40:
               meteo = "Pluie"
          elif 40 < meteo <= 60:
               meteo = "Soleil"
          elif 60 < meteo <= 80:
               meteo = "Nuageux"
          elif 80 < meteo <=100:
               meteo = "Tempete"
     return meteo