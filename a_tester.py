import random as rd



dico_jeu = {
     "points_de_vie_joueur" : 50,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }

#FONCTIONS EVGENI

def win_lose(dico_jeu):
    """Fonction qui verifie les conditions de victoire du Joueur et de l'Ennemie.
    """
    if dico_jeu["points_de_vie_ennemi"] <= 0:
        print("Vous avez reussi a battre le monstre ! Bien joué !")
        print("Merci d'avoir joué !")
        return True
    elif dico_jeu["points_de_vie_joueur"] <= 0:
        print("Le monstre vous a battu ! Il n'y a donc plus d'éspoir...")
        return False
    else:
        print("Le combat continue ! Choisisez votre action :")
        return None
    

def fin_de_partie(dico_jeu):
        if dico_jeu["points_de_vie_ennemi"] <= 0:
            dico_jeu["score"] = dico_jeu["points_de_vie_joueur"] + dico_jeu["potions"]*50
            print("Félicitations ! Vous avez remporté la partie !")
            print(f'Votre score pour cette partie est de {dico_jeu["score"]} points')
            print(f'Dans cette partie vous avez su garder {dico_jeu["potions"]} potions pour {dico_jeu["potions"]*50} points !') 
            print(f'Vous avez su gagner avec {dico_jeu["points_de_vie_joueur"]} points de vie restant pour {dico_jeu["points_de_vie_joueur"]} points !')
            return True
        elif dico_jeu["points_de_vie_joueur"] <=0:
            dico_jeu["score"] = 0
            print("Vous avez pas su l'emporter. Courage, vous ferez mieux la prochaine fois !")
            print(f'Votre score pour cette partie est de {dico_jeu["score"]} points...')
            return False
        else :
            pass
        with open("score.txt", "w") as fichier:
            fichier.write(f' Score de la partie : {dico_jeu["score"]} points !')
            return None
     
# =======================================================================================================================================================
     
# FONCTIONS MANU    
            
def choix_joueur(dico_jeu):    #choix d'attaquer ou  utiliser potion.
    """
    args: ne prend pas d'argument
    demande au joueur s'il souhaite attaquer ou prendre la potion
    s'il ne posséde plus de potion, le choix n'est pas demandé
    """
    
    choix=0   
    if dico_jeu["potions"]<1:
        return "Tested"
        choix=="attaquer"
    elif  dico_jeu["potions"]:
        while choix not in ["boire", "attaquer"]:
            return None
            choix=input("tu veux attaquer ou boire une potion? [attaquer/boire]:     ")
    if choix =="attaquer":
        return True
        attaque_joueur(dico_jeu)
    elif choix=="boire":
        return False
        usage_potions(dico_jeu)

def usage_potions():
    """
    args: ne prend pas d'arguments
    enlève 1 potion au nombre de potion du joueur
    génére un nombre aléatoire entre 15 et 50
    ce nombre sera ajouté aux points de vie du joueur
    affiche le nombre de points de vie gagnés
    s'il prend la potion fait passer le prochain tour au joueur
    """
    dico_jeu["potions"]-=1
    #tour_joueur-=1
    pts_potion=rd.randint(15,50)
    dico_jeu["points_de_vie_joueur"]+=pts_potion
    print(f"vous avez gagné {pts_potion} de vie!")
    return True

def à_qui(dico_jeu):
    if dico_jeu["tour_joueur"]==dico_jeu["tour_ennemi"]:  
        return True
    elif dico_jeu["tour_ennemi"]<dico_jeu["tour_joueur"]:
        return False
    
# ====================================================================================================================================================


# FONCTIONS YVETTE

def attaque_joueur(dico_jeu):
    """
    args: ne prend pas d'arguments
    fonction qui permet au joueur d'attaquer l'ennemi
    il affiche un nombre aléatoire de dégas subis entre 5 et 10 et le nombre de points de vie restant à l'ennemi
    """
    # fonction attaque qui enlève les points à l'ennemi de manière aléatoire
    # if dico_jeu["points_de_vie_joueur"]>0:
    dico_jeu["tour_joueur"]+=1
    degats_subis_ennemi = rd.randint(5,10)
    dico_jeu["points_de_vie_ennemi"]-= degats_subis_ennemi
    print(f"vous avez infligé {degats_subis_ennemi} dégâts à l'ennemi") 
    print(f'il reste {dico_jeu["points_de_vie_ennemi"]} points de vie à votre ennemi')
    
    
def attaque_ennemi(dico_jeu):
   
    """
    args: ne prend pas d'arguments
    la fonction permet à l'ennemi d'attaquer le joueur
    il affiche un nombre aléatoire de dégas subis et le nombre de points de vie restants au joueur
    """
    # if dico_jeu["points_de_vie_ennemi"]>0:
    dico_jeu["tour_ennemi"]+=1
    degats_subis_joueur = rd.randint(5,15)
    dico_jeu["points_de_vie_joueur"]-=degats_subis_joueur
    print(f'-                                                   -vous avez subi {degats_subis_joueur} dégâts.') 
    print(f'-                                                   -il vous reste {dico_jeu["points_de_vie_joueur"]} points de vie')

def usage_arme(dico_jeu):
    
    """
    Cette fonction permet au joueur de choisir une arme pour infliger des dégâts à l'ennemi.Il a le choix entre 3 armes : épée, arc et épée à deux mains.
    Les dégâts infligés dépendent de l'arme choisie.
    - Si c'est l'épée, les points de l'ennemi diminue aléatoirement entre 15 et 20 poins.
    - Si c'est l'arc, l'ennemi passe son prochain tour
    - Si l'épée à deux mains, les points de l'ennemi diminue aléatoirement entre 20 et 25 poins mais le joueur passe son prochain tour
    """
    degats_subis_ennemi=0
    choix_arme=input("quelle arme veux-tu utiliser?")
    if choix_arme in dico_jeu["arme"]:
        if choix_arme == dico_jeu["arme"][0]:
            degats_subis_ennemi = rd.randint(15,20)
        elif choix_arme == dico_jeu["arme"][1]:
            dico_jeu["tour_ennemi"]+=2
            print("l'ennemi passe son tour")
        elif choix_arme == dico_jeu["arme"][2]:
            degats_subis_ennemi = rd.randint(20,25)
            dico_jeu["tour_joueur"]+=2
        dico_jeu["points_de_vie_ennemi"] -= degats_subis_ennemi
        print(f"vous avez infligé {degats_subis_ennemi} dégâts à l'ennemi")
    else:
        print("Arme non valide.")
# =======================================================================================================================================================











