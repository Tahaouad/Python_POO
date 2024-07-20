class Entreprise:
    def __init__(self,RS=None,NE=None):
        self.Raison_sociale=RS
        self.Nom_Epse=NE
E1 = Entreprise("SA","RMA")
E2 = Entreprise("SA","SAHAM")

class Salarié:
    """
    Classe des Salarié
    """
    def __init__(self,M=None,Name=None,P=None,Sal=None,T_C=None,S=None):
        self.Matricule=M
        self.Nom=Name
        self.Prénom=P
        self.Salaire=Sal
        self.taux_charge=T_C
        self.société=S
    def Afficher(self):
        print("le Matricule du salarié est:{}".format(self.Matricule))
        print("le Nom du salarié est:{}".format(self.Nom))
        print("le Prénom du salarié est:{}".format(self.Prénom))
        print("le Salaire est:{}".format(self.Salaire))
        print("le Taux de charge est:{}".format(self.taux_charge))
        print("la société de l'employé est:",self.société.Nom_Epse,
              "sa raison sociale esr:",self.société.Raison_sociale)
    def Calcul_S_N(self):
        Salaire_Net = self.salaire-(self.salaire*self.taux_charge)
        return Salaire_Net
S1 = Salarié(1234,"ALI","AA",5000.0,0.25,E1)
S2 = Salarié(1235,"AHMED","ALI",10000.0,0.25,E2)
S3 = Salarié(8734,"ALI","MM",15000.0,0.25,E1)

S1.Afficher()
print("-----------------------------------")
S2.Afficher()
print("-----------------------------------")
S3.Afficher()
