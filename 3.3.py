# Créé par guillaume.reeves, le 06/10/2023 en Python 3.7
class Point:
    def __init__(self, abscisse, ordonnee):
        self.x, self.y = abscisse, ordonnee
    def translater(self, dx, dy):
        self.x+=dx
        self.y+=dy
    def __repr__(self):
        return str(self.x)+","+str(self.y)

p1=Point(12,7)
print(p1)
p1.translater(2,-3)
print(p1)