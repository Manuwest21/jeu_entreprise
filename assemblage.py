from main_fctions import    *
import random as rd
import matplotlib.pyplot as plt

dico_jeu = {
     "points_de_vie_joueur_1" : 50,
     "points_de_vie_joueur_2":50,
     "points_de_vie_ennemi" : 50,
     "potions_j1" : 3,
     "potions_j2":3,
     "tour_joueur_1" : 0,
     "tour_joueur_2":0,
     "tour_ennemi" : 0,
     "score_j1" : 0,
     "score_j2" :0,
     "J1/J2": "tour_joueur_1_ou_2"
}

tour=0



def jouer():
    mode_solo = solo()
    if mode_solo:
            while dico_jeu["points_de_vie_ennemi"]>0 and dico_jeu["points_de_vie_joueur_1"]>0 and dico_jeu["points_de_vie_joueur_2"]>0:
        
                nbre='seul'
                dico_jeu["points_de_vie_joueur_2"]=0                  #points de vie de joueur 2>> ramené à 0>> pr laisser place combat entre ennemi et joueur 1
                #dico_jeu["points_de_vie_ennemi"]=60 / pour augmenter difficulté
                
                if a_qui(dico_jeu,nbre)== "tour_joueur_1":
                    tour="joueur_1"
                    choix_joueur(dico_jeu, tour)
                elif a_qui(dico_jeu,nbre)=="tour_ennemi":          
                    tour="ennemi"
                    attaque_ennemi(dico_jeu)
            declaration_vainqueur(dico_jeu)
            score_fin_partie(dico_jeu)
        
    else:                                                         #else=     jouer partie à 2 joueurs
            while dico_jeu["points_de_vie_ennemi"]>0 and dico_jeu["points_de_vie_joueur_1"]>0 or dico_jeu["points_de_vie_joueur_2"]>0:
                nbre='deux'
                a_qui(dico_jeu,nbre)
                if a_qui(dico_jeu,nbre)== "tour_joueur_1":
                    tour="joueur_1" 
                    choix_joueur(dico_jeu,tour)
                elif a_qui(dico_jeu)== "tour_joueur_2":         #va demander joueur s'il veut "potion" ou "attaquer"   
                    tour="joueur_2"   
                    choix_joueur(dico_jeu, dico_jeu["J1/J2"])   #qui va appeler la fonction "attaquer" ou "bousage potion" selon choix
                else:          
                    attaque_ennemi(dico_jeu)
        
        
        
        
                declaration_vainqueur(dico_jeu)
                score_fin_partie(dico_jeu)
                print  (  "       niveau de vie actuel >>>  joueur 1: {} #########joueur 2:{}.format {dico_jeu["points_de_vie_joueur_1"]}{dico_jeu["points_de_vie_joueur_2"]}")
jouer()



# v=dico_jeu["points_de_vie_joueur"]
#         y=dico_jeu["points_de_vie_ennemi"]
#         x=[v, y]
#         plt.pie(x, labels=['notre_niveau_vie','niveau_vie_monster'], normalize=True,autopct = lambda x: str(round(x, 2)) + '%')  
#         if dico_jeu["points_de_vie_ennemi"]>0 and dico_jeu["points_de_vie_joueur"]>0:
#             plt.show()    

