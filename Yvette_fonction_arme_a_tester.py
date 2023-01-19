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

