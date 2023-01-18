import unittest
import random as rd

from a_tester import *

dico_jeu = {}

class TestAddWithUnittest(unittest.TestCase):
    
    # Test de la fonction win_lose
    def test_winorlose(self):
        self.assertEqual(win_lose({"points_de_vie_joueur" : 50,"points_de_vie_ennemi" : 50}),None)
        self.assertEqual(win_lose(dico_jeu={"points_de_vie_ennemi" : 0}), True)
        self.assertEqual(win_lose(dico_jeu={"points_de_vie_joueur" : 0,"points_de_vie_ennemi" : 50}), False) 
    
    def test_fin_de_partie(self):
        self.assertEqual(fin_de_partie(dico_jeu = {
     "points_de_vie_joueur" : 50,
     "points_de_vie_ennemi" : 0,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }), True )
        self.assertEqual(fin_de_partie(dico_jeu = {
     "points_de_vie_joueur" : 0,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }), False )
        

    def test_choix_joueur(self):
        self.assertEqual(choix_joueur("potion"),"quel choix la potion ou attaquer")


















