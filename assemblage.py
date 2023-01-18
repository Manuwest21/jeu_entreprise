from main_fctions import    *
import random as rd
import matplotlib.pyplot as plt

dico_jeu = {
     "points_de_vie_joueur" : 50,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 0,
     "tour_ennemi" : 0,
     "score" : 0
}





def jouer():
    while dico_jeu["points_de_vie_ennemi"]>0 and dico_jeu["points_de_vie_joueur"]>0:
        if à_qui(dico_jeu):         #va demander joueur s'il veut "potion" ou "attaquer"
            choix_joueur(dico_jeu)   #qui va appeler la fonction "attaquer" ou "bousage potion" selon choix
        else:          
            attaque_ennemi(dico_jeu)
        
        v=dico_jeu["points_de_vie_joueur"]
        y=dico_jeu["points_de_vie_ennemi"]
        x=[v, y]
        plt.pie(x, labels=['notre_niveau_vie','niveau_vie_monster'], normalize=True)  
        if dico_jeu["points_de_vie_ennemi"]>0 and dico_jeu["points_de_vie_joueur"]>0:
            plt.show()    
    win_loose(dico_jeu)
    fin_de_partie(dico_jeu)
    
jouer()