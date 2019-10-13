#coding:utf-8

"""
Modules pour la gestion des ressources du joueur :
- Bois(40max) , Nourriture(20) , Eau(21)  Pierre(40) , Or(10) , Fer(15) , Cuivre(20)
If Canicule (10%) -> 0 d'eau , 1 nourriture ,
If Pluie (20%) -> 4 d'eau , 0 nourriture ,
If Nuageux (50%) -> 2 d'eau , 2 nourriture ,
If Soleil (20%) -> 1 d'eau , 3 nourriture ,

"""
from modules.meteo import gen_meteo
from modules.batiments import Scierie, Mine , Atelier, Puit
from modules.aleatoire import nombre_alea

def conso(Yaath, dico_batiments):
    viande_restante = 0
    eau_restante = 0
    
    if Yaath.jour <= 5: 
        if not Yaath.jour-1 < 0:
            viande_restante = Yaath.viande - (Yaath.jour - 1)
        else:
            viande_restante = Yaath.viande
        if not Yaath.jour -2 < 0:
            eau_restante = Yaath.eau - (Yaath.jour - 2)
        else:
            eau_restante = Yaath.eau
    elif 5 < Yaath.jour <= 7:
        if not Yaath.jour-2 < 0:
            eau_restante =  Yaath.eau - (Yaath.jour -2)
        else:
            eau_restante = Yaath.eau
        viande_restante = Yaath.viande - 3
    else:
        viande_restante = Yaath.viande - 3
        eau_restante = Yaath.eau - 5

    nombre_genere = nombre_alea(1,100)
    nombre_genere2 = nombre_alea(1,100)


    if dico_batiments.get("puit").niveau ==2 and 1 <= nombre_genere <= 15:
         eau_restante +=1

    elif dico_batiments.get("puit").niveau ==3 and 1 <= nombre_genere <= 15:
        eau_restante +=1
        
    elif dico_batiments.get("puit").niveau ==4 and 1 <= nombre_genere <= 20:
        eau_restante +=1

    elif dico_batiments.get("puit").niveau ==5 and 1 <= nombre_genere <= 25:
        eau_restante +=1

    elif dico_batiments.get("puit").niveau ==6 and 1 <= nombre_genere <=30:
         eau_restante+=1

    elif dico_batiments.get("puit").niveau ==7 and 1 <= nombre_genere <=35: 
        eau_restante +=1

    elif dico_batiments.get("puit").niveau ==8 and 1 <= nombre_genere <=35:
          eau_restante +=1
          if 1 <= nombre_genere2 <=15:
                eau_restante +=1

    elif dico_batiments.get("puit").niveau ==9 and 1 <= nombre_genere <=40:
         eau_restante +=1
         if 1 <= nombre_genere2 <=30:
                eau_restante +=1


    elif dico_batiments.get("puit").niveau ==10 and 1 <= nombre_genere <=45:
        eau_restante +=1
        if 1 <= nombre_genere2 <=15:
                eau_restante +=2


    
    
    if dico_batiments.get("atelier").niveau ==2 and 1 <= nombre_genere <= 15:
         viande_restante +=1

    elif dico_batiments.get("atelier").niveau ==3 and 1 <= nombre_genere <= 15:
        viande_restante +=1
        
    elif dico_batiments.get("atelier").niveau ==4 and 1 <= nombre_genere <= 20:
        viande_restante +=1

    elif dico_batiments.get("atelier").niveau ==5 and 1 <= nombre_genere <= 25:
        viande_restante +=1


    elif dico_batiments.get("atelier").niveau ==6 and 1 <= nombre_genere <=30:
        viande_restante +=1

    elif dico_batiments.get("atelier").niveau ==7 and 1 <= nombre_genere <=35: 
        viande_restante +=1

    elif dico_batiments.get("atelier").niveau ==8 and 1 <= nombre_genere <=35:
          viande_restante +=1
          if 1 <= nombre_genere2 <=15:
                viande_restante +=1

    elif dico_batiments.get("atelier").niveau ==9 and 1 <= nombre_genere <=40:
         viande_restante +=1
         if 1 <= nombre_genere2 <=30:
                viande_restante  +=1

    elif dico_batiments.get("atelier").niveau ==10 and 1 <= nombre_genere <=45:
        viande_restante +=1
        if 1 <= nombre_genere2 <=15:
                viande_restante +=2

    
    Yaath.eau = eau_restante
    Yaath.viande = viande_restante
        
def recup_eau(meteo,Yaath,dico_batiments):
    eau_recup = 0
    if meteo=="Soleil":
        eau_recup =1
    elif meteo=="Nuageux":
        eau_recup =2
    elif meteo=="Pluie":
        eau_recup = 4
    elif meteo=="Canicule":
        eau_recup=0

    if dico_batiments.get("puit").niveau == 1:
        eau_recup += dico_batiments.get("puit").bonus_bat(15,1)
        
    elif dico_batiments.get("puit").niveau == 2:
        eau_recup +=dico_batiments.get("puit").bonus_bat(20,1) 

    elif dico_batiments.get("puit").niveau ==3:
        eau_recup += dico_batiments.get("puit").bonus_bat(30,1)

    elif dico_batiments.get("puit").niveau ==4:
        eau_recup += dico_batiments.get("puit").bonus_bat(35,1)

    elif dico_batiments.get("puit").niveau ==5:
        eau_recup += dico_batiments.get("puit").bonus_bat(40,1)
        eau_recup += dico_batiments.get("puit").bonus_bat(15,1)

    elif dico_batiments.get("puit").niveau ==6:
        eau_recup += dico_batiments.get("puit").bonus_bat(45,1)
        eau_recup += dico_batiments.get("puit").bonus_bat(20,1)

    elif dico_batiments.get("puit").niveau ==7:
        eau_recup += dico_batiments.get("puit").bonus_bat(50,1)
        eau_recup += dico_batiments.get("puit").bonus_bat(25,1)

    elif dico_batiments.get("puit").niveau ==8:
        eau_recup += dico_batiments.get("puit").bonus_bat(55,1)
        eau_recup += dico_batiments.get("puit").bonus_bat(30,1)

    elif dico_batiments.get("puit").niveau ==9:
        eau_recup += dico_batiments.get("puit").bonus_bat(55,1)
        eau_recup += dico_batiments.get("puit").bonus_bat(35,1)

    elif dico_batiments.get("puit").niveau ==10:
        eau_recup += dico_batiments.get("puit").bonus_bat(60,1)
        eau_recup += dico_batiments.get("puit").bonus_bat(35,1)
    if eau_recup + Yaath.eau > 21:
        difference = ( eau_recup + Yaath.eau) - 21
        eau_recup -= difference
    Yaath.eau += eau_recup


def recup_viande(meteo,Yaath,dico_batiments):
    viande_recup = 0
    if meteo=="Soleil":
        viande_recup=3
    elif meteo=="Nuageux":
        viande_recup=2
    elif meteo=="Canicule":
        viande_recup=1
    elif meteo=="Pluie":
        viande_recup=0

    if dico_batiments.get("atelier").niveau ==1:
        viande_recup += dico_batiments.get("atelier").bonus_bat(15,1)
        
    elif dico_batiments.get("atelier").niveau ==2:
        viande_recup +=dico_batiments.get("atelier").bonus_bat(20,1) 

    elif dico_batiments.get("atelier").niveau ==3:
        viande_recup += dico_batiments.get("atelier").bonus_bat(30,1)

    elif dico_batiments.get("atelier").niveau ==4:
        viande_recup += dico_batiments.get("atelier").bonus_bat(35,1)

    elif dico_batiments.get("atelier").niveau ==5:
        viande_recup += dico_batiments.get("atelier").bonus_bat(40,1)
        viande_recup += dico_batiments.get("atelier").bonus_bat(15,1)

    elif dico_batiments.get("atelier").niveau ==6:
        viande_recup += dico_batiments.get("atelier").bonus_bat(45,1)
        viande_recup += dico_batiments.get("atelier").bonus_bat(20,1)

    elif dico_batiments.get("atelier").niveau ==7:
        viande_recup += dico_batiments.get("atelier").bonus_bat(50,1)
        viande_recup += dico_batiments.get("atelier").bonus_bat(25,1)

    elif dico_batiments.get("atelier").niveau ==8:
        viande_recup += dico_batiments.get("atelier").bonus_bat(55,1)
        viande_recup += dico_batiments.get("atelier").bonus_bat(30,1)

    elif dico_batiments.get("atelier").niveau ==9:
        viande_recup += dico_batiments.get("atelier").bonus_bat(55,1)
        viande_recup += dico_batiments.get("atelier").bonus_bat(35,1)

    elif dico_batiments.get("atelier").niveau ==10:
        viande_recup += dico_batiments.get("atelier").bonus_bat(60,1)
        viande_recup += dico_batiments.get("atelier").bonus_bat(35,1)
    if viande_recup + Yaath.viande > 20:
        difference = ( viande_recup + Yaath.viande) - 20
        viande_recup -= difference
    Yaath.viande += viande_recup

def recup_bois(Yaath,dico_batiments):

    recup_bois = 1
    if dico_batiments.get("scierie").niveau == 1:
        recup_bois =2

    elif dico_batiments.get("scierie").niveau == 2:
        recup_bois =3

    elif dico_batiments.get("scierie").niveau == 3:
        recup_bois =4

    elif dico_batiments.get("scierie").niveau == 4:
        recup_bois = 4   #33% de +1
        recup_bois += dico_batiments.get("scierie").bonus_bat(33,1)

    elif dico_batiments.get("scierie").niveau == 5:
        recup_bois = 4   #45% de +1
        recup_bois += dico_batiments.get("scierie").bonus_bat(45,1)

    elif dico_batiments.get("scierie").niveau == 6:
        recup_bois =4    # 45 % de + 1 ET 25% de +1
        recup_bois += dico_batiments.get("scierie").bonus_bat(45,1)
        recup_bois += dico_batiments.get("scierie").bonus_bat(25,1)

    elif dico_batiments.get("scierie").niveau == 7:
        recup_bois = 5
        recup_bois += dico_batiments.get("scierie").bonus_bat(45,1)
        recup_bois += dico_batiments.get("scierie").bonus_bat(25,1)

    elif dico_batiments.get("scierie").niveau == 8:
        recup_bois = 5 # 55% de +1 ET  33% de +1
        recup_bois += dico_batiments.get("scierie").bonus_bat(55,1)
        recup_bois += dico_batiments.get("scierie").bonus_bat(33,1)

    elif dico_batiments.get("scierie").niveau == 9:
        recup_bois = 5 # 60% de +1 ET 45% de + 1
        recup_bois += dico_batiments.get("scierie").bonus_bat(60,1)
        recup_bois += dico_batiments.get("scierie").bonus_bat(45,1)


    elif dico_batiments.get("scierie").niveau == 10:
        recup_bois = 6 # 75% de +1 et 55% de +1
        recup_bois += dico_batiments.get("scierie").bonus_bat(75,1)
        recup_bois += dico_batiments.get("scierie").bonus_bat(55,1)


    if recup_bois + Yaath.bois > 40:
        difference = ( recup_bois + Yaath.bois) - 40
        recup_bois -= difference
    Yaath.bois += recup_bois


def recup_mineraux(Yaath,dico_batiments):
    recup_gold = 0
    recup_pierre = 0
    recup_cuivre = 0
    recup_fer = 0

    nombre_genere = 0
    nombre_chance = 0

    if dico_batiments.get("mine").niveau == 0:
        nombre_genere = nombre_alea(1,100)
        if 1 <= nombre_genere <= 70:
            recup_pierre +=1
        elif 70 < nombre_genere <= 90:
            recup_cuivre +=1
        elif 90 < nombre_genere <= 95:
            recup_fer += 1
        elif 95 < nombre_genere <=100:
            recup_gold +=1



    elif dico_batiments.get("mine").niveau == 1:
        recup_pierre +=1
        nombre_genere = nombre_alea(1,100)
        if 1 <= nombre_genere <= 70:
            recup_pierre +=1
        elif 70 < nombre_genere <= 90:
            recup_cuivre +=1
        elif 90 < nombre_genere <= 95:
            recup_fer += 1
        elif 95 < nombre_genere <=100:
            recup_gold +=1    

    elif dico_batiments.get("mine").niveau == 2:
        recup_pierre +=2 #pierre 65% et cuivre 25%
        nombre_genere = nombre_alea(1,100)
        if 1 <= nombre_genere <= 65:
            recup_pierre +=1
        elif 65 < nombre_genere <= 90:
            recup_cuivre +=1
        elif 90 < nombre_genere <= 95:
            recup_fer += 1
        elif 95 < nombre_genere <=100:
            recup_gold +=1        

    elif dico_batiments.get("mine").niveau == 3:
        recup_pierre +=3  #fer 10% et pierre 60%
        nombre_genere = nombre_alea(1,100)
        if 1 <= nombre_genere <= 60:
            recup_pierre +=1
        elif 60 < nombre_genere <= 85:
            recup_cuivre +=1
        elif 85 < nombre_genere <= 95:
            recup_fer += 1
        elif 95 < nombre_genere <=100:
            recup_gold +=1        


    elif dico_batiments.get("mine").niveau == 4:
        recup_pierre +=3  #33% de +1
        nombre_genere = nombre_alea(1,100)
        if 1 <= nombre_genere <= 60:
            recup_pierre +=1
        elif 60 < nombre_genere <= 85:
            recup_cuivre +=1
        elif 85 < nombre_genere <= 95:
            recup_fer += 1
        elif 95 < nombre_genere <=100:
            recup_gold +=1    

        nombre_chance = nombre_alea(1,100)
        if 1 <= nombre_chance <= 33:
            nombre_genere = nombre_alea(1,100)
            if 1 <= nombre_genere <= 60:
                recup_pierre +=1
            elif 60 < nombre_genere <= 85:
                recup_cuivre +=1
            elif 85 < nombre_genere <= 95:
                recup_fer += 1
            elif 95 < nombre_genere <=100:
                recup_gold +=1    



    elif dico_batiments.get("mine").niveau == 5:
        recup_pierre +=3 #45% de +1
        nombre_genere = nombre_alea(1,100)
        if 1 <= nombre_genere <= 60:
            recup_pierre +=1
        elif 60 < nombre_genere <= 85:
            recup_cuivre +=1
        elif 85 < nombre_genere <= 95:
            recup_fer += 1
        elif 95 < nombre_genere <=100:
            recup_gold +=1    

        nombre_chance = nombre_alea(1,100)
        if 1<= nombre_chance <= 45:
            nombre_genere = nombre_alea(1,100)
            if 1 <= nombre_genere <= 60:
                recup_pierre +=1
            elif 60 < nombre_genere <= 85:
                recup_cuivre +=1
            elif 85 < nombre_genere <= 95:
                recup_fer += 1
            elif 95 < nombre_genere <=100:
                recup_gold +=1    


    elif dico_batiments.get("mine").niveau == 6:
        recup_pierre +=3 # 45% de chance de +1, +25% de chance de +1 , fer= 15%, pierre = 55%
        nombre_genere = nombre_alea(1,100)
        if 1 <= nombre_genere <= 55:
            recup_pierre +=1
        elif 55 < nombre_genere <= 80:
            recup_cuivre +=1
        elif 80 < nombre_genere <= 95:
            recup_fer += 1
        elif 95 < nombre_genere <=100:
            recup_gold +=1     

        nombre_chance = nombre_alea(1,100)
        if 1<= nombre_chance <=45:
            nombre_genere = nombre_alea(1,100)
            if 1 <= nombre_genere <= 55:
                recup_pierre +=1
            elif 55 < nombre_genere <= 80:
                recup_cuivre +=1
            elif 80 < nombre_genere <= 95:
                recup_fer += 1
            elif 95 < nombre_genere <=100:
                recup_gold +=1  

        nombre_chance = nombre_alea(1,100)
        if 1<= nombre_chance <=25 :
            nombre_genere = nombre_alea(1,100)
            if 1 <= nombre_genere <= 55:
                recup_pierre +=1
            elif 55 < nombre_genere <= 80:
                recup_cuivre +=1
            elif 80 < nombre_genere <= 95:
                recup_fer += 1
            elif 95 < nombre_genere <=100:
                recup_gold +=1  


    elif dico_batiments.get("mine").niveau == 7: # 45% de chance de +1, +25% de chance de +1 , fer= 15%, pierre = 55%
        recup_pierre +=4
        nombre_genere = nombre_alea(1,100)
        if 1 <= nombre_genere <= 55:
            recup_pierre +=1
        elif 55 < nombre_genere <= 80:
            recup_cuivre +=1
        elif 80 < nombre_genere <= 95:
            recup_fer += 1
        elif 95 < nombre_genere <=100:
            recup_gold +=1     

        nombre_chance = nombre_alea(1,100)
        if 1<= nombre_chance <=45:
            nombre_genere = nombre_alea(1,100)
            if 1 <= nombre_genere <= 55:
                recup_pierre +=1
            elif 55 < nombre_genere <= 80:
                recup_cuivre +=1
            elif 80 < nombre_genere <= 95:
                recup_fer += 1
            elif 95 < nombre_genere <=100:
                recup_gold +=1  

        nombre_chance = nombre_alea(1,100)
        if 1<= nombre_chance <=25 :
            nombre_genere = nombre_alea(1,100)
            if 1 <= nombre_genere <= 55:
                recup_pierre +=1
            elif 55 < nombre_genere <= 80:
                recup_cuivre +=1
            elif 80 < nombre_genere <= 95:
                recup_fer += 1
            elif 95 < nombre_genere <=100:
                recup_gold +=1 


    elif dico_batiments.get("mine").niveau == 8:
        recup_pierre +=4 # 55% de chance de +1, 33% de chance de +1 ,or = 7%, pierre = 53%
        nombre_genere = nombre_alea(1,100)
        if 1 <= nombre_genere <= 53:
            recup_pierre +=1
        elif 53 < nombre_genere <= 78:
            recup_cuivre +=1
        elif 78 < nombre_genere <= 93:
            recup_fer += 1
        elif 93 < nombre_genere <=100:
            recup_gold +=1 


        nombre_chance = nombre_alea(1,100)
        if 1<= nombre_chance <= 55:
            nombre_genere = nombre_alea(1,100)
            if 1 <= nombre_genere <= 53:
                recup_pierre +=1
            elif 53 < nombre_genere <= 78:
                recup_cuivre +=1
            elif 78 < nombre_genere <= 93:
                recup_fer += 1
            elif 93 < nombre_genere <=100:
                recup_gold +=1 

        nombre_chance = nombre_alea(1,100)
        if 1<= nombre_chance <=33:
            nombre_genere = nombre_alea(1,100)
            if 1 <= nombre_genere <= 53:
                recup_pierre +=1
            elif 53 < nombre_genere <= 78:
                recup_cuivre +=1
            elif 78 < nombre_genere <= 93:
                recup_fer += 1
            elif 93 < nombre_genere <=100:
                recup_gold +=1             


    elif dico_batiments.get("mine").niveau == 9:
        recup_pierre +=4 # 60% de chance de +1, 45% de chance de +1 , cuivre = 30% , pierre  = 48%
        nombre_genere = nombre_alea(1,100)
        if 1 <= nombre_genere <= 48:
            recup_pierre +=1
        elif 48 < nombre_genere <= 78:
            recup_cuivre +=1
        elif 78 < nombre_genere <= 93:
            recup_fer += 1
        elif 93 < nombre_genere <=100:
            recup_gold +=1 



        nombre_chance = nombre_alea(1,100)
        if 1<= nombre_chance <=60:
            nombre_genere = nombre_alea(1,100)
            if 1 <= nombre_genere <= 48:
                recup_pierre +=1
            elif 48 < nombre_genere <= 78:
                recup_cuivre +=1
            elif 78 < nombre_genere <= 93:
                recup_fer += 1
            elif 93 < nombre_genere <=100:
                recup_gold +=1 


        nombre_chance = nombre_alea(1,100)
        if 1<= nombre_chance <= 45:
            nombre_genere = nombre_alea(1,100)
            if 1 <= nombre_genere <= 48:
                recup_pierre +=1
            elif 48 < nombre_genere <= 78:
                recup_cuivre +=1
            elif 78 < nombre_genere <= 93:
                recup_fer += 1
            elif 93 < nombre_genere <=100:
                recup_gold +=1 



    elif dico_batiments.get("mine").niveau == 10:
        recup_pierre +=5 # 75% de chance de +1, 55% de chance de +1, fer = 20%, pierre = 40%, or = 10%
        nombre_genere = nombre_alea(1,100)
        if 1 <= nombre_genere <= 40:
            recup_pierre +=1
        elif 40 < nombre_genere <= 70:
            recup_cuivre +=1
        elif 70 < nombre_genere <= 90:
            recup_fer += 1
        elif 90 < nombre_genere <=100:
            recup_gold +=1 




        nombre_chance = nombre_alea(1,100)
        if 1<=  nombre_chance <=75:
            nombre_genere = nombre_alea(1,100)
            if 1 <= nombre_genere <= 40:
                recup_pierre +=1
            elif 40 < nombre_genere <= 70:
                recup_cuivre +=1
            elif 70 < nombre_genere <= 90:
                recup_fer += 1
            elif 90 < nombre_genere <=100:
                recup_gold +=1 

        nombre_chance = nombre_alea(1,100)
        if 1<= nombre_chance <= 55:
            nombre_genere = nombre_alea(1,100)
            if 1 <= nombre_genere <= 40:
                recup_pierre +=1
            elif 40 < nombre_genere <= 70:
                recup_cuivre +=1
            elif 70 < nombre_genere <= 90:
                recup_fer += 1
            elif 90 < nombre_genere <=100:
                recup_gold +=1 


    if recup_pierre + Yaath.pierre > 40:
        difference = ( recup_pierre + Yaath.pierre) - 40
        recup_pierre -= difference

    if recup_cuivre + Yaath.cuivre > 20:
        difference = ( recup_cuivre + Yaath.cuivre) - 20
        recup_cuivre -= difference

    if recup_fer + Yaath.fer > 15:
        difference = ( recup_fer + Yaath.fer) - 15
        recup_fer -= difference

    if recup_gold + Yaath.gold > 10:
        difference = ( recup_gold + Yaath.gold )
        recup_gold -= difference

    Yaath.pierre += recup_pierre
    Yaath.cuivre += recup_cuivre
    Yaath.fer += recup_fer
    Yaath.gold += recup_gold
 
