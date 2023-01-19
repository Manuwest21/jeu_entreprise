import unittest
import random as rd
from Yvette_fonctions_a_tester import attaque_joueur, attaque_ennemi


class TestAddWithUnittest(unittest.TestCase):

    def test_attaque_joueur(self):
        print("test")
        self.assertEqual(attaque_joueur(dico_jeu = {
     "points_de_vie_joueur" : 0,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }), False)
        self.assertEqual(attaque_joueur(dico_jeu = {
     "points_de_vie_joueur" : 10,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }),True)
       self.assertEqual(attaque_joueur(dico_jeu = {
     "points_de_vie_joueur" : -1,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }),False)


    def test_attaque_joueur(self):
        print("test")
        self.assertEqual(attaque_ennemi(dico_jeu = {
     "points_de_vie_joueur" : 0,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }), False)
        self.assertEqual(attaque_joueur(dico_jeu = {
     "points_de_vie_joueur" : 50,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }),True)
       self.assertEqual(attaque_joueur(dico_jeu = {
     "points_de_vie_joueur" : -1,
     "points_de_vie_ennemi" : 50,
     "potions" : 3,
     "tour_joueur" : 1,
     "tour_ennemi" : 0,
     "score" : 0
 }),False)
