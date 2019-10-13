#coding:utf-8


"""

    Ce module sert à initialiser les touches et à les modifiers

"""


import pygame

def init_controles():
    controls_file = open("data/controls.ctrl","r")

    i = 0
    gauche =""
    droite =""
    bas    =""
    haut   =""
    action =""
    retour =""

    while i < 6:
        if i == 0:
            gauche = controls_file.readline()
            gauche = gauche[0:-1] # Pour retirer le dernier caractère de la chaine
            gauche = int(gauche)
        elif i == 1:
            droite = controls_file.readline()
            droite = droite[0:-1]
            droite = int(droite)
        elif i == 2:
            bas = controls_file.readline()
            bas = bas[0:-1]
            bas = int(bas)
        elif i == 3:
            haut = controls_file.readline()
            haut = haut[0:-1]
            haut = int(haut)
        elif i == 4:
            action = controls_file.readline()
            action = action[0:-1]
            action = int(action)
        elif i == 5:
            retour = controls_file.readline()
            retour = retour[0:-1]
            retour = int(retour)

        i+=1
    controls_file.close()

    return gauche,droite,bas,haut,action,retour

def modif_controles(dico_controles):
    controls_file = open("data/controls.ctrl","w")
    controls_file.write("{}\n{}\n{}\n{}\n{}\n{}\n".format(dico_controles.get("gauche"),dico_controles.get("droite"),dico_controles.get("bas"), dico_controles.get("haut"),dico_controles.get("action"), dico_controles.get("retour")))
    controls_file.close()




def re_init():
    controls_file = open("data/controls.ctrl","w")
    controls_file.write("{}\n{}\n{}\n{}\n{}\n{}\n".format(pygame.K_LEFT,pygame.K_RIGHT,pygame.K_DOWN, pygame.K_UP,pygame.K_SPACE,pygame.K_ESCAPE))
    controls_file.close()

if __name__ == "__main__":
    re_init()