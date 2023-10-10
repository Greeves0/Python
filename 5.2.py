# Créé par guillaume.reeves, le 06/10/2023 en Python 3.7
class Carre:
    def __init__(self, longueur):
        self.longueurDuCote=longueur
    def aire(self):
        return self.longueurDuCote**2
    def perimetre(self):
        return self.longueurDuCote*4
    def __repr__(self):
        return ("P="+str(self.perimetre())+" , "+"A="+str (self.aire()))

c1=Carre(5)
c2=Carre(10)
c3=Carre(100)
c4=Carre(15)
print(c1,'-',c2,'-',c3,'-',c4)