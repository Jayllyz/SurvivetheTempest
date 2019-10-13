#coding:utf-8

"""
    Pour alléger le code
"""


from modules.texte import print_text

def action_pos(position_parcours, a_verifier, message, aliasing , couleur1 , couleur2, position , font , ecran, centre_x, centre_y):
    if position_parcours == a_verifier:
        print_text(message,aliasing, couleur2,position,font,ecran,centre_x,centre_y)
    else:
        print_text(message,aliasing, couleur1,position,font,ecran,centre_x,centre_y)
