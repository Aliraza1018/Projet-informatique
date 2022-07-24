import csv
f2007 = open("Prénoms2007.csv")
f2008 = open("Prénoms2008.csv")
t2007 = list(csv.DictReader(f2007,delimiter=";"))
t2008 = list(csv.DictReader(f2008,delimiter=";"))

notes = open("notes (1).csv")
eleves = open("eleves (2).csv")
notes = list(csv.DictReader(notes))
eleves = list(csv.DictReader(eleves))

t20078 = t2007 + t2008

##Manipulation 2:
fille2007 = [f for f in t2007 if ["SEXE"] == "FEMME"]

#Manipulation 2:

##def fusion(e,n):
##    return {"prenom":e["prenom"],"jour":e["jour"],"mois":e["mois"],"annee":e["annee"], "projet":e["projet"],"note":n["note"]}

##t=[]
##for e in eleves:
##    for n in notes:
##        if e["prenom"]==n["prenom"]:
##            t.append(fusion(e,n))

#Manipulation 3:

##t=[fusion(e,n) for e in eleves for n in notes if e["prenom"]==n["prenom"]]

##t =[fusion(e,n) for e in eleves for n in notes if e["id"]==n["id"]]


#Manipulation 1:

Membre = open("Membre.csv")
Livres = open("Livres.csv")
Pret = open("Pret.csv")
Membre = list(csv.DictReader(Membre,delimiter=";"))
Livres = list(csv.DictReader(Livres,delimiter=";"))
Pret= list(csv.DictReader(Pret,delimiter=";"))


#Manipulation 2:
# Fusion de Membre et Pret
def fusion(e,n):
    return {"Prénom":e["Prénom"],"idm":e["idm"],"idl":n["idl"]}

t=[fusion(e,n) for e in Membre for n in Pret if e["idm"]==n["idm"]]
# Fusion de Pret et Livres
def fusion2(e,n):
    return {"idl":e["idl"], "idm":e["idm"],"titre":n["titre"]}

b=[fusion2(e,n) for e in Pret for n in Livres if e["idl"]==n["idl"]]

#Manipulation 3:
# Fusion de Membre , Pret et Livres
def fusion3(e,n,m):
    return {"Prénom":e["Prénom"],"idm":e["idm"],"idl":n["idl"], "titre":m["titre"]}

c=[fusion3(e,n,m) for e in Membre for n in Pret for m in Livres if e["idm"]==n["idm"] and n["idl"]== m["idl"]]

