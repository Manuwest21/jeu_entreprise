
import random as rd



def attaque_joueur(dico_jeu):
    """
    args: ne prend pas d'arguments
    fonction qui permet au joueur d'attaquer l'ennemi
    il affiche un nombre aléatoire de dégas infligés, entre 5 et 10, et le nombre de points de vie restant à l'ennemi
    """
    # fonction attaque qui enlève les points à l'ennemi en fonction des résultats du rd.randint(5,10)
    dico_jeu["tour_joueur"]+=1 # Ajout un tour au joueur pour son action
    degats_subis_ennemi = rd.randint(5,10) # Donne la quantité de dégats 
    dico_jeu["points_de_vie_ennemi"]-= degats_subis_ennemi # Inflige les dégats aux points de vie de l'ennemi
    print(f"vous avez infligé {degats_subis_ennemi} dégâts à l'ennemi") # Informe le joueur de la quantité de dégats infligés
    print(f'il reste {dico_jeu["points_de_vie_ennemi"]} points de vie à votre ennemi') # Informe le joueur de la quantité de points de vie qu'il reste a l'ennemi
    

def usage_potions(dico_jeu):
    """
    args: ne prend pas d'arguments
    enlève 1 potion au nombre de potion du joueur
    génére un nombre aléatoire entre 15 et 50
    ce nombre sera ajouté aux points de vie du joueur
    affiche le nombre de points de vie gagnés
    s'il prend la potion fait passer le prochain tour au joueur
    """
    
    dico_jeu["potions"]-=1 # Enleve une potion au joueur
    dico_jeu["tour_joueur"]+=2 # Fait passer son prochain tour au joueur
    pts_potion=rd.randint(15,50) # Donne la quantité de points de vie réstauré
    dico_jeu["points_de_vie_joueur"]+=pts_potion # Ajout les points de vie au joueur
    print(f"vous avez gagné {pts_potion} de vie!") # Informe le joueur du résultat de son action
    
def choix_joueur(dico_jeu):    #choix d'attaquer ou  utiliser potion.
    """
    args: ne prend pas d'argument
    demande au joueur s'il souhaite attaquer ou prendre la potion
    s'il ne posséde plus de potion, le choix n'est pas demandé
    """
    
    choix=0   
    if dico_jeu["potions"]<1: # Verifie que le joueur possede au moins une potion
        choix=="attaquer" # Si il a pas de potion il n'a que le choix d'attaquer
    elif  dico_jeu["potions"]: # Cas du joueur qui possede au moins une potion
        while choix not in ["boire", "attaquer"]: # Restreint la possibilité de Input a deux choix preci.
             choix=input("tu veux attaquer ou boire une potion? [attaquer/boire]:     ") # Input du joueur.
    if choix =="attaquer": # Le choix du joueur est d'attaquer
        attaque_joueur(dico_jeu) # appelle la fonction d'attaquer
    elif choix=="boire": # Le choix du joueur est de boire
        usage_potions(dico_jeu) # appelle la fonction qui permet d'utiliser une potion.
        
def attaque_ennemi(dico_jeu):
   
    """
    args: ne prend pas d'arguments
    la fonction permet à l'ennemi d'attaquer le joueur
    il affiche un nombre entre 5 et 15 de dégas subis et le nombre de points de vie restants au joueur
    """
   
    dico_jeu["tour_ennemi"]+=1 # Tour de l'ennemi augmente de 1 du a son action
    degats_subis_joueur = rd.randint(5,15) # Decide de la quantité de dégats
    dico_jeu["points_de_vie_joueur"]-=degats_subis_joueur # Inflige les dégats aux point de vie du joueur
    print(f'-                                                   -vous avez subi {degats_subis_joueur} dégâts.')
        # informe le joueur de la quantité de dégats subis 
    print(f'-                                                   -il vous reste {dico_jeu["points_de_vie_joueur"]} points de vie')
        # informe le joueur sur les points de vie qu'il lui reste.



def win_loose(dico_jeu):
    """Fonction qui verifie les conditions de victoire du Joueur et de l'Ennemi.
    """
    if dico_jeu["points_de_vie_ennemi"] <= 0: # Condition de victoire pour le joueur
        print("Vous avez reussi a battre le monstre ! Bien joué !") # Le joueur est informé de sa victoire.
        print("Merci d'avoir joué !")
    elif dico_jeu["points_de_vie_joueur"] <= 0: # Condition de la victoire du monstre
        print("Le monstre vous a battu ! Il n'y a donc plus d'éspoir...") # Le joueur est informé de sa défaite.

def fin_de_partie(dico_jeu):
        """Fonction qui donne le score du joueur pour la partie qu'il viens de faire et crée/ouvre un fichier
        score.txt afin de stocker le score du joueur a l'intérieur.
        En fonction du nombre des potions et des points de vie qu'il lui restent le score sera
        plus elevé.
            Une partie perdu donne un score égale a 0.

        Args:
            dico_jeu (_type_): Dict
        """
        if dico_jeu["points_de_vie_ennemi"] <= 0: # Condition de victoire du joueur
            dico_jeu["score"] = dico_jeu["points_de_vie_joueur"] + dico_jeu["potions"]*50 # Le calcul du score en fonction des points de vie et potions restantes
            print("Félicitations ! Vous avez remporté la partie !")
            print(f'Votre score pour cette partie est de {dico_jeu["score"]} points') # Affiche le score du joueur
            print(f'Dans cette partie vous avez su garder {dico_jeu["potions"]} potions pour {dico_jeu["potions"]*50} points !') 
            print(f'Vous avez su gagner avec {dico_jeu["points_de_vie_joueur"]} points de vie restant pour {dico_jeu["points_de_vie_joueur"]} points !')
            # Affiche les détails du calcul du score du joueur
        elif dico_jeu["points_de_vie_joueur"] <=0: # Condition de défaite du joueur
            dico_jeu["score"] = 0 # La défaite mets le score a 0
            print("Vous avez pas su l'emporter. Courage, vous ferez mieux la prochaine fois !")
            print(f'Votre score pour cette partie est de {dico_jeu["score"]} points...')
        else :
            pass
        with open("score.txt", "w") as fichier: # Crée/ouvre le fichier score.txt avec le droit d'écriture
            fichier.write(f' Score de la partie : {dico_jeu["score"]} points !') # Note le score du joueur dans le fichier score.txt
            

def à_qui(dico_jeu):
    """Fonction qui vérifie les tours du jeu.
       Détérmine a qui de jouer.

    Returns:
        _type_: Dict
    """
    if dico_jeu["tour_joueur"]==dico_jeu["tour_ennemi"]: # Condition ou les tours joueur et ennemi sont égaux  
        return True # Renvoi vrai : c'est au joueur de jouer
    elif dico_jeu["tour_ennemi"]<dico_jeu["tour_joueur"]: # Condition ou les tours de l'ennemi sont inferieur a ceux du joueur.
        return False # Renvoi faux : c'est a l'ennemi de jouer
        