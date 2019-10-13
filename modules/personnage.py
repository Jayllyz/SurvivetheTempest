#coding:utf-8

"""

    Module ou l'on définit la classe de notre personnage

"""

import pygame
from modules.constantes import TAILLE_SPRITE, NOMBRE_TILES_X, NOMBRE_TILES_Y
from modules.texte import print_text
from modules.dialogues import boite_de_dialogue
from modules.ressources import recup_eau, recup_bois, recup_mineraux, recup_viande
from modules.couts import cout_ev , cout_abri, cout_scierie, cout_mine

class Personnage:

    def __init__(self, bois, eau, viande, pierre, cuivre, fer, gold, jour, char_south, char_north, char_east, char_west,map):
        self.bois = bois
        self.eau = eau
        self.viande = viande
        self.pierre = pierre
        self.cuivre = cuivre
        self.fer = fer
        self.gold = gold
        self.jour = jour
        self.char_south = char_south
        self.char_north = char_north
        self.char_east = char_east
        self.char_west = char_west
        self.current_char = 0
        self.tile_x = 12
        self.tile_y = 11
        self.x = self.tile_x*TAILLE_SPRITE
        self.y = self.tile_y*TAILLE_SPRITE
        self.current_map = map

    def deplacement(self, direction, dico_maps):
        if direction == "haut":
            if self.tile_y > 0:
                if self.current_map.structure[self.tile_y-1][self.tile_x].move_on:
                    if self.current_map.structure[self.tile_y-1][self.tile_x].identifiant == 20:
                        self.current_map = dico_maps.get("map2")
                        self.tile_y = 17
                        self.y = self.tile_y*TAILLE_SPRITE
                    else:
                        self.tile_y-=1
                        self.y = self.tile_y*TAILLE_SPRITE
            self.current_char = self.char_north
        if direction == "bas":
            if self.tile_y < (NOMBRE_TILES_Y-1):
                if self.current_map.structure[self.tile_y+1][self.tile_x].move_on:
                    if self.current_map.structure[self.tile_y+1][self.tile_x].identifiant == 29:
                        self.current_map = dico_maps.get("map1")
                        self.tile_y = 1
                        self.y = self.tile_y*TAILLE_SPRITE
                    else:
                        self.tile_y+=1
                        self.y = self.tile_y*TAILLE_SPRITE
            self.current_char = self.char_south

        if direction == "droite":
            if self.tile_x < (NOMBRE_TILES_X-1):
                if self.current_map.structure[self.tile_y][self.tile_x+1].move_on:
                    self.tile_x+=1
                    self.x = self.tile_x*TAILLE_SPRITE
            self.current_char = self.char_east

        if direction == "gauche":
            if self.tile_x >0:
                if self.current_map.structure[self.tile_y][self.tile_x-1].move_on:
                    self.tile_x-=1
                    self.x = self.tile_x*TAILLE_SPRITE
            self.current_char = self.char_west


    def hud(self, ecran, font_hud,meteo):
        print_text("Eau : {}/21".format(self.eau), True, (255,255,255), (1,0), font_hud, ecran, False,False)
        print_text("Viande : {}/20".format(self.viande), True, (255,255,255), (1,24), font_hud, ecran, False,False)
        print_text("Bois : {}/40".format(self.bois), True, (255,255,255), (1,48), font_hud, ecran, False,False)
        print_text("Pierre : {}/40".format(self.pierre), True, (255,255,255), (1,72), font_hud, ecran, False,False)
        print_text("Cuivre : {}/20".format(self.cuivre), True, (255,255,255), (1,96), font_hud, ecran, False,False)
        print_text("Fer : {}/15".format(self.fer), True, (255,255,255), (1,120), font_hud, ecran, False,False)
        print_text("Or : {}/10".format(self.gold), True, (255,255,255), (1,144), font_hud, ecran, False,False)
        print_text("Jour(s) : {}".format(self.jour), True, (255,255,255), (0,15), font_hud, ecran, True,False)
        print_text("Méteo : {}".format(meteo), True, (200,0,0), (550,2), font_hud, ecran, False,False)

    def tuple_return(self):
        tuple_rss = ( self.bois , self.pierre , self.cuivre , self.fer , self.gold )
        return tuple_rss

    def action(self, ecran, boite, font_jeu, dico_controles, action_faite, meteo, dico_batiments, font_hud):
        quitter = False
        faire_action = False
        passer_jour = False
        a_fonctionne = True
        win = False
        lose = False
        bois, pierre, cuivre, fer, gold = 0,0,0,0,0

        if meteo == "Tempete":
            if self.current_map.structure[self.tile_y-1][self.tile_x].identifiant == 28:
                    quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                     "La tempête est là, vous rentrez vous abriter"
                    ,dico_controles, False, font_hud, meteo, False)
                    if dico_batiments.get("abri").niveau <12:
                        lose = True
                    else:
                        win = True

                    return quitter, passer_jour, win, lose, action_faite 

        if self.current_char == self.char_north :
            if self.current_map.structure[self.tile_y-1][self.tile_x].actionnable:
                if self.current_map.structure[self.tile_y-1][self.tile_x].identifiant == 19:
                    quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                     "En l'honneur du meilleur musicien#du monde qui a merveilleusement#accompagné nos derniers instants#sur cette maudite île avec sa musique,#Thanh-long -> RIP"
                    ,dico_controles, False, font_hud, meteo, False)
                   
                if action_faite == 3:

                    if self.current_map.structure[self.tile_y-1][self.tile_x].identifiant == 28:
                        quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                        "Souhaitez vous aller dormir ? :"
                        ,dico_controles, True, font_hud, meteo, True)
                        if faire_action:
                            passer_jour = True
                            return quitter, passer_jour, win, lose, action_faite  
                    
                    elif self.current_map.structure[self.tile_y-1][self.tile_x].identifiant == 25:
                        #bois , pierre , cuivre , fer ,or
                        niveau = dico_batiments.get("puit").niveau
                        if niveau < 10:
                            bois, pierre, cuivre, fer, gold = cout_ev(niveau)
                            quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                                "Puits niveau : {}# Coût pour l'améliorer :#Bois : {} - Pierre : {} - Cuivre : {}#Fer : {} - Or : {}#Voulez vous l'améliorer ?".format(niveau, bois, pierre, cuivre, fer, gold )
                                ,dico_controles, True, font_hud, meteo, True)
                            if faire_action:
                                a_fonctionne = dico_batiments.get("puit").lvl_up(self, cout_ev(niveau))
                                if not a_fonctionne:
                                    quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                                    "Vous n'avez pas les ressources nécessaires"
                                    ,dico_controles, False,font_hud,meteo, True)
                        else : 
                            quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                            "Puits niveau : {}".format(niveau)
                            ,dico_controles, False, font_hud,meteo, True)

                    elif self.current_map.structure[self.tile_y-1][self.tile_x].identifiant == 27:
                        #bois , pierre , cuivre , fer ,or
                        niveau = dico_batiments.get("atelier").niveau
                        if niveau < 10:
                            bois, pierre, cuivre, fer, gold = cout_ev(niveau)
                            quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                                "Atelier niveau : {}# Coût pour l'améliorer :#Bois : {} - Pierre : {} - Cuivre : {}#Fer : {} - Or : {}#Voulez vous l'améliorer ?".format(niveau, bois, pierre, cuivre, fer, gold )
                                ,dico_controles, True, font_hud,meteo, True)
                            if faire_action:
                                a_fonctionne = dico_batiments.get("atelier").lvl_up(self, cout_ev(niveau))
                                if not a_fonctionne:
                                    quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                                    "Vous n'avez pas les ressources nécessaires"
                                    ,dico_controles, False,font_hud,meteo, True)
                        else : 
                            quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                            "Atelier niveau : {}".format(niveau)
                            ,dico_controles, False, font_hud,meteo, True)

                    elif self.current_map.structure[self.tile_y-1][self.tile_x].identifiant == 26:
                        #bois , pierre , cuivre , fer ,or
                        niveau = dico_batiments.get("scierie").niveau
                        if niveau < 10:
                            bois, pierre, cuivre, fer, gold = cout_scierie(niveau)
                            quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                                "Scierie niveau : {}# Coût pour l'améliorer :#Bois : {} - Pierre : {} - Cuivre : {}#Fer : {} - Or : {}#Voulez vous l'améliorer ?".format(niveau, bois, pierre, cuivre, fer, gold )
                                ,dico_controles, True, font_hud,meteo, True)
                            if faire_action:
                                a_fonctionne = dico_batiments.get("scierie").lvl_up(self, cout_scierie(niveau))
                                if not a_fonctionne:
                                    quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                                    "Vous n'avez pas les ressources nécessaires"
                                    ,dico_controles, False,font_hud,meteo, True)
                        else : 
                            quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                            "Scierie niveau : {}".format(niveau)
                            ,dico_controles, False, font_hud,meteo, True)

                    elif self.current_map.structure[self.tile_y-1][self.tile_x].identifiant == 24:
                        #bois , pierre , cuivre , fer ,or
                        niveau = dico_batiments.get("mine").niveau
                        if niveau < 10:
                            bois, pierre, cuivre, fer, gold = cout_mine(niveau)
                            quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                                "Mine niveau : {}# Coût pour l'améliorer :#Bois : {} - Pierre : {} - Cuivre : {}#Fer : {} - Or : {}#Voulez vous l'améliorer ?".format(niveau, bois, pierre, cuivre, fer, gold )
                                ,dico_controles, True, font_hud,meteo, True)
                            if faire_action:
                                a_fonctionne = dico_batiments.get("mine").lvl_up(self, cout_mine(niveau))
                                if not a_fonctionne:
                                    quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                                    "Vous n'avez pas les ressources nécessaires"
                                    ,dico_controles, False,font_hud,meteo, True)
                        else : 
                            quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                            "Mine niveau : {}".format(niveau)
                            ,dico_controles, False, font_hud,meteo, True)

                else:
                    if self.jour > 1:

                        if self.current_map.structure[self.tile_y-1][self.tile_x].identifiant == 28:
                            #bois , pierre , cuivre , fer ,or
                            niveau = dico_batiments.get("abri").niveau
                            if niveau < 12:
                                bois, pierre, cuivre, fer, gold = cout_abri(niveau)
                                quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                                    "Abri niveau : {}# Coût pour l'améliorer :#Bois : {} - Pierre : {} - Cuivre : {}#Fer : {} - Or : {}#Voulez vous l'améliorer ?".format(niveau, bois, pierre, cuivre, fer, gold )
                                    ,dico_controles, True, font_hud,meteo, True)
                                if faire_action:
                                    a_fonctionne = dico_batiments.get("abri").lvl_up(self, cout_abri(niveau))
                                    if not a_fonctionne:
                                        quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                                        "Vous n'avez pas les ressources nécessaires"
                                        ,dico_controles, False,font_hud,meteo, True)          
                            else : 
                                quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                                "Abri niveau : {}".format(niveau)
                                ,dico_controles, False, font_hud,meteo, True)     
                                  

                    if self.current_map.structure[self.tile_y-1][self.tile_x].identifiant == 25:
                        if meteo != "Canicule":
                            quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                            "Voulez vous récupérer de l'eau ?#(Attention trois actions par jour !)"
                            ,dico_controles, True,font_hud,meteo, True)
                            if faire_action:
                                recup_eau(meteo, self, dico_batiments)
                                action_faite += 1

                    elif self.current_map.structure[self.tile_y-1][self.tile_x].identifiant == 27:
                        if meteo != "Pluie":
                            quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                            "Voulez vous récupérer de la viande ?#(Attention trois actions par jour !)"
                            ,dico_controles, True,font_hud,meteo, True)
                            if faire_action:
                                recup_viande(meteo, self, dico_batiments)
                                action_faite += 1 

                    elif self.current_map.structure[self.tile_y-1][self.tile_x].identifiant == 26:
                        if dico_batiments.get("abri").niveau >= 1:
                            quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                            "Voulez vous récupérer du bois ?#(Attention trois actions par jour !)"
                            ,dico_controles, True,font_hud,meteo, True)
                            if faire_action:
                                recup_bois(self, dico_batiments)
                                action_faite += 1  

                    elif self.current_map.structure[self.tile_y-1][self.tile_x].identifiant == 24:
                        if dico_batiments.get("abri").niveau >= 1:
                            quitter, faire_action = boite_de_dialogue(ecran, self, boite, font_jeu,
                            "Voulez vous récupérer des minéraux ?#(Attention trois actions par jour !)"
                            ,dico_controles, True,font_hud,meteo, True)
                            if faire_action:
                                recup_mineraux(self, dico_batiments)
                                action_faite += 1                    


        return quitter, passer_jour, win, lose, action_faite 

