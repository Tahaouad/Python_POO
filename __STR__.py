class Personne:
    def __init__(self,Nom=None):
        self.Name=Nom
    def __str__(self):
        return("le nom est "+self.Name)
P1 = Personne("ALI")
print(P1)
    
