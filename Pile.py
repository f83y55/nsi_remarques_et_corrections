# -*- coding: utf-8 -*-

class Pile :
    """Implémentation du TAD «Pile» en Python. """

    def __init__(self, taille) :
        """Ce constructeur sert à instancier un objet de la classe Pile. """
        self.taille = taille
        self.contenu = []

    def empiler(self, element) :
        """Empile un élément au sommet de la pile. """
        if self.est_pleine() :
            print("Impossible, la pile est pleine")
        else :
            self.contenu.append(element)

    def depiler(self) :
        """Extrait et retourne l'élément au sommet de la pile. """
        if self.est_vide() :
            print("Impossible, la pile est vide. ")
        else :
            return self.contenu.pop()

    def est_vide(self) :
        """La pile est-elle vide ? """
        if self.contenu == [] :
            return True
        else :
            return False

    def est_pleine(self) :
        """La pile est-elle pleine ? """
        if len(self.contenu) >= self.taille :
            return True
        else :
            return False

    def nbr_elements(self) :
        """Donne le nombre d'éléments dans la pile"""
        return len(self.contenu)

# Fin de la classe pile ; on peut la manipuler maitenant :
pileA = Pile(6)

for k in range(1,10) :
    print("On empile l'élément ",k)
    pileA.empiler(k)
    print("nbr d'éléments dans la pile : ",pileA.nbr_elements())

print("On dépile deux éléments : ", pileA.depiler(), pileA.depiler())
print("nbr d'éléments dans la pile : ", pileA.nbr_elements())
