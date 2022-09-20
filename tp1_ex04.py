# Créé par GUILLAUME.REEVES, le 15/09/2022 en Python 3.7

valeur_tva=20

prix_ht=40
tva=prix_ht*valeur_tva/100;
prix_ttc=prix_ht+tva;

print("Prix HT du prduit:",prix_ht,"€")
print("Indice de la TVA en 2015: ",valeur_tva," %")
print("Valeur de la TVA: ",tva," €")
print("Prix TTC: ",prix_ttc," €")