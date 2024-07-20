class Voiture:
    """
    Voitures
    """
    #Création des Voitures
    def __init__(self,C=None,A=None):
        self.couleur=C
        self.Annee=A

    def __del__(self):
        print("Je suis le déstructeur")
    def Afficher(self):
        print("Couleur:",self.couleur,"Annee:",self.Annee)
V1 = Voiture("rouge",2020)
V2 = Voiture("Noir",2021)

print(V1.couleur)
print(V2.couleur)
del V1
V2.Afficher()
print(V2.__doc__)#Afficher la documentation de la classe
print(V2.__dict__)#Affciher les attributs et leurs valeurs sous forme de Dict
print(dir(V2))#Afficher les Methodes accessibles pour l'objet V2

