class Fruit:
    nom="Fruit à manger" 
    def __init__(self, couleur, poids_g):
            print("J’adore les fruits.")
            self.couleur = couleur
            self.poids_g = poids_g
            
pomme =Fruit("verte",100)
Orange = Fruit("Orange",150)
print(pomme.nom) #affiche fruit à manger
print(Orange.nom)
print(Fruit.nom) #affiche fruit à manger
