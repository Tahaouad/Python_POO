class Compte:
    Nbre_Compte=0
    def __init__(self,Num=None,Name=None,Sold=None):
        self.Num_Compte=Num
        self.Nom_Pr=Name
        self.__Solde=Sold
        Compte.Nbre_Compte +=1
    def Verser(self):
        print("Donner le montant de versement")
        v=float(input())
        self.__Solde=self.__Solde+v
        return self.__Solde
    def Retirer(self):
        print("Donner le montant de Retrait")
        v=float(input())
        self.__Solde=self.__Solde-v
        return self.__Solde
    def __str__(self):
        return "Numéro de compte:"+str(self.Num_Compte)+"\n"+"Nom:"+self.Nom_Pr+"\n"+"Solde:"+str(self.__Solde)
Compte1 = Compte(2020,"NADIR SOUFIANE",20000)
Compte2 = Compte(2021,"NAD SOU",1000)
Compte1.Verser()
Compte1.Retirer()
print(Compte1)
print("le nombre de comptes Crées est ",Compte.Nbre_Compte)
