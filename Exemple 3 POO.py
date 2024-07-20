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
        

print("Début du Programme")

E1 = Etudiant("Ahmed",12345,18)#Création d'un objet Etudiant E1 avec 3 parametres
E2 = Etudiant("SARA",56789,17)#Création d'un objet  Etudiant E2 avec 3 parametres
E3 = Etudiant()#Possible car les parametres sont initialisés
print("le nom de E1 est",E1.nom,"son CIN est:",E1.CIN,"sa note est:",E1.note)
print("le nom de E2 est {},son CIN est {},sa note est {}".format(E2.nom,E2.CIN,E2.note))
print("le nom de E3 est",E3.nom,"son CIN est:",E3.CIN,"sa note est:",E3.note)
print(Etudiant.nbre_Etud)
