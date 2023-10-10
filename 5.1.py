# Créé par guillaume.reeves, le 06/10/2023 en Python 3.7
class Point:
    def __init__(self, abscisse, ordonnee):
        self.x, self.y = abscisse, ordonnee
    def translater(self, dx, dy):
        self.x+=dx
        self.y+=dy
    def homothetie(self, k):
        self.x *= k
        self.y *= k
    def __repr__(self):
        return str(self.x)+","+str(self.y)

p=Point(3,4)
print(p)
p.homothetie(2)
print(p)
