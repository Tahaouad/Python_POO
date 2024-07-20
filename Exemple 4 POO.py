class Etudiant:#Création de la classe Etudiant
    """
    Classe des Etudiants
    """
    nbre_Etud = 0 #Attribut de classe
    def __init__(self,name=None,C=None,No=None):#Constructeur paramétré intélligent(3 parametres obligatoires)
        self.nom=name #création de l'attribut Nom 
        self.CIN=C  #Création de l'atribut CIN
        self.note=No    #Création de l'attribut note
        Etudiant.nbre_Etud +=1
    def afficher(self,n):
        print("je suis {},mon CIN est {},ma note est {}".format(self.nom,self.CIN,self.note))
        match n:
            case 1:
                print("Bonjour")
            case 2:
                print("Hello")
            case _:
                print("langue inconnue")

print("Début du Programme")

E1 = Etudiant("Ahmed",12345,18)#Création d'un objet Etudiant E1 avec 3 parametres
E2 = Etudiant("SARA",56789,17)#Création d'un objet  Etudiant E2 avec 3 parametres
E3 = Etudiant()#Possible car les parametres sont initialisés
E1.afficher(2)
E2.afficher(1)
E3.afficher(6)

