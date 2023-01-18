import random as rd


 # VARIABLES
 
 dico_jeu = {
     "points_de_vie_joueur" : 50,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_jouer" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }


def attaque_joueur():
    points_de_vie_ennemi -= rd.randint(5,10)
    print("points de vie perdues")
    
def attaque_ennemi():
    pass
def usage_potions():
    if potions >= 1 (verification nombre potions):
        potions -= 1
    else:
        indication "vous n'avez plus de potions"
        revenir a choix joueur.
        
def choix_joueur():
    choix d'attaquer ou
    utiliser potion.
    
def resultat_partie():
    if pv jouer <= 0:
        joueur décalré perdant.
        partie prend fin.
    elif pv ennemi <= 0:
        joueur déclaré gagnant.
        partie prend fin.
    
def fin_de_partie():
    dico_jeu["score"] = dico_jeu["points_de_vie_joueur"] + dico_jeu["potions"]*50

        
while pv_ennemi>0 and pv_joueur>0:
    if tour_joueur>tour_ennemi:
        choix_joueur()
        if attaquer:
            attaque_joueur()
            tour_joueur+=1 
        elif potion:
            usage_potions()
    if tour_jouer<=tour_ennemi:
        attaque_ennemi()
        tour_ennemi+=1   

     AFFICHER LES POINTS DE VIE DU JOUEUR ET DE L'ENNEMI 
    













