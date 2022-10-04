# Créé par guillaume.reeves, le 04/10/2022 en Python 3.7

from random import *
nombre = randint(1,20)
valeur=0

while valeur!=nombre:
    valeur=int(input("Donner nous un chiffre compris entre 0 et 20"))
    print(valeur)
    if valeur>nombre:
        print("est trop grand")
    elif valeur<nombre:
        print("est trop petit")
    else:
        print("exact")