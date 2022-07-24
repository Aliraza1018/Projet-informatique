##import csv
##fichier = open("eleves3.csv")
##table =list(csv.DictReader(fichier,delimiter=";"))
####
##for x in table:
##    x["jour"]= int (x["jour"])
##    x["mois"] = int (x["mois"])
##    x["annee"] = int (x["annee"])


##Manipulation 1 :
##t= [21,13,34,8]
##sorted(t)

##Manipulation 2 :
##b= ["banane","pomme","cassis","fraise"]
##sorted(b)


##Manipulation 3 :
##
##def prenom(x):
##    return x["prenom"]
##tri_eleves = sorted(table,key=prenom)
##print(tri_eleves)

##Manipulation 4 :
##
##def prenom(x):
##    return x["prenom"]
##tri_eleves = sorted(table,key=prenom , reverse= True)
##print(tri_eleves)

##Manipulation 5 :

##def note_puis_nom(x):
##    return x["note"] , x ["nom"]
##liste_a_afficher = sorted(table, key=note_puis_nom)
##print(liste_a_afficher)

##Exercices Trie d'une table:
##Exercice 1:
##def mois(x):
##    return x["mois"]
##tri_eleves = sorted(table,key=mois)
##print(tri_eleves)

##Exercice 2:

##def mois_puis_jour(x):
##    return x["mois"] , x ["jour"]
##liste_a_afficher = sorted(table, key=mois_puis_jour)
##print(liste_a_afficher)

##Exercice 3:

##def age(x):
##    return x["annee"] , x["mois"] , x["jour"]
##liste_a_afficher = sorted(table, key=age, reverse = True)
##print(liste_a_afficher)

##Exercice 4:

import csv
fichier = open("sac a dos.csv")
table =list(csv.DictReader(fichier,delimiter=";"))
##
for x in table:
    x["Poids"]= int (x["Poids"])
    x["Valeur"] = int (x["Valeur"])

##max=0
##valeur=0
##pt=10
##for x in table:
##
##    if x["Poids"] <= pt:
##        max += x["Poids"]
##        valeur+=x["Valeur"]
##        print(x["Objet"])
##        pt=pt-max
##        print ("max =", max ,"Valeur =" , valeur)
##
##max=0
##pt=10
##valeur=0
##def Poids(x):
##    return x["Poids"]
##tri_Poids = sorted(table , key=Poids)
####print(tri_Poids)
##
##
##for x in tri_Poids:
##    if x["Poids"] <= pt:
##        max = x["Poids"]
##        valeur += x["Valeur"]
##        print(x["Objet"])
##        pt=pt-max
##        print ("max=",max)
##        print("pt=",pt)
##        print("valeur =" , valeur)

##max=0
##pt=10
##valeur=0
##def valeur_puis_poids(x):
##    return x["Valeur"] , x["Poids"]
##valeur_puis_poids = sorted(table , key=valeur_puis_poids)
##print(valeur_puis_poids)


##for x in Poids_valeur:
##    if x["Poids"] <= pt:
##        max = x["Poids"]
##        valeur += x["Valeur"]
##        print(x["Objet"])
##        pt=pt-max
##        print ("max=",max)
##        print("pt=",pt)
##        print("valeur =" , valeur)



for e in table:
    e["rapport"]=e["Valeur"]/e["Poids"]


def rapport(x):
    return x["rapport"]
tri_rapport = sorted(table , key=rapport , reverse=True)
print(tri_rapport)


##def rapport_puis_poids(x):
##    return x["rapport"] , x["Poids"]
##rapport_puis_poids = sorted(table , key=rapport_puis_poids , reverse=True)
##print(rapport_puis_poids)

print(table)
table.append("Valeur": 7200; 'rapport': 1200.0, 'Objet': 'B', 'Poids': 6)
