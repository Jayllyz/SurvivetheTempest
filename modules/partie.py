#coding:utf-8

import pygame
from modules.tiles import Tiles
from modules.map import Map
from modules.meteo import gen_meteo
from modules.ressources import conso
from modules.batiments import Batiments, Atelier,Mine, Abri, Scierie, Puit
from modules.sauvegarde import save
from modules.texte import print_text


def deroulement_partie(ecran, font_jeu, font_hud, dico_controles, Yaath, dico_maps,dico_batiments, boite):
   win = False
   lose = False 
   quitter = False 
   retour_menu = False

  
   while win == False and lose == False and quitter == False:
        quitter, win, lose , retour_menu = jour(Yaath,font_hud, font_jeu, ecran, dico_controles, dico_maps, dico_batiments,boite)
        if quitter:
            return quitter
        elif retour_menu:
            return quitter
        elif win == True: 
            quitter = gagner(dico_controles, ecran, font_jeu)
            return quitter
        elif lose == True: 
            quitter = perdre(dico_controles, ecran, font_jeu, "tempete")
            return quitter
        quitter, lose = nuit(Yaath, dico_batiments, dico_maps)
        if quitter:
            return quitter
        elif lose == True: 
            quitter = perdre(dico_controles, ecran, font_jeu, "conso")
            return quitter
        




def jour(Yaath,font_hud, font_jeu, ecran, dico_controles, dico_maps,dico_batiments, boite):
    quitter = False
    win = False
    lose = False
    boucle = True
    retour_menu = False


    if Yaath.jour == 1:
        meteo = "Pluie"
    else:
        meteo = gen_meteo(Yaath.jour)
    
    action_faite = 0
    passer_jour = False
    
    while boucle :
        
        pygame.time.Clock().tick(20)

        Yaath.current_map.afficher(ecran)
        ecran.blit(Yaath.current_char, (Yaath.x,Yaath.y))
        if Yaath.current_map == dico_maps.get("map2"):
            Yaath.hud(ecran, font_hud, meteo)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boucle = False
                quitter = True

            elif event.type == pygame.KEYUP:
                if event.key == dico_controles.get("retour"):
                    boucle = False
                    retour_menu = True
                
                elif event.key == dico_controles.get("action"):
                    quitter, passer_jour, win, lose, action_faite = Yaath.action(ecran, boite, font_jeu, dico_controles, action_faite, meteo, dico_batiments, font_hud)
                    if quitter:
                        boucle = False
                    if passer_jour:
                        boucle = False
                        return quitter, win, lose, retour_menu
                    if win or lose:
                        boucle = False
                     

                
            elif event.type == pygame.KEYDOWN:
                if event.key == dico_controles.get("haut"):
                    Yaath.deplacement("haut",dico_maps)
                elif event.key == dico_controles.get("bas"):
                    Yaath.deplacement("bas",dico_maps)
                elif event.key == dico_controles.get("gauche"):
                    Yaath.deplacement("gauche",dico_maps)
                elif event.key == dico_controles.get("droite"):
                    Yaath.deplacement("droite",dico_maps)

        pygame.display.flip()
    
    return quitter, win, lose, retour_menu

def nuit(Yaath, dico_batiments, dico_maps):
    quitter = False
    lose = False
    conso(Yaath, dico_batiments)
    if Yaath.eau < 0 or Yaath.viande < 0:
        lose = True
        return quitter, lose
    if not lose:
        if Yaath.jour == 1:
            dico_batiments.get("abri").niveau = 1
        Yaath.jour +=1
        save(Yaath, dico_batiments, dico_maps)

    return quitter, lose
    

def gagner(dico_controles, ecran, font_jeu):
    boucle = True
    quitter = False

    while boucle:
        ecran.fill((255,255,255))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boucle = False
                quitter = True
            elif event.type == pygame.KEYDOWN:
                if event.key == dico_controles.get("action"):
                    boucle = False


        print_text("Félicitation ! Vous avez survécu !(Appuyé sur action pour continuer)", True, (0,185,255), (0,0), font_jeu, ecran, True, True)

        pygame.display.flip()
    
    return quitter

def perdre(dico_controles, ecran, font_jeu, raison):
    boucle = True
    quitter = False

    while boucle:
        ecran.fill((255,255,255))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boucle = False
                quitter = True
            elif event.type == pygame.KEYDOWN:
                if event.key == dico_controles.get("action"):
                    boucle = False

        if raison == "conso":
            print_text("Vous n'aviez pas assez de vivres... (Appuyé sur action pour continuer)", True, (255,28,0), (0,0), font_jeu, ecran, True, True)
        else:
            print_text("Votre abri n'a pas résisté... (Appuyé sur action pour continuer)", True, (255,28,0), (0,0), font_jeu, ecran, True, True)
        pygame.display.flip()
    
    return quitter