#coding:utf-8

"""

 Ce module sert à faciliter l'affichage d'un texte à l'écran

"""

import pygame



def print_text(message, aliasing , couleur , position , font , ecran, centre_x, centre_y):
    try:
        texte = font.render(message, aliasing , couleur)
    except:
        print("Problème lors du rendu d'un texte")
    
    x, y = position # pour garder les positions en mémoire si jamais on ne veut centrer que en x ou que en y 

    if (centre_x == True) and (centre_y == True):
        position = texte.get_rect()
        position.centerx = ecran.get_rect().centerx 
        position.centery = ecran.get_rect().centery

    elif centre_x == True:
        position = texte.get_rect()
        position.centerx = ecran.get_rect().centerx
        position.centery = y 

    elif centre_y == True:
        position = texte.get_rect()
        position.centery = ecran.get_rect().centery
        position.centerx = x

    try:
        ecran.blit(texte, position)
    except:
        print("Problème lors de l'affichage d'un texte sur l'écran")


if __name__ == "__main__": # cette ligne sert à vérifier si le fichier avec lequel on lance le programme est celui-ci
    """

    Tout le code ci-dessous sert uniquement à tester les fonctions de ce fichier indépendamment du programme principal

    """
    pygame.init()
    test_ecran = pygame.display.set_mode((200,200))
    continuer = True
    test_font = pygame.font.SysFont("arial", 20)
    print_text("Test réussi", True, (255,255,255), (100,100), test_font, test_ecran, True, True)
    pygame.display.flip()

    while continuer:
        for test_event in pygame.event.get():
            if test_event.type == pygame.QUIT:
                continuer = False