#coding:utf-8
"""
Fonction de gestion des batiments

"""
from modules.couts      import cout_scierie , cout_mine , cout_ev, cout_abri
from modules.aleatoire import nombre_alea

class Batiments:

    def __init__(self, niveau, niveau_max):
        self.niveau = niveau
        self.niveau_max = niveau_max

    def bonus_bat(self,nombre_max,bonus):
        nombre_genere = nombre_alea(1,100)
        if 1 <= nombre_genere <= nombre_max :
            return bonus
        else :
            return 0

class Scierie(Batiments):

    def __init__(self,niveau, niveau_max):
        Batiments.__init__(self,niveau, niveau_max)

    def lvl_up(self,perso,couts_scierie):
        a_fonctionne = True
        bois, pierre, cuivre, fer, gold = perso.bois, perso.pierre, perso.cuivre, perso.fer, perso.gold
        bois_compare, pierre_compare, cuivre_compare, fer_compare,gold_compare = couts_scierie
        if self.niveau < self.niveau_max and bois >= bois_compare and pierre >= pierre_compare and cuivre >= cuivre_compare  and fer >= fer_compare and gold >= gold_compare:
            self.niveau +=1
            bois -= bois_compare
            pierre -= pierre_compare
            cuivre -= cuivre_compare
            fer -= fer_compare
            gold -= gold_compare
            perso.bois, perso.pierre, perso.cuivre, perso.fer, perso.gold = bois, pierre, cuivre, fer, gold
            return a_fonctionne

        else:
            a_fonctionne = False
            return a_fonctionne
    


class Puit(Batiments):
    def __init__(self,niveau, niveau_max):
        Batiments.__init__(self,niveau, niveau_max)

    def lvl_up(self,perso,couts_ev):
        a_fonctionne = True
        bois, pierre, cuivre, fer, gold = perso.bois, perso.pierre, perso.cuivre, perso.fer, perso.gold
        bois_compare, pierre_compare, cuivre_compare, fer_compare,gold_compare = couts_ev
        if self.niveau < self.niveau_max and bois >= bois_compare and pierre >= pierre_compare and cuivre >= cuivre_compare  and fer >= fer_compare and gold >= gold_compare:
            self.niveau +=1
            bois -= bois_compare
            pierre -= pierre_compare
            cuivre -= cuivre_compare
            fer -= fer_compare
            gold -= gold_compare
            perso.bois, perso.pierre, perso.cuivre, perso.fer, perso.gold = bois, pierre, cuivre, fer, gold
            return a_fonctionne

        else:
            a_fonctionne = False
            return a_fonctionne
        

    



class Mine(Batiments):

    def __init__(self,niveau,niveau_max):
        Batiments.__init__(self,niveau,niveau_max)

    def lvl_up(self,perso,couts_mine):
        a_fonctionne = True
        bois, pierre, cuivre, fer, gold = perso.bois, perso.pierre, perso.cuivre, perso.fer, perso.gold
        bois_compare, pierre_compare, cuivre_compare, fer_compare,gold_compare = couts_mine
        if self.niveau < self.niveau_max and bois >= bois_compare and pierre >= pierre_compare and cuivre >= cuivre_compare  and fer >= fer_compare and gold >= gold_compare:
            self.niveau +=1
            bois -= bois_compare
            pierre -= pierre_compare
            cuivre -= cuivre_compare
            fer -= fer_compare
            gold -= gold_compare
            perso.bois, perso.pierre, perso.cuivre, perso.fer, perso.gold = bois, pierre, cuivre, fer, gold
            return a_fonctionne

        else:
            a_fonctionne = False
            return a_fonctionne


class Atelier(Batiments):


    def __init__(self,niveau,niveau_max):
        Batiments.__init__(self,niveau,niveau_max)

    def lvl_up(self,perso,couts_ev):
        a_fonctionne = True
        bois, pierre, cuivre, fer, gold = perso.bois, perso.pierre, perso.cuivre, perso.fer, perso.gold
        bois_compare, pierre_compare, cuivre_compare, fer_compare,gold_compare = couts_ev
        if self.niveau < self.niveau_max and bois >= bois_compare and pierre >= pierre_compare and cuivre >= cuivre_compare  and fer >= fer_compare and gold >= gold_compare:
            self.niveau +=1
            bois -= bois_compare
            pierre -= pierre_compare
            cuivre -= cuivre_compare
            fer -= fer_compare
            gold -= gold_compare
            perso.bois, perso.pierre, perso.cuivre, perso.fer, perso.gold = bois, pierre, cuivre, fer, gold
            return a_fonctionne

        else:
            a_fonctionne = False
            return a_fonctionne

class Abri(Batiments):
    
    def __init__(self,niveau,niveau_max):
        Batiments.__init__(self,niveau,niveau_max)
        
    def lvl_up(self,perso,couts_abri):
        a_fonctionne = True
        bois, pierre, cuivre, fer, gold = perso.bois, perso.pierre, perso.cuivre, perso.fer, perso.gold
        bois_compare, pierre_compare, cuivre_compare, fer_compare,gold_compare = couts_abri
        if self.niveau < self.niveau_max and bois >= bois_compare and pierre >= pierre_compare and cuivre >= cuivre_compare  and fer >= fer_compare and gold >= gold_compare:
            self.niveau +=1
            bois -= bois_compare
            pierre -= pierre_compare
            cuivre -= cuivre_compare
            fer -= fer_compare
            gold -= gold_compare
            perso.bois, perso.pierre, perso.cuivre, perso.fer, perso.gold = bois, pierre, cuivre, fer, gold
            return a_fonctionne

        else:
            a_fonctionne = False
            return a_fonctionne



if __name__ == "__main__":
    scierie = Scierie(0, 10)
    q = "o"
    while q == "o":
        scierie.lvl_up(5,5)
        print("Niveau scierie : {}".format(scierie.niveau))
        q = input("continuer ?")