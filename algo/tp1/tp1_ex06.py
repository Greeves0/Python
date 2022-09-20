# Créé par GUILLAUME.REEVES, le 15/09/2022 en Python 3.7

age=int(input("Donner l'âge de votre animal")) #ou on peut directement mettre un nombre
if(age>=6) and (age<=7):
    print("Poussin")
elif(age>=8) and (age<=9):
    print("Pupille")
elif(age>=10) and (age<=11):
    print("Minime")
elif(age>=12) and (age<=15):
    print("Cadet")
elif(age>=15):
    print("Hors catégorie")