#coding:utf-8

import pygame
from modules.constantes import  TAILLE_ECRAN ,TAILLE_POLICE_MENU, TAILLE_POLICE_JEU, TAILLE_POLICE_INTERFACE, TAILLE_POLICE_TITRE
from modules.menu import menu_principal
from modules.controles import init_controles, re_init
from modules.new_game import nouvelle_partie
from modules.personnage import Personnage
from modules.fichier import if_exist
from modules.tiles import Tiles
from modules.map import Map
from modules.batiments import Batiments, Atelier,Mine, Abri, Scierie, Puit
from modules.partie import deroulement_partie
from modules.sauvegarde import load

"""

    Fichier principal du programme, qui servira à exécuter celui-ci

"""

def main():

    if if_exist("data/controls.ctrl"):
        gauche,droite,bas,haut,action,retour = init_controles() #Récupère les valeurs des touches stockées dans le fichier
    else:
        re_init()
        gauche,droite,bas,haut,action,retour = init_controles()

    dict_controles = {"gauche":gauche,"droite":droite,"bas":bas,"haut":haut,"action":action,"retour":retour} #les stockes dans un dictionnaire



    try:
        pygame.init() # Initialise pygame et tout ses modules
    except:
        print("Erreur lors de l'initialisation de pygame")

    pygame.display.set_caption("Survive the tempest") # Pour le titre de l'écran

    try:
        arial_font = pygame.font.SysFont("arial", TAILLE_POLICE_JEU)
        impact_font_titre = pygame.font.SysFont("impact", TAILLE_POLICE_TITRE)
        arial_font_option = pygame.font.SysFont("arial", TAILLE_POLICE_INTERFACE)
        arial_font_menu_bold = pygame.font.SysFont("arial", TAILLE_POLICE_MENU)
        font_hud = pygame.font.SysFont("arial", TAILLE_POLICE_INTERFACE)
    except:
        print("Erreur lors du chargement de la police d'écriture")

    try:
        arial_font_menu_bold.set_bold(True) # Pour mettre en gras
        font_hud.set_bold(True)
    except:
        print("Erreur : impossible de mettre en gras la police d'écriture")

    try:
        musique_menu = pygame.mixer.Sound("sons/main.ogg") # Charge une musique
    except:
        print("Erreur lors du chargement d'une musique (module mixer)")

    try:
        ecran = pygame.display.set_mode((TAILLE_ECRAN)) # Initialise l'écran
    except:
        print("Erreur lors de l'initialisation de la surface (de l'écran)")

    try:
        logo = pygame.image.load("images/logo.png").convert_alpha() # Charge les images , le convert_alpha sert à gérer la transparence
        fond_menu = pygame.image.load("images/menu.png").convert_alpha()
        fond_menu_option = pygame.image.load("images/menu_option.png").convert_alpha()
        char_south = pygame.image.load("images/personnage/char_south.png").convert_alpha()
        char_north = pygame.image.load("images/personnage/char_north.png").convert_alpha()
        char_east = pygame.image.load("images/personnage/char_east.png").convert_alpha()
        char_west = pygame.image.load("images/personnage/char_west.png").convert_alpha()
        plage1 = pygame.image.load("images/tiles/0.png").convert_alpha()
        plage2 = pygame.image.load("images/tiles/1.png").convert_alpha()
        sable1 = pygame.image.load("images/tiles/2.png").convert_alpha()
        ocean1 = pygame.image.load("images/tiles/3.png").convert_alpha()
        ocean2 = pygame.image.load("images/tiles/4.png").convert_alpha()
        sable2 = pygame.image.load("images/tiles/5.png").convert_alpha()
        sable3 = pygame.image.load("images/tiles/6.png").convert_alpha()
        debris1 = pygame.image.load("images/tiles/7.png").convert_alpha()
        debris2 = pygame.image.load("images/tiles/8.png").convert_alpha()
        debris3 = pygame.image.load("images/tiles/9.png").convert_alpha()
        rocher1 = pygame.image.load("images/tiles/10.png").convert_alpha()
        herbe1 = pygame.image.load("images/tiles/11.png").convert_alpha()
        herbe2 = pygame.image.load("images/tiles/12.png").convert_alpha()
        fleur1 = pygame.image.load("images/tiles/13.png").convert_alpha()
        fleur2 = pygame.image.load("images/tiles/14.png").convert_alpha()
        fleur3 = pygame.image.load("images/tiles/15.png").convert_alpha()
        fleur4 = pygame.image.load("images/tiles/16.png").convert_alpha()
        herbe3 = pygame.image.load("images/tiles/17.png").convert_alpha()
        rocher2 = pygame.image.load("images/tiles/18.png").convert_alpha()
        sepulture = pygame.image.load("images/tiles/19.png").convert_alpha()
        herbe4 = pygame.image.load("images/tiles/20.png").convert_alpha()
        arbre1 = pygame.image.load("images/tiles/21.png").convert_alpha()
        arbre2 = pygame.image.load("images/tiles/22.png").convert_alpha()
        pierre1 = pygame.image.load("images/tiles/23.png").convert_alpha()
        mine = pygame.image.load("images/tiles/24.png").convert_alpha()
        puits = pygame.image.load("images/tiles/25.png").convert_alpha()
        scierie = pygame.image.load("images/tiles/26.png").convert_alpha()
        atelier = pygame.image.load("images/tiles/27.png").convert_alpha()
        abri = pygame.image.load("images/tiles/28.png").convert_alpha()
        herbe5 = pygame.image.load("images/tiles/29.png").convert_alpha()

        Yaath = Personnage(5,5,5,5,0,0,1,1, char_south, char_north, char_east, char_west, 0)
    except:
        print("Erreur lors du chargement d'une image")
        return 0

    pygame.display.set_icon(logo) # Pour l'icone de l'écran


    Plage1 = Tiles(0,plage1,False,False)
    Plage2 = Tiles(1,plage2,False,False)
    Sable1 = Tiles(2,sable1,False,True)
    Ocean1 = Tiles(3,ocean1,False,False)
    Ocean2 = Tiles(4,ocean2,False,False)
    Sable2 = Tiles(5,sable2,False,True)
    Sable3 = Tiles(6,sable3,False,True)
    Debris1 = Tiles(7,debris1,False,False)
    Debris2 = Tiles(8,debris2,False,False)
    Debris3 = Tiles(9,debris3,False,False)
    Rocher1 = Tiles(10,rocher1,False,False)
    Herbe1 = Tiles(11,herbe1,False,True)
    Herbe2 = Tiles(12,herbe2,False,True)
    Fleur1 = Tiles(13,fleur1,False,True)
    Fleur2 = Tiles(14,fleur2,False,True)
    Fleur3 = Tiles(15,fleur3,False,True)
    Fleur4 = Tiles(16,fleur4,False,True)
    Herbe3 = Tiles(17,herbe3,False,True)
    Rocher2 = Tiles(18,rocher2,False,False)
    Sepulture = Tiles(19,sepulture,True,False)
    Herbe4 = Tiles(20,herbe4, False, True)
    Arbre1 = Tiles(21, arbre1, False, False)
    Arbre2 = Tiles(22, arbre2, False, False)
    Pierre1 = Tiles(23, pierre1, False, False)
    Mine1 = Tiles(24, mine, True, False)
    Puits = Tiles(25, puits, True, False)
    Scierie1 = Tiles(26, scierie, True, False)
    Atelier1 = Tiles(27, atelier, True, False)
    Abri1 = Tiles(28, abri, True, False)
    Herbe5 = Tiles(29, herbe5, False, True)

    #La je créer les structures des deux maps, que je vais ensuite ajouter à un objet map pour l'afficher

    structure_map1 = [
        [Rocher2,Rocher2,Herbe1,Herbe1,Herbe2,Fleur1,Herbe1,Fleur1,Herbe3,Rocher2,Herbe4,Rocher2,Herbe3,Herbe1,Herbe1,Herbe1,Herbe1,Fleur1,Herbe1,Herbe1,Herbe1,Herbe1,Rocher2,Rocher2,Rocher2],
        [Rocher2,Rocher2,Herbe1,Herbe1,Herbe2,Fleur2,Herbe2,Fleur1,Herbe3,Fleur1,Sable1,Herbe3,Herbe3,Herbe1,Herbe1,Herbe1,Herbe1,Herbe1,Herbe1,Herbe1,Herbe1,Herbe1,Fleur3,Rocher2,Rocher2],
        [Rocher2,Sepulture,Rocher2,Rocher2,Herbe2,Herbe2,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Herbe3,Herbe3,Herbe3,Fleur1,Herbe1,Herbe1,Fleur1,Herbe3,Herbe1,Herbe1,Herbe3,Fleur2,Rocher2],
        [Rocher1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable2,Sable1,Sable1,Sable1,Rocher1,Sable1,Sable1,Sable1,Herbe3,Herbe1,Fleur2,Sable3,Herbe3,Herbe3,Herbe3,Rocher2,Herbe3,Rocher1],
        [Rocher1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Herbe3,Herbe2,Herbe3,Sable1,Rocher1],
        [Rocher1,Rocher1,Sable1,Sable1,Sable3,Sable1,Rocher1,Sable1,Sable3,Sable1,Sable1,Sable1,Sable1,Sable2,Sable1,Sable1,Sable1,Sable1,Sable1,Sable3,Sable2,Sable1,Sable1,Sable1,Rocher1],
        [Rocher1,Rocher1,Rocher1,Sable1,Sable1,Sable1,Sable2,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Rocher1,Rocher1,Sable1,Rocher1],
        [Rocher1,Rocher1,Rocher1,Rocher1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Rocher1,Rocher1,Rocher1,Rocher1,Rocher1,Rocher1],
        [Rocher1,Rocher1,Rocher1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable3,Sable2,Sable1,Sable1,Sable1,Sable1,Rocher1,Rocher1,Rocher1,Rocher1],
        [Rocher1,Sable1,Sable1,Sable3,Sable2,Sable1,Sable1,Sable1,Sable1,Sable1,Rocher1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Rocher1,Sable1,Sable3,Sable1,Rocher1],
        [Rocher1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Rocher1],
        [Rocher1,Sable1,Sable1,Sable3,Sable1,Sable1,Sable1,Sable2,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable1,Sable2,Sable1,Sable1,Sable1,Sable1,Sable1,Rocher1,Rocher1],
        [Plage1,Plage2,Plage1,Plage2,Plage1,Plage2,Plage1,Plage2,Plage1,Plage2,Plage1,Plage2,Debris2,Plage2,Plage1,Plage2,Plage1,Plage2,Plage1,Plage2,Plage1,Plage2,Plage1,Plage2,Plage1],
        [Ocean1,Debris3,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1],
        [Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Debris1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1],
        [Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Debris1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1],
        [Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1,Ocean1],
        [Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2],
        [Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2,Ocean2]
    ]

    structure_map2 = [
        [Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Rocher2, Rocher2, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1],
        [Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Herbe2, Rocher2, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1],
        [Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Fleur3, Herbe2, Herbe1, Herbe2, Arbre2, Arbre2, Arbre2, Herbe2, Rocher2, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Pierre1, Mine1, Pierre1, Pierre1, Pierre1, Pierre1],
        [Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Herbe2, Scierie1, Herbe2, Herbe1, Arbre1, Arbre1, Arbre1, Herbe2, Herbe3, Rocher2, Rocher2, Rocher2, Fleur4, Fleur3, Rocher2, Herbe3, Rocher2, Rocher2, Fleur2, Rocher2],
        [Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Herbe2, Herbe2, Herbe2, Herbe2, Herbe2, Herbe2, Herbe2, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Rocher2],
        [Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Herbe2, Herbe2, Herbe2, Herbe2, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Rocher2],
        [Herbe1, Herbe1, Herbe1, Herbe1, Herbe1, Herbe1, Herbe1, Herbe1, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Fleur1, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Rocher2],
        [Herbe3, Herbe3, Herbe3, Atelier1, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Abri1, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Rocher2, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Rocher2],
        [Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Rocher2, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe1, Herbe3, Fleur1, Herbe1, Fleur2, Herbe3, Herbe3, Arbre2],
        [Arbre2, Arbre2, Arbre2, Arbre2, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe1, Puits, Herbe2, Herbe3, Arbre2, Arbre1],
        [Arbre1, Arbre1, Arbre1, Arbre1, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Arbre2, Arbre2, Arbre2, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Fleur3, Herbe2, Fleur4, Herbe3, Arbre1, Arbre2],
        [Rocher2, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Arbre1, Arbre1, Arbre1, Fleur3, Arbre2, Arbre2, Arbre2, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Arbre1],
        [Rocher2, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe2, Herbe2, Herbe2, Herbe2, Arbre1, Arbre1, Arbre1, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Rocher2, Rocher2],
        [Arbre2, Herbe3, Herbe3, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Herbe3, Herbe3, Herbe3, Herbe2, Herbe2, Herbe2, Herbe2, Herbe2, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe2, Herbe2, Herbe3, Rocher2],
        [Arbre1, Herbe1, Fleur2, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe2, Herbe2, Herbe2, Herbe2, Herbe3, Herbe3, Herbe3, Rocher2, Herbe3, Herbe2, Herbe3, Rocher2],
        [Herbe1, Herbe1, Herbe1, Herbe1, Herbe1, Herbe1, Herbe1, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe1, Herbe1, Herbe1, Herbe2, Rocher2, Rocher2],
        [Herbe1, Herbe1, Herbe1, Herbe1, Herbe1, Herbe2, Herbe1, Herbe1, Herbe1, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe3, Herbe2, Herbe2, Herbe1, Herbe1, Rocher2, Rocher2],
        [Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Herbe3, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Arbre2, Herbe3, Herbe3, Rocher2, Rocher2, Rocher2, Rocher2],
        [Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Herbe5, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Arbre1, Rocher2, Rocher2, Rocher2, Rocher2, Rocher2, Rocher2]
    ]


    atelier = Atelier(0,10)
    mine = Mine(0,10)
    scierie = Scierie(0,10)
    abri = Abri(0,12)
    puit = Puit(0,10)

    map1 = Map(structure_map1)
    map2 = Map(structure_map2)


    dico_maps = {"map1":map1, "map2":map2}
    dico_batiments = {"atelier":atelier,"mine":mine,"scierie":scierie,"abri":abri,"puit":puit}

    quitter = False
    continuer = True

    while continuer : # Boucle principal du programme
        choix, dict_controles = menu_principal(ecran, musique_menu, fond_menu, arial_font_menu_bold, arial_font , fond_menu_option , arial_font_option, impact_font_titre, dict_controles)

        if choix == 1:
            quitter = nouvelle_partie(ecran, arial_font,font_hud, dict_controles, Yaath,dico_maps, dico_batiments,fond_menu_option)
            if quitter :
                continuer = False
        elif choix == 2:
            load(Yaath, dico_maps, dico_batiments)
            quitter = deroulement_partie(ecran, arial_font,font_hud, dict_controles, Yaath,dico_maps, dico_batiments,fond_menu_option)
            if quitter :
                continuer = False
        elif choix  == 3:
            continuer = False

    pygame.quit()

if __name__ == "__main__":
    main()
