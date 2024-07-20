class Moteur:
    def __init__(self,R=None,F=None):
        self.Réf=R
        self.Fabriquant=F
M1 = Moteur(45667,"BMW")
M2 = Moteur(67889,"Renault")
class Vehicule:
    def __init__(self,M=None,Ann=None,Col=None,Mo=M1):
        self.Marque=M
        self.Année=Ann
        self.Couleur=Col
        self.MT=Mo
    
    def Afficher(self):
        print("Marque voiture:",self.Marque)
        print("Annéé voiture:",self.Année)
        print("Couleur voiture:",self.Couleur)
        print("Infos Moteur:\n","Réféence:",self.MT.Réf,
              "Fabriquant:",self.MT.Fabriquant)
V1 = Vehicule("Clio",2020,"bleu",M2)
V2 = Vehicule("BMW",2022,"Noir",M1)
V1.Afficher()
print("----------------")
V2.Afficher()
V3 = Vehicule()
print("----------------")
V3.Afficher()
print(V1)
