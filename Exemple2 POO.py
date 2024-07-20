class Etudiant:#Création de la classe Etudiant
    """
    Classe des Etudiants
    """
    nbre_Etudiant=0
    def __init__(self,a=None,b=None,c=None):#Constructeur paramétré (3 parametres obligatoires)
        
        self.nom=a #création de l'attribut Nom
        self.CIN=b #Création de l'atribut CIN
        self.note=c    #Création de l'attribut note
        Etudiant.nbre_Etudiant += 1
    def afficher(self,n):
        match n:
            case 1:    
                print("Bonjour",self.nom)
            case 2:
                print("Hello",self.nom)
            case _:
                print("Error")
print("Début du Programme")

E1 = Etudiant("ALI",123455,17)  #création de l'objet e1 avec 3 parametres
E2 = Etudiant()
E2.nom="Ahmed"
E2.CIN=45678
E2.note=19
E3 = Etudiant()
print(Etudiant.nbre_Etudiant)
E1.afficher(1)
E2.afficher(2)
E3.afficher(6)
