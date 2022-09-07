# -*- coding: utf-8 -*-
import sys, os

# Printing on/off
def blockPrint():
    sys.stdout = open(os.devnull, 'w')
def enablePrint():
    sys.stdout = sys.__stdout__

blockPrint()
from Pile import Pile
enablePrint() 


class File :
    """Implémentation du TAD «File» en Python. """

    def __init__(self, taille) :
        """Ce constructeur sert à instancier un objet de la classe File. """
        self.taille = taille
        self._pileA = Pile(taille)
        self._pileB = Pile(taille)

    def _AversB(self) :
        while not self._pileA.est_vide() :
            blockPrint()
            self._pileB.empiler(self._pileA.depiler())
            enablePrint()

    def _BversA(self) :
        while not self._pileB.est_vide() :
            blockPrint()
            self._pileA.empiler(self._pileB.depiler())
            enablePrint()

    def enfiler(self, element) :
        """Empile un élément au sommet de la file. """
        if self.est_pleine() :
            print("Impossible, la file est pleine")
        else :
            blockPrint()
            self._pileA.empiler(element)
            enablePrint()

    def defiler(self) :
        """Extrait et retourne l'élément au sommet de la pile. """
        if self.est_vide() :
            print("Impossible, la pile est vide. ")
        else :
            blockPrint()
            self._AversB()
            ret = self._pileB.depiler()
            self._BversA()
            enablePrint()
            return ret

    def est_vide(self) :
        """La pile est-elle vide ? """
        return not self._pileA.contenu

    def est_pleine(self) :
        """La pile est-elle pleine ? """
        if len(self._pileA.contenu) >= self.taille :
            return True
        else :
            return False

    def nbr_elements(self) :
        """Donne le nombre d'éléments dans la pile"""
        return len(self._pileA.contenu)

    def __repr__(self) :
        return f"entrée --> {self._pileA.contenu[::-1]} --> sortie"
    __str__ = __repr__

# Fin de la classe File ; on peut la manipuler maitenant :
fileA = File(6)

for k in range(1,10) :
    print("On enfile l'élément ", k)
    fileA.enfiler(k)
    print("file : ", fileA)

print("On défile deux éléments : ", fileA.defiler(), fileA.defiler())
print("file : ", fileA)
