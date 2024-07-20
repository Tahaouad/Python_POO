class Vehicule:
    """
    Classe pour la création de Vehicules
    """
    def __init__(self,M=None,Col="rouge"):
        self.__Matricule=M
        self.couleur=Col
    def set_Matricule(self):
        self.__Matricule=int(input("Donner le nouveau Matricule"))
    def get_Matricule(self):
       return self.__Matricule
 
#Début de programme
        
voiture = Vehicule(122356,"Noir")
print(voiture.get_Matricule())
voiture.set_Matricule()
print(voiture.get_Matricule())


