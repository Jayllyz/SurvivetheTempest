# Créé par david.antony, le 05/02/2019 en Python 3.2
#coding:utf-8
"""
Programme pour le fichier de sauvegarde

"""

def if_exist(nom_fichier):
    try:
        fichier = open(nom_fichier,"r")
    except IOError:
        return False
    fichier.close()
    return True

if __name__ == "__main__":
    print(if_exist("../data/save.stt"))