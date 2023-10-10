# Créé par guillaume.reeves, le 06/10/2023 en Python 3.7

class Point:
    def placer(self, abscisse, ordonnee):
        self.x=abscisse
        self.y=ordonnee
    def translater(self, dx, dy):
        self.x+=dx
        self.y+=dy

p1=Point()
p1.placer(12,7)
print(p1.x,p1.y)
p1.translater(2,-3)
print(p1.x,p1.y)

p2=Point()
p2.placer(5,3)
print(p2.x,p2.y)
p2.translater(-6,2)
print(p2.x,p2.y)

