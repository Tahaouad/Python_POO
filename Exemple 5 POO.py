class Moteur:
    def __init__(self,M=None,P=None):
        self.Marque_Mt=M
        self.Puissance=P
        
Mt1 = Moteur("VW",200)
Mt2 = Moteur("BMW",150)
class Voiture:
    def __init__(self,M1=None,C=None,m_t=None):
        self.Marque_V = M1
        self.couleur = C
        self.mt=m_t
    def afficher (self):
        print("Marque:{}".format(self.Marque_V))
        print("Couleur:{}".format(self.couleur))
        print("Marque:{}".format(self.mt.Marque_Mt))
        print("Puissance:{}".format(self.mt.Puissance))
v1 = Voiture("Mercedes","noir",Mt1)
v2 = Voiture("BMW","noir",Mt2)

v1.afficher()
v2.afficher()
