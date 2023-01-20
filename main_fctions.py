
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
    choix_nbre=0
    while choix_nbre!= "solo" and choix_nbre!= "duo":
        choix_nbre=input("tu fais la partie solo ou en duo? ['solo', 'duo']:   ")
    if choix_nbre=="solo":
        return True
    elif choix_nbre=="duo":
        return False

def quel_joueur_joue():
    if dico_jeu["tour_joueur_1"]<=dico_jeu["tour_joueur_2"]and dico_jeu["tour_joueur_1"]<=dico_jeu["tour_ennemi"]:
        return True
    elif dico_jeu["tour_joueur_2"]<dico_jeu["tour_joueur_1"]and dico_jeu["tour_joueur_2"] <= dico_jeu["tour_ennemi"]:
        return False
    
    
def a_qui(dico_jeu, nbre):
    
    
    if nbre=="seul":
        if dico_jeu["tour_joueur_1"]==dico_jeu["tour_ennemi"]:  
            tour=True
        elif dico_jeu["tour_joueur_1"]<dico_jeu["tour_ennemi"]:
            tour=False
        

        
    elif nbre=="deux":
    
        if dico_jeu["tour_joueur_1"]<=dico_jeu["tour_joueur_2"]and dico_jeu["tour_joueur_1"]<=dico_jeu["tour_ennemi"]:
            tour=True
        elif dico_jeu["tour_joueur_2"]<dico_jeu["tour_joueur_1"]and dico_jeu["tour_joueur_2"] <= dico_jeu["tour_ennemi"]:
            tour=True
        elif dico_jeu["tour_ennemi"]<dico_jeu["tour_joueur_2"]and dico_jeu["tour_ennemi"]<dico_jeu["tour_joueur_2"]:
            tour=False
        
       
            
    return tour

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
            while choix not in ["boire", "attaquer"]:
                 choix=input("joueur 1, tu veux attaquer ou boire une potion? [attaquer/boire]:     ")
                 
        if choix =="attaquer":
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
    # fonction attaque qui enlève les points à l'ennemi de manière aléatoire
    # if dico_jeu["points_de_vie_joueur"]>0:
    if tour=="joueur_1":
        
        dico_jeu["tour_joueur_1"]+=1
        degats_subis_ennemi = rd.randint(5,10)
        dico_jeu["points_de_vie_ennemi"]-= degats_subis_ennemi
        print(f"vous avez infligé {degats_subis_ennemi} dégâts à l'ennemi") 
        print(f'                                          points de vie de ennemi >>> {dico_jeu["points_de_vie_ennemi"]} ')
    
    elif tour=="joueur_2":
        
        dico_jeu["tour_joueur_2"]+=1
        degats_subis_ennemi = rd.randint(5,10)
        dico_jeu["points_de_vie_ennemi"]-= degats_subis_ennemi
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
                                     #assignation de variables pour afficher score temporaire
    # vie_j2=dico_jeu["points_de_vie_joueur_2"]
    #                                     #assignation variable pour afficher nombre de potions restantes
    # cbien_potions_2=dico_jeu["potions_j2"]
    # nbre="deux"
    if nbre=="seul":
    
        if tour=="joueur_1":                                                                     # partie utilisée pour le mode 1 joueur
    
             dico_jeu["potions_j1"]-=1
             cbien_potions_1=dico_jeu["potions_j1"]                                  #retire 1 potion au nombre de potions restantes
             dico_jeu["tour_joueur_1"]+=2                                           #adaptation du nombre de tour pour que le tour prochain soit passé
             pts_potion=rd.randint(15,50)                                           #génération nombre aléatoire
             
             vie_j1=dico_jeu["points_de_vie_joueur_1"]+pts_potion #nombre ajouté au nombre de points de vie
             print(f"joueur 1, tu as gagné {pts_potion} de vie!   {vie_j1}     de vie et      {cbien_potions_1} potions restantes ") 
    
    elif nbre=="deux":                                                         # partie utilisée pour le mode 2 joueurs
        
        if tour=="joueur_1":            
            dico_jeu["potions_j1"]-=1
            cbien_potions_1=dico_jeu["potions_j1"]        
            dico_jeu["tour_joueur_1"]+=2
            pts_potion=rd.randint(15,50)
            vie_j1=dico_jeu["points_de_vie_joueur_1"]+pts_potion
            print(f"joueur 1, tu as gagné {pts_potion} de viee!   {vie_j1}     de vie et      {cbien_potions_1} potions restantes ")                         
        
        else:
            dico_jeu["potions_j2"]-=1 
            cbien_potions_2=dico_jeu["potions_j2"] 
            dico_jeu["tour_joueur_2"]+=2
            pts_potion=rd.randint(15,50)
            vie_j2=dico_jeu["points_de_vie_joueur_2"]+pts_potion
            print(f"joueur 2, tu as gagné {pts_potion} de vie!    {vie_j2}     de vie et       {cbien_potions_2} potions restantes ")
    
    

        
        
def attaque_ennemi(dico_jeu,nbre):
   
    """
    args: ne prend pas d'arguments
    la fonction permet à l'ennemi d'attaquer le joueur
    il affiche un nombre entre 5 et 15 de dégas subis et le nombre de points de vie restants au joueur
    """
    # if dico_jeu["points_de_vie_ennemi"]>0:
    dico_jeu["tour_ennemi"]+=1
    degats_subis_joueur = rd.randint(5,15)
    if nbre=='seul':
        dico_jeu["points_de_vie_joueur_1"]-=degats_subis_joueur
        print(f'-                                                   -tu as subi {degats_subis_joueur} dégâts.') 
        print(f'-                                                   -joueur_1, il te reste {dico_jeu["points_de_vie_joueur_1"]} points de vie')
    elif nbre== 'deux':
        dico_jeu["points_de_vie_joueur_1"]-=degats_subis_joueur
        dico_jeu["points_de_vie_joueur_2"]-=degats_subis_joueur
        print(f'--                                              vous avez subi {degats_subis_joueur} dégâts.') 
        print(f'-                                                                          -niveau de vie actuel  >>> joueur 1:{dico_jeu["points_de_vie_joueur_1"]}')
        print(f'                                                                                                      joueur 2:{dico_jeu["points_de_vie_joueur_2"]}')
        # print(f'-                                                                        -joueur_2, il te reste {dico_jeu["points_de_vie_joueur_2"]} points de vie')
        # print("niveau de vie actuel >>>  joueur 1: {} #########joueur 2:{}.format{dico_jeu["points_de_vie_joueur_1"]}{dico_jeu["points_de_vie_joueur_2"]}")                                                   ')


def declaration_vainqueur(dico_jeu,nbre):
    """Fonction qui verifie les conditions de victoire du Joueur et de l'Ennemi.
    """
    if nbre=="seul":
        if dico_jeu["points_de_vie_ennemi"] <= 0:                                      # declaration vainqueur si le monstre a perdu
            print("Tu as reussi a battre le monstre ! Bien joué !")
            print("Merci d'avoir joué !")
        elif dico_jeu["score_j1"]<=0:
            print("Le monstre vous a battu ! Il n'y a donc plus d'éspoir...")
            
    elif nbre=="deux":
        if dico_jeu["points_de_vie_ennemi"] <= 0:                                      # declaration vainqueur si le monstre a perdu
            if dico_jeu["score_j1"]<dico_jeu["score_j2"]:
                print("le_joueur_2 gagne!")
            elif dico_jeu["score_j1"]>dico_jeu["score_j1"]:
                print("le joueur_1 gagne!")
            else:                                                                    
                print("vous êtes déclaré tous les 2 vainqueurs ex-aequo!!") 
                
        elif dico_jeu["score_j1"] <= 0 and dico_jeu["score_j1"]<=0:
            print("le monstre est le boss!")
            if dico_jeu["score_j1"] <= 0 and dico_jeu["score_j1"]>=0:
                print("le joueur 2 est le boss")
            elif dico_jeu["score_j1"] >= 0 and dico_jeu["score_j1"]<=0:
                print("le joueur 2 est le boss")

def score_fin_partie(dico_jeu,nbre):
    if nbre=="seul":
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
            # if {dico_jeu["score_j1"]}>{dico_jeu["score_j2"]}:
            #     gagnant="joueur 1"
            # elif {dico_jeu["score_j2"]}>{dico_jeu["score_j1"]}:
            #     gagnant="joueur 2"
                 
            # print(f'Vous avez su gagner avec {dico_jeu["points_de_vie_joueur_1"]} points de vie restant pour {dico_jeu["points_de_vie_joueur"]} points !')
        # elif dico_jeu["points_de_vie_joueur_1"] <=0:
        #     dico_jeu["score"] = 0
        #     print("Vous avez pas su l'emporter. Courage, vous ferez mieux la prochaine fois !")
        #     print(f'Votre score pour cette partie est de {dico_jeu["score"]} points...')
        # else :
        #     pass
    with open("score.txt", "w") as fichier:
        fichier.write(f' Score de la partie : {dico_jeu["score_J1"]} points ! ; Score de la partie : {dico_jeu["score_J2"]} points !')
        
