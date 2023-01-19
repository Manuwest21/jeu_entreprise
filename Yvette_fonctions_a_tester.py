dico_jeu = {
     "points_de_vie_joueur" : 50,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0,
     "arme": ["epee","arc","epee_deux_mains"]
 }

import random as rd
def attaque_joueur(dico_jeu):
    """fonction qui permet au joueur d'attaquer l'ennemi

    Returns:
        il affiche le nombre de dégas subis et le nombre de points de vie restant à l'ennemi
    """
    # fonction attaque qui enlève les points à l'ennemi de manière aléatoire
    if dico_jeu["points_de_vie_joueur"]>0:
        degats_subis_ennemi = rd.randint(5,10)
        dico_jeu["points_de_vie_ennemi"]-= degats_subis_ennemi
        print(f'vous avez infligé {degats_subis_ennemi} dégâts.') 
        print(f'il reste {dico_jeu["points_de_vie_ennemi"]} points de vie à votre ennemi')
        return True
    else:
        return False
    
def attaque_ennemi():
    """la fonction permet à l'ennemi d'attaquer le joueur
    
    Returns:
        il affiche le nombre de dégas subis et le nombre de points de vie restants au joueur
    """
    if dico_jeu["points_de_vie_ennemi"]>0:
        degats_subis_joueur = rd.randint(5,15)
        dico_jeu["points_de_vie_joueur"]-=degats_subis_joueur
        print(f'vous avez subi {degats_subis_joueur} dégâts.') 
        print(f'il vous reste {dico_jeu["points_de_vie_joueur"]} points de vie')
        dico_jeu["tour_ennemi"]-=1
        return True
    else:
        return False

def usage_arme(dico_jeu):
    """
    permet au joeur de choisir une arme entre epée, arc et epée à deux mains

    Args:prend en compte l'arme utilisée et affiche le nombre de dégpâts subis ou le joueur/ennemi passe son prochain tour
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

