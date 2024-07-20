class Myclasse:
    """
    Classe Niveau+Groupe
    """
    def __init__(self,N=None,G=None):
        self.Niveau=N
        self.Groupe=G
C1 = Myclasse("Bac","G1")
C2 = Myclasse("TC","G6")

class Eleve:
    def __init__(self,Name=None,Not_s=None,Ref=None):
        self.Nom=Name
        self.Notes=Not_s
        self.Reference=Ref
    def Afficher(self):
        print("Nom:",self.Nom)
        print("Notes:",self.Notes)
        print("Réference:","Niveau:",self.Reference.Niveau,"Groupe:",
              self.Reference.Groupe)
        print("Moyenne:",self.Moyenne())
    def Moyenne(self):
        M=sum(self.Notes)/len(self.Notes)
        return M
Eleve1 = Eleve("ALI",[13,15.5,18],C2)
Eleve2 = Eleve("Mohamed",[14,17,10],C1)
Eleve1.Afficher()
print("----------------------------------------------------------")
Eleve2.Afficher()
