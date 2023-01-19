from main_fctions import    *
import random as rd

dico_jeu = {
     "points_de_vie_joueur" : 50,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 0,
     "tour_ennemi" : 0,
     "score" : 0
} # L'ensemble des clé/valeurs necessaire au fonctionnement du jeu.


def jouer():
    """Fonction qui assemble le jeu et permet de appeller differents fonctions
       afin de pouvoir jouer.
    """
    while dico_jeu["points_de_vie_ennemi"]>0 and dico_jeu["points_de_vie_joueur"]>0: # Le jeu continue si il reste des points de vie au joueur ET a l'ennemi.

        if à_qui(dico_jeu): # On détérmine qui doit joueur : joueur ou ennemi.
            choix_joueur(dico_jeu)  # Si c'est le tour du joueur alors on lui propose les actions qu'il peut effectuer.
        else:          
            attaque_ennemi(dico_jeu) # Si c'est le tour de l'ennemi alors il attaque le joueur
               
    win_loose(dico_jeu) # On vérifie si les conditions de victoire ou de défaite ont était remplis.
    fin_de_partie(dico_jeu) # Donne le score détaille de la partie qui viens d'étre faite.
    
jouer()