# Créé par david.antony, le 16/04/2019 en Python 3.2
#coding:utf-8


def cout_scierie(niveau):

    couts_scierie = 0
    if niveau == 0:
        couts_scierie = (1,0,0,0,0) # bois , pierre , cuivre , fer ,or

    elif niveau == 1:
        couts_scierie = (2,0,0,0,0)

    elif niveau == 2:
        couts_scierie = (3,1,0,0,0)

    elif niveau == 3:
        couts_scierie = (4,2,0,0,0)

    elif niveau == 4:
        couts_scierie = (6,4,0,0,0)

    elif niveau == 5:
        couts_scierie = (10,8,3,0,0)

    elif niveau == 6:
        couts_scierie = (15,10,6,1,0)

    elif niveau == 7:
        couts_scierie = (25,15,10,4,0)

    elif niveau == 8:
        couts_scierie = (30,20,12,6,1)

    elif niveau == 9:
        couts_scierie = (40,25,12,6,3)
    return couts_scierie

def cout_mine(niveau):
    couts_mine = 0
    if niveau == 0:
        couts_mine = (0,1,0,0,0)

    elif niveau == 1:
        couts_mine = (0,2,0,0,0)

    elif niveau == 2:
        couts_mine = (1,3,0,0,0)

    elif niveau == 3:
        couts_mine = (2,4,0,0,0)

    elif niveau == 4:
        couts_mine = (4,6,0,0,0)

    elif niveau == 5:
        couts_mine = (8,10,3,0,0)

    elif niveau == 6:
        couts_mine = (10,15,6,1,0)

    elif niveau == 7:
        couts_mine = (15,25,10,4,0)

    elif niveau == 8:
        couts_mine = (20,30,12,6,1)

    elif niveau == 9:
        couts_mine = (25,40,12,6,3)
    return couts_mine

def cout_ev(niveau):
    couts_ev = 0
    if niveau == 0:
        couts_ev = (1,0,0,0,0)

    elif niveau == 1:
        couts_ev = (3,1,0,0,0)

    elif niveau == 2:
        couts_ev = (1,3,0,0,0)

    elif niveau == 3:
        couts_ev = (2,4,0,0,0)

    elif niveau == 4:
        couts_ev = (4,6,0,0,0)

    elif niveau == 5:
        couts_ev = (8,10,3,0,0)

    elif niveau == 6:
        couts_ev = (10,15,6,1,0)

    elif niveau == 7:
        couts_ev = (15,25,10,4,0)

    elif niveau == 8:
        couts_ev = (20,30,12,6,1)

    elif niveau == 9:
        couts_ev = (25,40,12,6,3)
    return couts_ev

def cout_abri(niveau):
    couts_abri = 0
    if niveau ==0:
        couts_abri = (0,0,0,0,0)
        
    elif niveau ==1:
        couts_abri = (1,1,0,0,0)
    
    elif niveau ==2:
        couts_abri = (1,2,0,0,0)
        
    elif niveau ==3:
        couts_abri = (2,4,0,0,0)        
    
    elif niveau ==4:
        couts_abri = (4,6,0,0,0) 
    
    elif niveau ==5:
        couts_abri = (8,8,1,0,0)
        
    elif niveau ==6:
        couts_abri = (10,10,3,0,0)
        
    elif niveau ==7:
        couts_abri = (12,12,5,1,0)
        
    elif niveau ==8:
        couts_abri = (15,15,8,2,0)
    
    elif niveau ==9:
        couts_abri = (20,20,10,4,1)
   
    elif niveau ==10:
        couts_abri = (25,25,10,4,2)
    
    elif niveau ==11:
        couts_abri = (25,25,11,5,10)
        
    return couts_abri