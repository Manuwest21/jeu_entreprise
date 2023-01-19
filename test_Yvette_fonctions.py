import unittest
import random as rd
from Yvette_fonctions_a_tester import *


class TestAddWithUnittest(unittest.TestCase):

 # Test de la fonction attaque_joueur
    def test_attaque_joueur(self):
        print("test")
        self.assertEqual(attaque_joueur(dico_jeu = {
     "points_de_vie_joueur" : 10,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }), True)
        self.assertEqual(attaque_joueur(dico_jeu = {
     "points_de_vie_joueur" : 0,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }),False)
        self.assertEqual(attaque_joueur(dico_jeu = {
     "points_de_vie_joueur" : -1,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }),False)

# Test de la fonction attaque_ennemi

    def test_attaque_ennemi(self):
        print("test")
        self.assertEqual(attaque_ennemi(dico_jeu = {
     "points_de_vie_joueur" : 50,
     "points_de_vie_ennemi" : 2,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }), True)
        self.assertEqual(attaque_ennemi(dico_jeu = {
     "points_de_vie_joueur" : 50,
     "points_de_vie_ennemi" : 0,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }),False)
        self.assertEqual(attaque_ennemi(dico_jeu = {
     "points_de_vie_joueur" : 50,
     "points_de_vie_ennemi" : -5,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }),False)
    
# Test de la fonction usage_arme
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