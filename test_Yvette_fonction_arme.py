import unittest
import random as rd
from Yvette_fonction_arme_a_tester import usage_arme

class TestAddWithUnittest(unittest.TestCase):

    def test_usage_arme(self):
         print("test")
         self.assertNotIn("test_item",["epee","arc","epee_deux_mains"],None)
         self.assertEqual(usage_arme(dico_jeu = {
     "points_de_vie_joueur" : 50,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0,
     "arme": ["epee","arc","epee_deux_mains"]
 }), True)