#coding:utf-8 

"""

    Dans ce fichier il y aura tout ce dont on a besoin pour lire et afficher la map

"""

import pygame
from modules.constantes import TAILLE_SPRITE
from modules.tiles import Tiles

class Map():

    def __init__(self,structure):
        self.structure = structure
    

    def afficher(self,ecran):

        num_ligne = 0
        for ligne in self.structure:
            num_case = 0
            for tile in ligne:
                x = num_case*TAILLE_SPRITE
                y = num_ligne*TAILLE_SPRITE

                ecran.blit(tile.image, (x,y))
                
                num_case+=1
            num_ligne+=1
                
