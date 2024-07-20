class vehicule:
    def __init__(self,M=None,MS=None,MIL=None):
        self.__marque=M
        self.max_speed=MS
        self.mealage=MIL
    def afficher(self):
        print("Matricule : {} MAX \SPEED : {} Mealage: {}".format(self.__marque,self.max_speed,self.mealage))
    def get_marque(self):
        print(self.__marque)
    def set_marque(self,M):
        self.__marque=M
    def del_marque(self):
        del self.__marque
    Marque = property(get_marque,set_marque,del_marque,"TEST vehicule")
class vehucles():
    def __init__(self):
        pass
class bus(vehicule):
    def __init__(self,M,MS,MIL,MAT=None,C=None):
        self.Matricule=M
        self.capacite=C
        vehicule.__init__(self,M=None,MS=None,MIL=None)
bus1=bus("GOLF",250,22,2222,2121122)
bus1.afficher()
bus1.Marque="Dacia"
print(bus1.Marque)





