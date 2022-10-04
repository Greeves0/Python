# Créé par guillaume.reeves, le 04/10/2022 en Python 3.7
valeur=0
max=0
for n in range(0,5):
    valeur=int(input("saisir un nombre"))
    if valeur>max:
        max=valeur

print("le nombre max est",max)
