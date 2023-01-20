from main_fctions import *
import random as rd
from colorama import Fore, Back, Style

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
     
    #  "J1/J2": "tour_joueur_1_ou_2"
}



def solo():
    """"ne prend pas d'arguments
        demande si on veut jouer en solo ou en duo
    Returns:
        _type_: booleen 
    """
    choix_nbre=0
    while choix_nbre!= "solo" and choix_nbre!= "duo":
        choix_nbre=input(Fore.WHITE + str("tu fais la partie solo ou en duo? ['solo', 'duo']:   ")) #va répéter question [solo ou duo] si pas 1 des 2 items inscrit
        print(Fore.RESET)
    if choix_nbre=="solo":
        return True
    elif choix_nbre=="duo":
        return False

def a_qui(dico_jeu, nbre):
    """
    utlisée pour jeu solo et duo: permet de savoir si c'est au joeuur ou à l'ennemi de jouer
    Args:
        dico_jeu (_type_): le dico et (via "nbre")le mode de jeu :solo ou duo 
        nbre (_type_): _description_

    Returns:
        _type_: booléen pour savoir si c'est à un joueur ou à l'ennemi de jouer
    """
    
    if nbre=="seul":
        if dico_jeu["tour_joueur_1"]<=dico_jeu["tour_ennemi"]:  ##va se baser sur la comparaison des tours joués de chacun pour désigner à qui est le tour
            tour=True
        elif dico_jeu["tour_joueur_1"]>dico_jeu["tour_ennemi"]:
            tour=False
        
        

        
    elif nbre=="deux":                                         ##va se baser sur la comparaison des tours joués de chacun pour désigner à qui est le tour
    
        if dico_jeu["tour_joueur_1"]<=dico_jeu["tour_joueur_2"]and dico_jeu["tour_joueur_1"]<=dico_jeu["tour_ennemi"]:
            tour=True
        elif dico_jeu["tour_joueur_2"]<dico_jeu["tour_joueur_1"]and dico_jeu["tour_joueur_2"] <= dico_jeu["tour_ennemi"]:
            tour=True
        elif dico_jeu["tour_ennemi"]<dico_jeu["tour_joueur_2"]and dico_jeu["tour_ennemi"]<dico_jeu["tour_joueur_2"]:
            tour=False
               
    return tour                                               #retourne un booléen qui va désigner si c'est à un joueur ou à l'ennemi de jouer



def quel_joueur_joue():
    """"
    en jeu "duo": avec alternance des tours, permet de savoir si c'est au joueur 1 ou 2 de jouer
    Returns:
        _type_: booléen
    """
    if dico_jeu["tour_joueur_1"]<=dico_jeu["tour_joueur_2"]and dico_jeu["tour_joueur_1"]<=dico_jeu["tour_ennemi"]:
        return True                                                 
    elif dico_jeu["tour_joueur_2"]<dico_jeu["tour_joueur_1"]and dico_jeu["tour_joueur_2"] <= dico_jeu["tour_ennemi"]:
        return False
    #va se baser sur la comparaison des tours joués de chacun pour désigner à qui est le tour
    

def choix_joueur(dico_jeu, tour,nbre):    #choix d'attaquer ou  utiliser potion.
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
            while choix not in ["boire", "attaquer"]:              #va demander le choix de boire ou d'attaquer / répéte la question si pas un des 2 items
                 choix=input(Fore.WHITE + str("joueur_1, tu veux attaquer ou boire une potion? [attaquer/boire]:     "))
                 print(Fore.RESET)
                 
        if choix =="attaquer":                                     #selon choix, va appeler la fonction "attaque" ou "boire potion"
            attaque_joueur(dico_jeu,tour)
        elif choix=="boire":
            usage_potions(dico_jeu,tour,nbre)
            
    
    if tour=="joueur_2":
        choix=0   
        if dico_jeu["potions_j2"]<1:
            choix=="attaquer"
        else:
            while choix not in ["boire", "attaquer"]:
                 choix=input(Fore.WHITE + str("joueur_2, tu veux attaquer ou boire une potion? [attaquer/boire]:     "))
                 print(Fore.RESET)
        if choix =="attaquer":
            attaque_joueur(dico_jeu,tour)
        elif choix=="boire":
            usage_potions(dico_jeu,tour,nbre)
    



def attaque_joueur(dico_jeu,tour):
    """
    args: ne prend pas d'arguments
    fonction qui permet au joueur d'attaquer l'ennemiduo
    
    il affiche un nombre aléatoire de dégas subis entre 5 et 10 et le nombre de points de vie restant à l'ennemi
    """
   
    if tour=="joueur_1":
        
        dico_jeu["tour_joueur_1"]+=1                                                       #actualise nombre de tour joué pour alternance de jeu
        degats_subis_ennemi = rd.randint(5,10)                                             #génération d'un nombre aléatoire pour notre attaque
        dico_jeu["points_de_vie_ennemi"]-= degats_subis_ennemi                             #actualisation des points de l'ennemi
        print(Fore.GREEN + Style.BRIGHT + f"vous avez infligé {degats_subis_ennemi} dégâts à l'ennemi") 
        print(Fore.RESET)
        print(Fore.GREEN + Style.BRIGHT + f'                                          points de vie de ennemi >>> {dico_jeu["points_de_vie_ennemi"]} ')
        print(Fore.RESET)
    
    elif tour=="joueur_2":
        
        dico_jeu["tour_joueur_2"]+=1                                                      #actualise nombre de tour joué pour alternance de jeu
        degats_subis_ennemi = rd.randint(5,10)                                            #génération d'un nombre aléatoire pour notre attaque
        dico_jeu["points_de_vie_ennemi"]-= degats_subis_ennemi                            #actualisation des points de l'ennemi
        print(Fore.GREEN + Style.NORMAL + f"vous avez infligé {degats_subis_ennemi} dégâts à l'ennemi") 
        print(Fore.RESET)
        print(Fore.GREEN + Style.NORMAL + f'                                          il lui reste {dico_jeu["points_de_vie_ennemi"]} points de vie ')
        print(Fore.RESET)
    

def usage_potions(dico_jeu, tour,nbre):
    """
    args: ne prend pas d'arguments
    enlève 1 potion au nombre de potion du joueur
    génére un nombre aléatoire entre 15 et 50
    ce nombre sera ajouté aux points de vie du joueur
    affiche le nombre de points de vie gagnés
    s'il prend la potion fait passer le prochain tour au joueur
    """
                                     
  
    if nbre=="seul":
    
        if tour=="joueur_1":                                                             # partie utilisée pour le mode 1 joueur
    
             dico_jeu["potions_j1"]-=1                                                   #retire 1 potion au nombre de potions restantes
             cbien_potions_1=dico_jeu["potions_j1"]                                      #assignation variable pour indiquer nombre de portions restantes
             dico_jeu["tour_joueur_1"]+=2                                                #adaptation du nombre de tour pour que le tour prochain soit passé
             pts_potion=rd.randint(15,50)                                                #génération nombre aléatoire    
             dico_jeu["points_de_vie_joueur_1"]+=pts_potion   
             vie_j1=dico_jeu["points_de_vie_joueur_1"]                                   #nombre ajouté au nombre de points de vie
             print(Fore.CYAN + Style.BRIGHT + f"joueur_1, tu as gagné {pts_potion} de vie!   {vie_j1}     de vie et      {cbien_potions_1} potions restantes ") 
             print(Fore.RESET)
    
    elif nbre=="deux":                                                                    # partie utilisée pour le mode 2 joueurs
        
        if tour=="joueur_1":            
            dico_jeu["potions_j1"]-=1
            cbien_potions_1=dico_jeu["potions_j1"]                                        #assignation variable pour afficher nombre de potions restantes
            dico_jeu["tour_joueur_1"]+=2
            pts_potion=rd.randint(15,50)
            dico_jeu["points_de_vie_joueur_1"]+=pts_potion
            vie_j1=dico_jeu["points_de_vie_joueur_1"]                                    #assignation variable pour afficher niveau de vie actuel
            print(Fore.CYAN + Style.BRIGHT + f"joueur_1, tu as gagné {pts_potion} de vie!   {vie_j1}     de vie et      {cbien_potions_1} potions restantes ")   
            print(Fore.RESET)                      
        
        else:
            dico_jeu["potions_j2"]-=1 
            cbien_potions_2=dico_jeu["potions_j2"] 
            dico_jeu["tour_joueur_2"]+=2
            pts_potion=rd.randint(15,50)                                                #génération nombre aléatoire de points de vie de la potion
            dico_jeu["points_de_vie_joueur_2"]+=pts_potion
            vie_j2=dico_jeu["points_de_vie_joueur_2"]
            print(Fore.CYAN + Style.NORMAL + f"joueur_2, tu as gagné {pts_potion} de vie!    {vie_j2}     de vie et       {cbien_potions_2} potions restantes ")
            print(Fore.RESET)  
    
    

        
        
def attaque_ennemi(dico_jeu,nbre):
   
    """
    args: ne prend pas d'arguments
    la fonction permet à l'ennemi d'attaquer le joueur
    il affiche un nombre aléatoire de dégas subis et le nombre de points de vie restants au joueur
    """
   
    dico_jeu["tour_ennemi"]+=1
    degats_subis_joueur = rd.randint(5,15)
    if nbre=='seul':
        dico_jeu["points_de_vie_joueur_1"]-=degats_subis_joueur                          #actualise le nombre des points des joueurs selon attaque ennemi
        print(Fore.RED + Style.DIM + f'tu as subi {degats_subis_joueur} dégâts.') 
        print(Fore.RESET)
        print(Fore.RED + Style.DIM + f'joueur_1, il te reste {dico_jeu["points_de_vie_joueur_1"]} points de vie')
        print(Fore.RESET)
    elif nbre== 'deux':
        dico_jeu["points_de_vie_joueur_1"]-=degats_subis_joueur                          #actualise le nombre des points des joueurs selon attaque ennemi
        dico_jeu["points_de_vie_joueur_2"]-=degats_subis_joueur
        print(Fore.RED + Style.NORMAL+ f'vous avez subi {degats_subis_joueur} dégâts.') 
        print(Fore.RESET)
        print(Fore.RED + Style.NORMAL + f'niveau de vie actuel:   >>> joueur_1 :{dico_jeu["points_de_vie_joueur_1"]} vies')
        print(Fore.RED + Style.NORMAL + f'                        >>> joueur_2 :{dico_jeu["points_de_vie_joueur_2"]} vies')
        print(Fore.RESET)

def declaration_vainqueur(dico_jeu,nbre):
    """Fonction qui verifie les conditions de victoire du Joueur et de l'Ennemi.
    args= le dico et le mode de jeu (solo ou duo)
    """
    if nbre=="seul":                                                                
        if dico_jeu["points_de_vie_ennemi"] <= 0:                                      # declaration vainqueur si le monstre a perdu
            print(Fore.GREEN + Style.DIM + str("Tu as reussi a battre le monstre ! Bien joué !"))
            print(Fore.RESET)
            print(Fore.GREEN + Style.DIM + str("Merci d'avoir joué !"))
            print(Fore.RESET)
        elif dico_jeu["score_j1"]<=0:                                                 #déclaration du monstre vainqueur si notre niveau de vie est de 0 ou moins
            print(Fore.RED + Style.DIM + str("Le monstre vous a battu ! Il n'y a donc plus d'éspoir..."))
            print(Fore.RESET)
            
    elif nbre=="deux":                                                                 #déclaration vainqueur en mode duo
        if dico_jeu["points_de_vie_ennemi"] <= 0:                                      # declaration vainqueur si le monstre a perdu
            if dico_jeu["score_j1"]<dico_jeu["score_j2"]:
                print(Fore.GREEN + Style.NORMAL + str("le_joueur_2 gagne!"))
                print(Fore.RESET)
            elif dico_jeu["score_j1"]>dico_jeu["score_j1"]:
                print(Fore.GREEN + Style.NORMAL + str("le joueur_1 gagne!"))
                print(Fore.RESET)
            else:                                                                    
                print(Fore.GREEN + Style.NORMAL + str("vous êtes déclaré tous les 2 vainqueurs ex-aequo!!"))
                print(Fore.RESET)
                
        elif dico_jeu["score_j1"] <= 0 and dico_jeu["score_j2"]<=0:               
            print(Fore.RED + Style.NORMAL + str("le monstre est le boss!"))
            print(Fore.RESET)
                                                #déclaration de l'ennemi vainqueur si les scores des 2 joueurs sont à 0 ou moins
            if dico_jeu["score_j1"] <= 0 and dico_jeu["score_j2"]>=0:
                print(Fore.GREEN + Style.NORMAL + str("le joueur_2 est le boss"))
                print(Fore.RESET)
            elif dico_jeu["score_j1"] >= 0 and dico_jeu["score_j2"]<=0:             # le joueur qui a le plus de points de vie est déclaré vainqueur
                print(Fore.GREEN + Style.NORMAL + str("le joueur_2 est le boss"))
                print(Fore.RESET)

def score_fin_partie(dico_jeu,nbre):
    """"
    va calculer et afficher le score de fin de partie
    Args:
        dico_jeu
        nbre= si mode solo ou duo
    """
    if nbre=="seul":
        dico_jeu["score_j1"] = dico_jeu["points_de_vie_joueur_1"] + dico_jeu["potions_j1"]*50
        # print("Félicitations ! Vous avez remporté la partie !")
        print(Fore.CYAN + Style.BRIGHT + f'joueur 1, tu as su garder {dico_jeu["potions_j1"]} potions >>> ça te rapporte {dico_jeu["potions_j1"]*50} points !') 
        print(Fore.RESET)
        print(Fore.CYAN + Style.BRIGHT + f'                                                               voici votre score >>> {dico_jeu["score_j1"]} points')
        print(Fore.RESET)

    elif nbre=="deux":
        dico_jeu["score_j1"] = dico_jeu["points_de_vie_joueur_1"] + dico_jeu["potions_j1"]*50
        dico_jeu["score_j2"] = dico_jeu["points_de_vie_joueur_2"] + dico_jeu["potions_j2"]*50
        if dico_jeu["points_de_vie_ennemi"] <= 0:
            # print("Félicitations ! Vous avez remporté la partie !")
            print(Fore.CYAN + Style.BRIGHT + f'joueur_1, tu as su garder {dico_jeu["potions_j1"]} potions   >>> ça te rapporte {dico_jeu["potions_j1"]*50} points !') 
            print(Fore.RESET)
            print(Fore.CYAN + Style.BRIGHT + f'joueur_1, tu as su garder {dico_jeu["potions_j2"]} potions   >>> ça te rapporte {dico_jeu["potions_j2"]*50} points !') 
            print(Fore.RESET)
            print(Fore.CYAN + Style.BRIGHT + f'                                                               voici vos scores:                     >>> joueur_1: {dico_jeu["score_j1"]} points')
            print(Fore.RESET)
            print(Fore.CYAN + Style.BRIGHT + f'                                                                                                      >>> joueur_2: {dico_jeu["score_j2"]} points')
            print(Fore.RESET)

    with open("score.txt", "w") as fichier:
        fichier.write(f' Score de la partie : {dico_jeu["score_j1"]} points ! ; Score de la partie : {dico_jeu["score_j2"]} points !')