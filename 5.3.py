# Créé par guillaume.reeves, le 06/10/2023 en Python 3.7
class Rectangle:
    def __init__(self, longueur,largeur):
        self.longueurDuCote=longueur
        self.largeurducote=largeur
    def aire(self):
        return self.longueurDuCote*self.largeurducote
    def perimetre(self):
        return self.longueurDuCote*2+self.largeurducote*2
    def __repr__(self):
        return ("P="+str(self.perimetre())+" , "+"A="+str (self.aire()))

c1=Rectangle(5,10)
c2=Rectangle(10,20)
c3=Rectangle(100,200)
c4=Rectangle(15,30)
print(c1,'-',c2,'-',c3,'-',c4)
