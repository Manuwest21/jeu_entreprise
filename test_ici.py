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
        choix_nbre=input("tu fais la partie solo ou en duo? ['solo', 'duo']:   ") #va répéter question [solo ou duo] si pas 1 des 2 items inscrit
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
        if dico_jeu["tour_joueur_1"]==dico_jeu["tour_ennemi"]:  ##va se baser sur la comparaison des tours joués de chacun pour désigner à qui est le tour
            tour=True
        elif dico_jeu["tour_joueur_1"]<dico_jeu["tour_ennemi"]:
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
                 choix=input("joueur 1, tu veux attaquer ou boire une potion? [attaquer/boire]:     ")
                 
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
                 choix=input("joueur 2, tu veux attaquer ou boire une potion? [attaquer/boire]:     ")
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
        print(f"vous avez infligé {degats_subis_ennemi} dégâts à l'ennemi") 
        print(f'                                          points de vie de ennemi >>> {dico_jeu["points_de_vie_ennemi"]} ')
    
    elif tour=="joueur_2":
        
        dico_jeu["tour_joueur_2"]+=1                                                      #actualise nombre de tour joué pour alternance de jeu
        degats_subis_ennemi = rd.randint(5,10)                                            #génération d'un nombre aléatoire pour notre attaque
        dico_jeu["points_de_vie_ennemi"]-= degats_subis_ennemi                            #actualisation des points de l'ennemi
        print(f"vous avez infligé {degats_subis_ennemi} dégâts à l'ennemi") 
        print(f'il lui reste{dico_jeu["points_de_vie_ennemi"]} points de vie ')
    

def usage_potions(dico_jeu, tour,nbre):
    """
    args: ne prend pas d'arguments
    enlève 1 potion au nombre de potion du joueur
    génére un nombre aléatoire entre 15 et 50
    ce nombre sera ajouté aux points de vie du joueur
    affiche le nombre de points de vie gagnés
    s'il prend la potion fait passer le prochain tour au joueur
    """
                                     
  
    if nbre=="un":
    
        if tour=="joueur_1":                                                             # partie utilisée pour le mode 1 joueur
    
             dico_jeu["potions_j1"]-=1                                                   #retire 1 potion au nombre de potions restantes
             cbien_potions_1=dico_jeu["potions_j1"]                                      #assignation variable pour indiquer nombre de portions restantes
             dico_jeu["tour_joueur_1"]+=2                                                #adaptation du nombre de tour pour que le tour prochain soit passé
             pts_potion=rd.randint(15,50)                                                #génération nombre aléatoire    
             dico_jeu["points_de_vie_joueur_1"]+=pts_potion   
             vie_j1=dico_jeu["points_de_vie_joueur_1"]                                   #nombre ajouté au nombre de points de vie
             print(f"joueur 1, tu as gagné {pts_potion} de vie!   {vie_j1}     de vie et      {cbien_potions_1} potions restantes ") 
    
    elif nbre=="deux":                                                                    # partie utilisée pour le mode 2 joueurs
        
        if tour=="joueur_1":            
            dico_jeu["potions_j1"]-=1
            cbien_potions_1=dico_jeu["potions_j1"]                                        #assignation variable pour afficher nombre de potions restantes
            dico_jeu["tour_joueur_1"]+=2
            pts_potion=rd.randint(15,50)
            dico_jeu["points_de_vie_joueur_1"]+=pts_potion
            vie_j1=dico_jeu["points_de_vie_joueur_1"]                                    #assignation variable pour afficher niveau de vie actuel
            print(f"joueur 1, tu as gagné {pts_potion} de viee!   {vie_j1}     de vie et      {cbien_potions_1} potions restantes ")                         
        
        else:
            dico_jeu["potions_j2"]-=1 
            cbien_potions_2=dico_jeu["potions_j2"] 
            dico_jeu["tour_joueur_2"]+=2
            pts_potion=rd.randint(15,50)                                                #génération nombre aléatoire de points de vie de la potion
            dico_jeu["points_de_vie_joueur_2"]+=pts_potion
            vie_j2=dico_jeu["points_de_vie_joueur_2"]
            print(f"joueur 2, tu as gagné {pts_potion} de vie!    {vie_j2}     de vie et       {cbien_potions_2} potions restantes ")
    
    

        
        
def attaque_ennemi(dico_jeu,nbre):
   
    """
    args: ne prend pas d'arguments
    la fonction permet à l'ennemi d'attaquer le joueur
    il affiche un nombre aléatoire de dégas subis et le nombre de points de vie restants au joueur
    """
   
    dico_jeu["tour_ennemi"]+=1
    degats_subis_joueur = rd.randint(5,15)
    if nbre=='un':
        dico_jeu["points_de_vie_joueur_1"]-=degats_subis_joueur                          #actualise le nombre des points des joueurs selon attaque ennemi
        print(f'-                                                   -tu as subi {degats_subis_joueur} dégâts.') 
        print(f'-                                                   -joueur_1, il te reste {dico_jeu["points_de_vie_joueur_1"]} points de vie')
    elif nbre== 'deux':
        dico_jeu["points_de_vie_joueur_1"]-=degats_subis_joueur                          #actualise le nombre des points des joueurs selon attaque ennemi
        dico_jeu["points_de_vie_joueur_2"]-=degats_subis_joueur
        print(f'--                                              vous avez subi {degats_subis_joueur} dégâts.') 
        print(f'-                                                                          -niveau de vie actuel  >>> joueur 1:{dico_jeu["points_de_vie_joueur_1"]}')
        print(f'                                                                                                      joueur 2:{dico_jeu["points_de_vie_joueur_2"]}')
        

def declaration_vainqueur(dico_jeu,nbre):
    """Fonction qui verifie les conditions de victoire du Joueur et de l'Ennemi.
    args= le dico et le mode de jeu (solo ou duo)
    """
    if nbre=="un":                                                                
        if dico_jeu["points_de_vie_ennemi"] <= 0:                                      # declaration vainqueur si le monstre a perdu
            print("Tu as reussi a battre le monstre ! Bien joué !")
            print("Merci d'avoir joué !")
        elif dico_jeu["score_j1"]<=0:                                                 #déclaration du monstre vainqueur si notre niveau de vie est de 0 ou moins
            print("Le monstre vous a battu ! Il n'y a donc plus d'éspoir...")
            
    elif nbre=="deux":                                                                 #déclaration vainqueur en mode duo
        if dico_jeu["points_de_vie_ennemi"] <= 0:                                      # declaration vainqueur si le monstre a perdu
            if dico_jeu["score_j1"]<dico_jeu["score_j2"]:
                print("le_joueur_2 gagne!")
            elif dico_jeu["score_j1"]>dico_jeu["score_j1"]:
                print("le joueur_1 gagne!")
            else:                                                                    
                print("vous êtes déclaré tous les 2 vainqueurs ex-aequo!!") 
                
        elif dico_jeu["score_j1"] <= 0 and dico_jeu["score_j2"]<=0:               
            print("le monstre est le boss!")                                         #déclaration de l'ennemi vainqueur si les scores des 2 joueurs sont à 0 ou moins
            if dico_jeu["score_j1"] <= 0 and dico_jeu["score_j2"]>=0:
                print("le joueur 2 est le boss")
            elif dico_jeu["score_j1"] >= 0 and dico_jeu["score_j2"]<=0:             # le joueur qui a le plus de points de vie est déclaré vainqueur
                print("le joueur 2 est le boss")

def score_fin_partie(dico_jeu,nbre):
    """"
    va calculer et afficher le score de fin de partie
    Args:
        dico_jeu
        nbre= si mode solo ou duo
    """
    if nbre=="un":
        dico_jeu["score_j1"] = dico_jeu["points_de_vie_joueur_1"] + dico_jeu["potions_j1"]*50
        # print("Félicitations ! Vous avez remporté la partie !")
        print(f'joueur 1, tu as su garder {dico_jeu["potions_j1"]} potions >>> ça te rapporte {dico_jeu["potions_j1"]*50} points !') 
        print(f'                                                                   voici votre score >>> {dico_jeu["score_j1"]} points')
        
    elif nbre=="deux":
        dico_jeu["score_j1"] = dico_jeu["points_de_vie_joueur_1"] + dico_jeu["potions_j1"]*50
        dico_jeu["score_j2"] = dico_jeu["points_de_vie_joueur_2"] + dico_jeu["potions_j2"]*50
        if dico_jeu["points_de_vie_ennemi"] <= 0:
            # print("Félicitations ! Vous avez remporté la partie !")
            print(f'joueur 1, tu as su garder {dico_jeu["potions_j1"]} potions   >>> ça te rapporte {dico_jeu["potions_j1"]*50} points !') 
            print(f'joueur 1, tu as su garder {dico_jeu["potions_j2"]} potions   >>> ça te rapporte {dico_jeu["potions_j2"]*50} points !') 
            print(f'                                                               voici vos scores:                      >>> joueur 1: {dico_jeu["score_j1"]} points')
            print(f'                                                                                                          joueur 2: {dico_jeu["score_j2"]} points')
           
    with open("score.txt", "w") as fichier:
        fichier.write(f' Score de la partie : {dico_jeu["score_J1"]} points ! ; Score de la partie : {dico_jeu["score_J2"]} points !')


def jouer():
    mode_solo = solo()
    if mode_solo:
        while dico_jeu["points_de_vie_ennemi"]>=0 or (dico_jeu["points_de_vie_joueur_1"]>=0 and dico_jeu["points_de_vie_joueur_2"])>=0:
            nbre='seul'                                   #la boucle va permettre de continuer tant que l'ennemi ou un des joueurs a un niveau de vie supérieur à 0
            if a_qui(dico_jeu,nbre):                      #détermine à qui est le tour, par alternance
                tour="joueur_1"
                choix_joueur(dico_jeu, tour,nbre)         #le joueur choisit son action : attaquer ou boire potion// cela va appeler la fonction de l'action choisie
            else:                                 
                tour="ennemi"  
                attaque_ennemi(dico_jeu,nbre)             # le tour de l'ennemi est automatique, celui d'atatquer// actualisation des scores selon attaque
    
    else:                                                 #va introduire la partie à 2 joueurs
        while dico_jeu["points_de_vie_ennemi"]>0 and dico_jeu["points_de_vie_joueur_1"]>0 or dico_jeu["points_de_vie_joueur_2"]>0:
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

