# Créé par david.antony, le 05/02/2019 en Python 3.2
#coding:utf-8

def vol_musique(nom_fichier):
    try:
        fichier = open(nom_fichier,"r")
    except IOError:
        print ("erreur durant l'ouverture du fichier de musique")
    volume_musique = fichier.read()
    fichier.close()
    return volume_musique

def ecrire_volume(nom_fichier,volume_musique):
    fichier = open(nom_fichier,"w")
    fichier.write(volume_musique)
    fichier.close



