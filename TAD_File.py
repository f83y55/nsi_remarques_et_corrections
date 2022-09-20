#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Définition de la classe File

class File :
    """Implémentation de la structure de données «File» en Python. """

    def __init__(self) :
        """Ce constructeur instancie un objet de la classe File. """
        self.contenu = []

    def enfiler(self, element) :
        """Empile un élément au sommet de la file. """
        self.contenu.append(element)

    def defiler(self) :
        """Extrait et retourne l'élément au sommet de la file. """
        if self.est_vide() :
            print("Impossible, la file est vide. ")
        else :
            return self.contenu.pop(0)

    def est_vide(self) :
        """La file est-elle vide ? """
        if self.contenu == [] :
            return True
        else :
            return False

    def nbre_elements(self) :
        """Donne le nombre d'éléments dans la file"""
        return len(self.contenu)