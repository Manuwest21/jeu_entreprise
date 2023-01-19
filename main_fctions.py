
import random as rd

dico_jeu = {
     "points_de_vie_joueur_1" : 50,
     "points_de_vie_joueur_2":50,
     "points_de_vie_ennemi" : 50,
     "potions_j1" : 3,
     "potions_j2":3,
     "tour_joueur_1" : 0,
     "tour_joueur_2":0,
     "tour_ennemi" : 0,
     "score_J1" : 0,
     "score_J2" :0,
     "J1/J2": "tour_joueur_1_ou_2"
}




def solo():
    choix_nbre=0
    while choix_nbre!= "solo" and choix_nbre!= "duo":
        choix_nbre=input("tu fais la partie solo ou en duo? ['solo', 'duo']:   ")
    if choix_nbre=="solo":
        return True
    elif choix_nbre=="duo":
        return False



def a_qui(dico_jeu, nbre):
    
    
    if nbre=="seul":
        if dico_jeu["tour_joueur_1"]==dico_jeu["tour_ennemi"]:  
            tour="tour_joueur_1"
        elif dico_jeu["tour_ennemi"]<dico_jeu["tour_joueur_1"]:
            tour="ennemi"
        else:
            tour="ennemi"

        
    # elif nbre=="deux":
    
    #     if dico_jeu["tour_joueur_1"]<=dico_jeu["tour_joueur_2"]and dico_jeu["tour_joueur_1"]<=dico_jeu["tour_ennemi"]:
    #         tour="tour_joueur_1"
    #     elif dico_jeu["tour_joueur_2"]<dico_jeu["tour_joueur_1"]and dico_jeu["tour_joueur_2"] <= dico_jeu["tour_ennemi"]:
    #         tour="tour_joueur_2"
    #     elif dico_jeu["tour_joueur_2"]<dico_jeu["tour_ennemi"]:
    #         tour="ennemi"
    #     else:
    #         tour="ennemi"
            
    return tour

def choix_joueur(dico_jeu, tour):    #choix d'attaquer ou  utiliser potion.
    """
    args: ne prend pas d'argument
    demande au joueur s'il souhaite attaquer ou prendre la potion
    s'il ne posséde plus de potion, le choix n'est pas demandé
    """
    if tour=="joueur_1":
        choix=0   
        if dico_jeu["potions_j1"]<1:
            choix=="attaquer"
        else:
            while choix not in ["boire", "attaquer"]:
                 choix=input("joueur 1, tu veux attaquer ou boire une potion? [attaquer/boire]:     ")
                 
        if choix =="attaquer":
            attaque_joueur(dico_jeu,tour)
        elif choix=="boire":
            usage_potions(dico_jeu,tour)
            
        
    if tour=="joueur_2":
        choix=0   
        if dico_jeu["potions_j2"]<1:
            choix=="attaquer"
        else:
            while choix not in ["boire", "attaquer"]:
                 choix=input("joueur 2, tu veux attaquer ou boire une potion? [attaquer/boire]:     ")
        if choix =="attaquer":
            attaque_joueur(dico_jeu)
        elif choix=="boire":
            usage_potions(dico_jeu,tour)



def attaque_joueur(dico_jeu,tour):
    """
    args: ne prend pas d'arguments
    fonction qui permet au joueur d'attaquer l'ennemi
    il affiche un nombre aléatoire de dégas subis entre 5 et 10 et le nombre de points de vie restant à l'ennemi
    """
    # fonction attaque qui enlève les points à l'ennemi de manière aléatoire
    # if dico_jeu["points_de_vie_joueur"]>0:
    if tour=="joueur_1":
        
        dico_jeu["tour_joueur_1"]+=1
        degats_subis_ennemi = rd.randint(5,10)
        dico_jeu["points_de_vie_ennemi"]-= degats_subis_ennemi
        print(f"vous avez infligé {degats_subis_ennemi} dégâts à l'ennemi") 
        print(f'il reste {dico_jeu["points_de_vie_ennemi"]} points de vie à votre ennemi')
    
    elif tour=="joueur_2":
        
        dico_jeu["tour_joueur_2"]+=1
        degats_subis_ennemi = rd.randint(5,10)
        dico_jeu["points_de_vie_ennemi"]-= degats_subis_ennemi
        print(f"vous avez infligé {degats_subis_ennemi} dégâts à l'ennemi") 
        print(f'il reste {dico_jeu["points_de_vie_ennemi"]} points de vie à votre ennemi')
    

def usage_potions(dico_jeu, tour):
    """
    args: ne prend pas d'arguments
    enlève 1 potion au nombre de potion du joueur
    génére un nombre aléatoire entre 15 et 50
    ce nombre sera ajouté aux points de vie du joueur
    affiche le nombre de points de vie gagnés
    s'il prend la potion fait passer le prochain tour au joueur
    """
    if tour== "joueur_1":
        dico_jeu["potions_j1"]-=1
        dico_jeu["tour_joueur_1"]+=2
        pts_potion=rd.randint(15,50)
        dico_jeu["points_de_vie_joueur_1"]+=pts_potion
        print(f"joueur 1, tu as gagné {pts_potion} de vie!")
        
    elif tour== "joueur_2":
        dico_jeu["potions_j2"]-=1
        dico_jeu["tour_joueur_2"]+=2
        pts_potion=rd.randint(15,50)
        dico_jeu["points_de_vie_joueur_2"]+=pts_potion
        print(f"joueur 2, tu as gagné{pts_potion} de vie!")
    

        
        
def attaque_ennemi(dico_jeu):
   
    """
    args: ne prend pas d'arguments
    la fonction permet à l'ennemi d'attaquer le joueur
    il affiche un nombre aléatoire de dégas subis et le nombre de points de vie restants au joueur
    """
    # if dico_jeu["points_de_vie_ennemi"]>0:
    dico_jeu["tour_ennemi"]+=1
    degats_subis_joueur = rd.randint(5,15)
    if solo:
        dico_jeu["points_de_vie_joueur_1"]-=degats_subis_joueur
        print(f'-                                                   -tu as subi {degats_subis_joueur} dégâts.') 
        print(f'-                                                   -joueur_1, il te reste {dico_jeu["points_de_vie_joueur_1"]} points de vie')
    else:
        dico_jeu["points_de_vie_joueur_1"]-=degats_subis_joueur
        dico_jeu["points_de_vie_joueur_2"]-=degats_subis_joueur
        print(f'-                                                   -vous avez subi {degats_subis_joueur} dégâts.') 
        print(f'-                                                   -joueur_1, il te reste {dico_jeu["points_de_vie_joueur_1"]} points de vie')
        print(f'-                                                   -joueur_2, il te reste {dico_jeu["points_de_vie_joueur"]} points de vie')



def declaration_vainqueur(dico_jeu):
    """Fonction qui verifie les conditions de victoire du Joueur et de l'Ennemi.
    """
    if dico_jeu["points_de_vie_ennemi"] <= 0:
        if solo:
            print("Tu as reussi a battre le monstre ! Bien joué !")
            print("Merci d'avoir joué !")
        else:
            if dico_jeu["tour_joueur_1"]<dico_jeu["tour_joueur_2"]:
                print("le_joueur_2 gagne!")
            elif dico_jeu["tour_joueur_2!"]<dico_jeu["tour_joueur_1"]:
                print("le joueur_1 gagne!")
            else:
                print("vous êtes déclaré tous les 2 vainqueurs ex-aequo!!") 
            
    elif dico_jeu["points_de_vie_joueur_1"] <= 0 and dico_jeu["points_de_vie_joueur_2"]<=0:
        print("Le monstre vous a battu ! Il n'y a donc plus d'éspoir...")

def score_fin_partie(dico_jeu):
        if dico_jeu["points_de_vie_ennemi"] <= 0:
            dico_jeu["score_j1"] = dico_jeu["points_de_vie_joueur_1"] + dico_jeu["potions_j1"]*50
            dico_jeu["score_j2"] = dico_jeu["points_de_vie_joueur_2"] + dico_jeu["potions_j2"]*50
            print("Félicitations ! Vous avez remporté la partie !")
            print(f'joueur 1, ton score pour cette partie est de {dico_jeu["score_j1"]} points')
            print(f'joueur 2, ton score pour cette partie est de {dico_jeu["score_j2"]} points')
            print(f'joueur 1, dans cette partie tu as su garder {dico_jeu["potions_j1"]} potions pour {dico_jeu["potions_j1"]*50} points !') 
            print(f'joueur 2, dans cette partie tu as su garder {dico_jeu["potions_j2"]} potions pour {dico_jeu["potions_j2"]*50} points !') 
            print(f'Vous avez su gagner avec {dico_jeu["points_de_vie_joueur"]} points de vie restant pour {dico_jeu["points_de_vie_joueur"]} points !')
        elif dico_jeu["points_de_vie_joueur_1"] <=0:
            dico_jeu["score"] = 0
            print("Vous avez pas su l'emporter. Courage, vous ferez mieux la prochaine fois !")
            print(f'Votre score pour cette partie est de {dico_jeu["score"]} points...')
        else :
            pass
        with open("score.txt", "w") as fichier:
            fichier.write(f' Score de la partie : {dico_jeu["score_j1"]} points ! ; Score de la partie : {dico_jeu["score_j2"]} points !')
    



