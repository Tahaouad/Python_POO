class Etudiant:         #Création de la classe Etudiant
    def __init__(self): #Constructeur par défaut de la classe (sans parametre)
        self.nom="ALI"  #Création de l'attribut nom
        self.note=10.0  #Création de l'attribut note
        self.Age=18     #Création de l'attribut Age
#Début du PP
print("Début du programme")
E1 = Etudiant()    #Création du 1 er objet E1 de type Etudiant
E2 = Etudiant()    #Création du 2 eme objet E2 de type Etudiant
E1.nom="Mohamed"   #changement de la valeur de l'attribut nom de l'objet E1
E2.nom="Ahmed"     #changement de la valeur de l'attribut nom de l'objet E2
E1.Age=19     #changement de la valeur de l'attribut Age de l'objet E1
E2.note=15    #changement de la valeur de l'attribut note de l'objet E2
E1.ville="CASA" #création d'un attribut ville seulemnt pour l'objet E1
print("le nom de E1 est :",E1.nom,"la note de E1 est:",E1.note,"l'age de E1 est:",E1.Age)
print("le nom de E2 est {},sa note est {}".format(E2.nom,E2.note))
print(E1.ville)
print(E2.ville) #Error 
