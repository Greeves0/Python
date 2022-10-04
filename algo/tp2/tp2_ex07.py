# Créé par GUILLAUME.REEVES, le 27/09/2022 en Python 3.7

valeur=0
max=0
while valeur>=0:
    valeur=int(input("saisir un nombre positif ou alors si vous voulez sortir, mettre un nombre négatif"))
    if valeur>max:
        max=valeur

print("le nombre max est",max)
