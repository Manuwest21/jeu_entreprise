from main_fctions import *
import random as rd
from colorama import Fore, Back, Style





def jouer():
    mode_solo = solo()
    if mode_solo:
        while dico_jeu["points_de_vie_ennemi"]>0 and (dico_jeu["points_de_vie_joueur_1"])>0:
            nbre='seul'                                   #la boucle va permettre de continuer tant que l'ennemi ou un des joueurs a un niveau de vie supérieur à 0
            if a_qui(dico_jeu,nbre):                      #détermine à qui est le tour, par alternance
                tour="joueur_1"
                choix_joueur(dico_jeu, tour,nbre)         #le joueur choisit son action : attaquer ou boire potion// cela va appeler la fonction de l'action choisie
            else:                                 
                tour="ennemi"  
                attaque_ennemi(dico_jeu,nbre)             # le tour de l'ennemi est automatique, celui d'atatquer// actualisation des scores selon attaque
    
    else:                                                 #va introduire la partie à 2 joueurs
        while dico_jeu["points_de_vie_ennemi"]>0 and dico_jeu["points_de_vie_joueur_1"]>0 and dico_jeu["points_de_vie_joueur_2"]>0:
            nbre='deux'                                   #le nombre permet d'indiquer aux fonctions si on en mode de partie solo ou duo            
            if a_qui(dico_jeu,nbre):                      # vérifie si c'est au tour d'un joueur ou de l'ennemi de jouer
                if quel_joueur_joue():                    # détermine si c'est au tour du joueur 1 ou 2 de jouer
                    tour="joueur_1" 
                    choix_joueur(dico_jeu,tour,nbre)      #les joueurs choisissent entre l'attaque et la potion
                else:
                    tour="joueur_2"
                    choix_joueur(dico_jeu,tour,nbre)
            else: 
                tour="ennemi"                  
                attaque_ennemi(dico_jeu, nbre)           # le tour de l'ennemi est automatique, celui d'atatquer// actualisation des scores selon attaque
                       
    score_fin_partie(dico_jeu,nbre)                      #calcule le score de fin de partie
    declaration_vainqueur(dico_jeu,nbre)                 #déclare le vainqueur de la partie
    
    
jouer()