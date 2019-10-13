# Créé par david.antony, le 12/02/2019 en Python 3.2
#coding:utf-8
"""
Modules de la gestion de sauvegarde de la partie du joueur
"""
from modules.personnage import Personnage
from modules.fichier import if_exist


def save(Yaath,dico_batiments,dico_maps):
    save_file = open("data/save.stt","w")
    save_file.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(Yaath.bois,Yaath.eau,Yaath.viande,Yaath.pierre,Yaath.cuivre,Yaath.fer,Yaath.gold,Yaath.jour,dico_batiments.get("atelier").niveau,dico_batiments.get("mine").niveau,dico_batiments.get("puit").niveau,dico_batiments.get("abri").niveau,dico_batiments.get("scierie").niveau, Yaath.tile_x, Yaath.tile_y))  
    save_file.close()
    


def load(Yaath,dico_maps,dico_batiments):
    if if_exist("data/save.stt"):
        save_file = open("data/save.stt","r") 
        i = 0
        bois =""
        eau = ""
        viande = ""
        pierre = ""
        cuivre = ""
        fer = ""
        gold = ""
        jour = ""
        atelier = ""
        mine = "" 
        abri = ""
        puit = ""
        scierie = ""
        tile_x = ""
        tile_y = ""

    while i < 15:
         if i == 0:
            bois = save_file.readline()
            bois = bois[0:-1] 
            bois = int(bois)
         
         elif i == 1:
            eau = save_file.readline()
            eau = eau[0:-1]
            eau = int(eau)
         
         elif i == 2:
            viande = save_file.readline()
            viande = viande[0:-1]
            viande = int(viande)
         
         elif i == 3:
            pierre = save_file.readline()
            pierre = pierre[0:-1]
            pierre = int(pierre)
         
         elif i == 4:
            cuivre = save_file.readline()
            cuivre = cuivre[0:-1]
            cuivre = int(cuivre)
         
         elif i == 5:
            fer = save_file.readline()
            fer = fer[0:-1]
            fer = int(fer)
         
         elif i==6:
            gold = save_file.readline()
            gold = gold[0:-1]
            gold = int(gold)
         
         elif i==7:
            jour = save_file.readline()
            jour = jour[0:-1]
            jour = int(jour)

         elif i==8:  
            atelier = save_file.readline()
            atelier = atelier[0:-1]
            atelier = int(atelier)
        
         elif i==9:  
            mine = save_file.readline()
            mine = mine[0:-1]
            mine = int(mine)
         elif i==10:  
            abri = save_file.readline()
            abri = abri[0:-1]
            abri = int(abri)
         
         elif i==11:  
            puit = save_file.readline()
            puit = puit[0:-1]
            puit = int(puit)
         
         elif i==12:  
            scierie = save_file.readline()
            scierie = scierie[0:-1]
            scierie = int(scierie)

         elif i==13:  
            tile_x = save_file.readline()
            tile_x = tile_x[0:-1]
            tile_x = int(tile_x)

         elif i==14:  
            tile_y = save_file.readline()
            tile_y = tile_y[0:-1]
            tile_y = int(tile_y)
         
         
         i+=1
    save_file.close()
    
    Yaath.bois = bois
    Yaath.eau = eau 
    Yaath.viande= viande 
    Yaath.pierre = pierre
    Yaath.cuivre = cuivre 
    Yaath.fer = fer
    Yaath.gold = gold
    Yaath.jour = jour 
    Yaath.current_map = dico_maps.get("map2")
    Yaath.current_char = Yaath.char_north

    dico_batiments.get("atelier").niveau = atelier
    dico_batiments.get("mine").niveau = mine
    dico_batiments.get("abri").niveau = abri
    dico_batiments.get("scierie").niveau = scierie
    dico_batiments.get("puit").niveau = puit

    Yaath.tile_x = tile_x
    Yaath.tile_y = tile_y

    Yaath.x = Yaath.tile_x*32
    Yaath.y = Yaath.tile_y*32
