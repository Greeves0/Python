# Créé par guillaume.reeves, le 06/10/2023 en Python 3.7
class Point:
    def __init__(self, abscisse, ordonnee):
        self.x, self.y = abscisse, ordonnee
    def translater(self, dx, dy):
        self.x+=dx
        self.y+=dy

p1=Point(12,7)
print(p1.x,p1.y)
p1.translater(2,-3)
print(p1.x,p1.y)
