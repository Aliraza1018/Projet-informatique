##Question 2:

import csv
Fichier = open("notes.csv")
table = list(csv.DictReader(Fichier, delimiter= ","))

##Question 3:
##print(len(table))
##print(len(table[0])-1)
##"Nombre d'élèves est de 4 et nombre de matière est de 3"

##Question 4:

def note(table):
    for e in table:
        if e["Nom"]=="Luna":
            print(e["Math"])

## Question 5:
def convertir(table):
    for e in table:
        e["Math"]= int(e["Math"])
        e["Nsi"]= int(e["Nsi"])
        e["Anglais"]= int(e["Anglais"])
    print(table)

##Question 6:
def eleve(table):
    for e in table:
        if e["Nom"]=="Marc":
            return "True"
##Question 7:
##somme = 0
def moyenne(table):
    somme = 0
    for e in table:
        somme += e["Nsi"]
        moyenne = somme / (e[len["Nsi"]])
        print (moyenne)


