# Créé par GUILLAUME.REEVES, le 27/09/2022 en Python 3.7

G=int(input("Donner le nombre que vous souhaiter multiplier"))
R=G
for n in range(1,11):
    G=R*n
    print(R,"*",n,"=",G)
