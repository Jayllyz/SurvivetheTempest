#coding:utf-8


"""

    Ce module sert à afficher et gérer le menu principal du jeu

"""

import pygame
from modules.texte import print_text
from modules.constantes import NOIR, ROUGE , BLANC , BLEU
from modules.position import action_pos
from modules.controles import modif_controles
from modules.fichier import if_exist
from modules.musique import ecrire_volume, vol_musique


def menu_principal(ecran, musique_menu, fond_menu, font_menu, font_jeu, fond_menu_option, font_option, font_titre,dico_controles):

    choix = 0 # variable qui ne sert qu'à vérifier le choix de l'utilisateur dans le menu
    try :
        volume_musique = vol_musique("data/volume.m")
        volume_musique = float(volume_musique)
    except :
        volume_musique = 0.5
    musique_menu.set_volume(volume_musique)
    musique_menu.play(-1) #joue la musique à l'infini
    pos = 0
    pygame.key.set_repeat(200, 80) # le premier nombre correspond au nombres de millisecondes avant de commencer à répéter, puis le deuxieme c'est le nombre de millisecondes entre chaque répétitions
    if if_exist("data/save.stt")== True:
        while (choix != 1) and (choix != 2) and (choix != 3): # 1 = nouvelle partie, 2 = continuer, 3 = quitter , les options seront gérés dans le menu
            ecran.blit(fond_menu, (0,0))
            print_text("Survive the tempest", True, BLEU, (0,152-76), font_titre, ecran, True, False)
            action_pos(pos, 1, "Nouvelle partie", True, NOIR, ROUGE, (0,152), font_menu, ecran, True, False)

            action_pos(pos,2,"Charger la partie", True, NOIR, ROUGE, (0,152+76), font_menu, ecran, True, False)

            action_pos(pos,3,"Options", True, NOIR, ROUGE, (0,152+76*2), font_menu, ecran, True, False)

            action_pos(pos,4,"Quitter", True, NOIR, ROUGE, (0,152+76*3), font_menu, ecran, True, False)

            print_text("Version : 1.0.0", True, NOIR, (0, 588), font_jeu, ecran, True, False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    choix = 3
                elif event.type == pygame.KEYDOWN:
                    if event.key == dico_controles.get("bas"):
                        pos+= 1
                        if pos == 5:
                            pos = 1
                    if event.key == dico_controles.get("haut"):
                        pos-= 1
                        if pos == 0 :
                            pos = 4
                        elif pos < 0:
                            pos = 1

                elif event.type == pygame.KEYUP:
                    if event.key == dico_controles.get("action"):
                        if pos == 1 :
                            choix = 1
                        elif pos == 2 :
                            choix = 2
                        elif pos == 3 :
                            choix = gerer_option(ecran, fond_menu, fond_menu_option, musique_menu , font_option , dico_controles)
                        elif pos == 4 :
                            choix = 3


            pygame.display.flip()

    else:
        while (choix != 1) and (choix != 3): # 1 = nouvelle partie, 2 = continuer, 3 = quitter , les options seront gérés dans le menu
            ecran.blit(fond_menu, (0,0))
            print_text("Survive the tempest", True, BLEU, (0,152-76), font_titre, ecran, True, False)
            action_pos(pos, 1, "Nouvelle partie", True, NOIR, ROUGE, (0,152+76), font_menu, ecran, True, False)

            action_pos(pos,2,"Options", True, NOIR, ROUGE, (0,152+76*2), font_menu, ecran, True, False)

            action_pos(pos,3,"Quitter", True, NOIR, ROUGE, (0,152+76*3), font_menu, ecran, True, False)

            print_text("Version : 1.0.0", True, NOIR, (0, 588), font_jeu, ecran, True, False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    choix = 3
                elif event.type == pygame.KEYDOWN:
                    if event.key == dico_controles.get("bas"):
                        pos+= 1
                        if pos == 4:
                            pos = 1
                    elif event.key == dico_controles.get("haut"):
                        pos-= 1
                        if pos == 0 :
                            pos = 3
                        elif pos < 0:
                            pos = 1

                elif event.type == pygame.KEYUP:
                    if event.key == dico_controles.get("action"):
                        if pos == 1 :
                            choix = 1
                        elif pos == 2 :
                            choix = gerer_option(ecran, fond_menu, fond_menu_option, musique_menu , font_option , dico_controles)
                        elif pos == 3 :
                            choix = 3

            pygame.display.flip()

    musique_menu.stop()
    return choix, dico_controles


def gerer_option(ecran, fond_menu, fond_menu_option, musique_menu , font_option , dico_controles):

    pos_option = fond_menu_option.get_rect()
    pos_option.centerx = ecran.get_rect().centerx
    pos_option.centery = ecran.get_rect().centery

    pos = 0
    en_action = False
    choix = 0
    quitter_menu_option = False
    secu = 0
    while not quitter_menu_option:
        volume_musique = musique_menu.get_volume()
        ecran.blit(fond_menu, (0,0))
        ecran.blit(fond_menu_option, pos_option)
        print_text("Options", True, BLANC, (0,165), font_option, ecran, True, False)

        action_pos(pos,1,"Volume de la musique : {}%".format(int(volume_musique*100)), True, BLANC, ROUGE, (0, 200), font_option, ecran, True, False)

        action_pos(pos,2,"Aller à gauche/Menu options : {}".format(dico_controles["gauche"]), True, BLANC, ROUGE,(216,230),font_option,ecran,True,False)

        action_pos(pos,3,"Aller à droite/Menu options : {}".format(dico_controles.get("droite")), True, BLANC, ROUGE,(216,260),font_option,ecran,True,False)

        action_pos(pos,4,"Aller en bas/Menus : {}".format(dico_controles.get("bas")), True, BLANC, ROUGE,(216,290),font_option,ecran,True,False)

        action_pos(pos,5,"Aller en haut/Menus : {}".format(dico_controles.get("haut")), True, BLANC,ROUGE,(216,320),font_option,ecran,True,False)

        action_pos(pos,6,"Faire une action/Menus : {}".format(dico_controles.get("action")), True, BLANC , ROUGE,(216,350),font_option,ecran,True,False)

        action_pos(pos,7,"Ouvrir interface/Quitter options : {}".format(dico_controles.get("retour")), True,BLANC,ROUGE,(216,380),font_option,ecran,True,False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitter_menu_option = True
                choix = 3
            elif event.type == pygame.KEYDOWN:
                if not en_action:
                    if event.key == dico_controles.get("retour"):
                        quitter_menu_option = True
                if event.key == dico_controles.get("bas"):
                    pos+= 1
                    if pos == 8:
                        pos = 1
                elif event.key == dico_controles.get("haut"):
                    pos-= 1
                    if pos == 0:
                        pos = 7
                    elif pos < 0:
                        pos = 1

                elif event.key == dico_controles.get("droite"):
                    if pos == 1:
                        if volume_musique < 1.0:
                            volume_musique  += 0.01


                            musique_menu.set_volume(volume_musique)

                elif event.key == dico_controles.get("gauche"):
                    if pos == 1:
                        if volume_musique > 0.0:
                            volume_musique -= 0.01

                            musique_menu.set_volume(volume_musique)
                if en_action == True:
                    if pos == 2:
                        for cle,valeur in dico_controles.items():
                            if  event.key == valeur:
                                secu = dico_controles.get("gauche")
                                dico_controles[cle] = secu
                        dico_controles["gauche"] = event.key
                    elif pos == 3:
                        for cle,valeur in dico_controles.items():
                            if  event.key == valeur:
                                secu = dico_controles.get("droite")
                                dico_controles[cle] = secu
                        dico_controles["droite"] = event.key
                    elif pos == 4:
                        for cle,valeur in dico_controles.items():
                            if  event.key == valeur:
                                secu = dico_controles.get("bas")
                                dico_controles[cle] = secu
                        dico_controles["bas"] = event.key
                    elif pos == 5:
                        for cle,valeur in dico_controles.items():
                            if  event.key == valeur:
                                secu = dico_controles.get("haut")
                                dico_controles[cle] = secu
                        dico_controles["haut"] = event.key
                    elif pos == 6:
                        for cle,valeur in dico_controles.items():
                            if  event.key == valeur:
                                secu = dico_controles.get("action")
                                dico_controles[cle] = secu
                        dico_controles["action"] = event.key
                    elif pos == 7:
                        for cle,valeur in dico_controles.items():
                            if  event.key == valeur:
                                secu = dico_controles.get("retour")
                                dico_controles[cle] = secu
                        dico_controles["retour"] = event.key
                    en_action = False

            elif event.type == pygame.KEYUP:

                if event.key == dico_controles.get("action") and en_action == False:
                    if pos in range(2,8):
                        en_action = True

        pygame.display.flip()
    modif_controles(dico_controles)
    volume_musique = str(volume_musique)
    ecrire_volume("data/volume.m",volume_musique)
    return choix
