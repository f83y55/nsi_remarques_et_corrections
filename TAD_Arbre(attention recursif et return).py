#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Arbre:
    """Implémentation de la structure de données «Arbre» en Python."""

    # creerArbre(arbre, racine) → arbre
    def __init__(self, racine=None):
        self._racine = racine    # valeur
        self._gauche = None      # Sous-arbre gauche
        self._droit = None       # Sous-arbre droit

    # estVide(arbre) → booléen
    def estVide(self):
        return self._racine is None

    # racine(arbre) → valeur
    def racine(self):
        assert not self.estVide(), "L'arbre est vide."
        return self._racine

    #  sag(arbre) → arbre
    def sag(self):
        return self._gauche

    # sad(arbre) → arbre
    def sad(self):
        return self._droit

    #  assembler(arbre, arbre, arbre) → arbre
    def assembler(self, sag = None, sad = None):
        assert not self.estVide(), "L'arbre est vide."
        self._gauche = sag
        self._droit = sad

    # définition de l'impression (print) de l'objet
    def __str__(self):
        return "({},{},{})".format(self._racine, self._gauche, self._droit)

    # définition de l'affichage d'appel de l'objet
    def __repr__(self):
        return "Arbre()"

    # affiche l'arbre binaire dans la console
    def afficher(self):
        if self.estVide():
            print("L'arbre est vide.")
        else:
             self._afficher(0)

    def _afficher(self, level):
        if self._droit:
            self._droit._afficher(level + 1)
        print("{}{}".format(' ' * 4 * level, self._racine))
        if self._gauche:
            self._gauche._afficher(level + 1)



    # ---------------------------------------------#
    # PARTIE - ALGORITHMES SUR LES ARBRES BINAIRES #
    # ---------------------------------------------#

    # parcoursLargeure(arbre) → liste     (parcours en largeur de l'arbre)
    def parcoursLargeur(self):
        # A COMPLETER

        return p

    # parcoursPre(arbre) → liste     (parcours préfixé de l'arbre)
    def parcoursPre(self):
        if self.estVide():
            return []
        else:
            return self._parcoursPre([])

    def _parcoursPre(self, liste):
        liste.append(self.racine())
        if self.sag() : liste.extend(self.sag().parcoursPre())
        if self.sad() : liste.extend(self.sad().parcoursPre())


        return liste

    # parcoursInf(arbre) → liste     (parcours infixé de l'arbre)
    def parcoursInf(self):
        if self.estVide():
            return []
        else:
            return self._parcoursInf([])

    def _parcoursInf(self, liste):
        if self.sag() : liste.extend(self.sag().parcoursPre())
        liste.append(self.racine())
        if self.sad() : liste.extend(self.sad().parcoursPre())

        return liste

    # parcoursPost(arbre) → liste     (parcours postfixé de l'arbre)
    def parcoursPost(self):
        if self.estVide():
            return []
        else:
            return self._parcoursPost([])

    def _parcoursPost(self, liste):
        if self.sag() : liste.extend(self.sag().parcoursPre())
        if self.sad() : liste.extend(self.sad().parcoursPre())
        liste.append(self.racine())


        return liste

    # rechercher(arbre, valeur) → booléen
    def taille(self):
        if self.estVide():
            return 0
        else:
            t = 1
        if self.sag():
            t += self.sag().taille()
        if self.sad():
            t += self.sad().taille()
        return t

        return n

    # hauteurNoeud(arbre, valeur) → entier
    def hauteurNoeud(self, valeur):
        if self.estVide():
            assert False, "L'arbre est vide."
        if not valeur in self.parcoursPre():
            assert False, "La valeur " + str(valeur) + " n'est pas dans l'arbre."
        dicoN = self._hauteursNoeuds({}, 1)
        return dicoN[valeur]

    def _hauteursNoeuds(self, dicoN, niv):
        dicoN[self._racine] = h
        if self.sag():
          dicoN = self.sag()._hauteursNoeuds(dicoN, h+1)
        if self.sad():
          dicoN = self.sad()._hauteursNoeuds(dicoN, h+1)
        return dicoN

        return dicoN

    # hauteur(arbre) → entier
    def hauteur(self):
        if self.estVide():
            return 0
        else:
            return max(self._hauteursNoeuds({}, 1).values())

        return h

    # ----------------------------------------------------------#
    # PARTIE - ALGORITHMES SUR LES ARBRES BINAIRES DE RECHERCHE #
    # ----------------------------------------------------------#

    # rechercher(arbre_binaire, valeur) → booléen
    def rechercher(self, x):
        if x == self.racine() :
            print(x, self.racine(), x == self.racine())
            return True
        if x < self.racine() and not self.sag() is None :
            self.sag().rechercher(x)
            #return self.sag().rechercher(x)
        if x > self.racine() and not self.sad() is None :
            self.sad().rechercher(x)
            #return self.sad().rechercher(x)
        #print(x, "tail")
        return False




    # ajouter(arbre_binaire, valeur) →
    def ajouter(self, valeur):
        # A COMPLETER
        pass # A remplacer

    #  min(arbre_binaire) → Entier
    def minimum(self):
        # A COMPLETER

        return m

    #  max(arbre_binaire) → Entier
    def maximum(self):
        # A COMPLETER

        return m


a=Arbre(23)
b=Arbre(13)
c=Arbre(54)
a.assembler(b,c)
a.afficher()
print(*[
a.rechercher(23),
a.rechercher(13),
a.rechercher(54),
a.rechercher(10),
a.rechercher(15),
a.rechercher(25),
a.rechercher(55)
])
