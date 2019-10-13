#coding:utf-8


"""

    Fichier qui gère la nouvelle partie

"""

import pygame
import time
from modules.partie import deroulement_partie
from modules.texte import print_text


def nouvelle_partie(ecran, font_jeu, font_hud, dico_controles, Yaath,dico_maps,dico_batiments,  boite):

    quitter = False

    quitter = introduction(ecran, font_jeu, dico_controles)
    if not quitter :
        Yaath.eau = 5
        Yaath.viande = 5
        Yaath.bois = 5
        Yaath.pierre = 5
        Yaath.cuivre = 0
        Yaath.fer = 0
        Yaath.gold = 1
        Yaath.tile_x = 12
        Yaath.tile_y = 11
        Yaath.x = Yaath.tile_x*32
        Yaath.y = Yaath.tile_y*32
        Yaath.jour = 1
        Yaath.current_char = Yaath.char_south
        Yaath.current_map = dico_maps.get("map1")
        dico_batiments.get("abri").niveau = 0
        dico_batiments.get("atelier").niveau = 0
        dico_batiments.get("puit").niveau = 0
        dico_batiments.get("mine").niveau = 0
        dico_batiments.get("scierie").niveau = 0
        quitter = deroulement_partie(ecran, font_jeu, font_hud, dico_controles, Yaath, dico_maps,dico_batiments, boite)

    return quitter



def introduction(ecran, font_jeu, dico_controles):

    quitter_jeu = False
    boucle = True


    

    while boucle:
        
        ecran.fill((255,255,255))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boucle = False
                quitter_jeu = True
            elif event.type == pygame.KEYDOWN:
                if event.key == dico_controles.get("action"):
                    boucle = False

        print_text("Durant mon voyage en mer, moi et mon équipage avons dû faire face à une tempête.", True, (0,0,0), (0,152-76), font_jeu, ecran, True, False)
        print_text("Malheureusement pour moi j'ai été éjecté du navire sur une de nos barques.", True, (0,0,0),(0,152),font_jeu,ecran, True, False)
        print_text("Je me suis échoué sur cette île, ma barque s'est brisée,", True, (0,0,0),(0,152+76),font_jeu,ecran, True, False)
        print_text("je dois attendre que mon équipage vienne me chercher, je n'ai pas beaucoup de temps", True, (0,0,0),(0,152+76*2),font_jeu,ecran, True, False)
        print_text("pour me construire un abri, la tempête va revenir d'ici une vingtaine de jours.", True, (0,0,0),(0,152+76*3),font_jeu,ecran, True, False)
        print_text("Je dois me limiter à trois actions par jour sous risque de manquer d'eau", True, (0,0,0),(0,152+76*4),font_jeu,ecran, True, False)
        print_text("Appuyer sur la touche Action pour continuer", True, (0,42,178),(0,152+76*5),font_jeu,ecran, True, False)

        pygame.display.flip()


    return quitter_jeu





