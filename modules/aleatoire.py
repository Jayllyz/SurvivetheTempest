#coding:utf-8

"""
Module pour la fonction de génération aléatoire qui va être utilisé pour la météo et les ressources.
"""
from random import randint

def nombre_alea(borne_a,borne_b):
    try:
        random_number = randint(borne_a,borne_b)
    except:
        print("Erreur durant la génération du nombre")
    return random_number


if __name__ == "__main__":
    i = 0

    while i < 10:
        print(nombre_alea(1,10))
        i+=1

