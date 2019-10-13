#coding:utf-8

import pygame
from modules.texte import print_text
from modules.position import action_pos
from modules.constantes import BLANC, ROUGE

def boite_de_dialogue(ecran, perso, boite, font_jeu, message, dico_controles, verifier, font_hud, meteo, hud):

    pos_boite = boite.get_rect()
    pos_boite.centerx = ecran.get_rect().centerx
    pos_boite.centery = ecran.get_rect().centery

    pos_initial = 200
    i = 0
    

    message = message.split("#")
    
    pos = 2
    faire_action = False
    boucle = True
    quitter = False

    while boucle:
        perso.current_map.afficher(ecran)
        ecran.blit(perso.current_char, (perso.x, perso.y))
        if hud:
            perso.hud(ecran, font_hud, meteo)
        ecran.blit(boite, pos_boite)
        for i in range(0,len(message)):
            pos_y = pos_initial + 30*(i+1)
            print_text(message[i], True,(255,255,255), (0, pos_y), font_jeu, ecran , True, False)
        if verifier:
            action_pos(pos,1,"Oui", True, BLANC, ROUGE, (0,pos_y+30), font_jeu, ecran, True, False)
            action_pos(pos,2,"Non", True, BLANC, ROUGE, (0,pos_y+60), font_jeu, ecran, True, False)
        else:
            print_text("Appuyer sur la touche Action pour fermer le dialogue", True, (0,185,255), (0,pos_y+30), font_jeu, ecran, True, False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boucle = False
                quitter = True
            elif event.type == pygame.KEYUP:
                if event.key == dico_controles.get("action"):
                    if verifier:
                        if pos == 1:
                            faire_action = True
                            return quitter, faire_action
                        elif pos == 2:
                            return quitter, faire_action
                    else:
                        boucle = False
            elif event.type == pygame.KEYDOWN:
                if event.key == dico_controles.get("bas"):
                    pos+= 1
                    if pos == 3:
                        pos = 1
                elif event.key == dico_controles.get("haut"):
                    pos-= 1
                    if pos == 0:
                        pos = 2
                    elif pos < 0:
                        pos = 1                  
        
        pygame.display.flip()
    
    return quitter, faire_action