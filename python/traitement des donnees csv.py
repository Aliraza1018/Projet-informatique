##import csv
##fichier = open("eleves.csv")
##table =list(csv.reader(fichier))
##"K:\Bureau\

##import csv
##fichier = open("eleves.csv")
##table =list(csv.DictReader(fichier))

##import csv
##fichier = open("eleves.csv")
##table = list(csv.DictReader(fichier, delimiter=";"))

##import csv
##fichier = open("Resultat-des-lycees.csv")
##table = list(csv.DictReader(fichier, delimiter=";")

##for x in table:
##    x["jour"]= int (x["jour"])
##        mois = int (x["mois"])
##    if mois < 1 or mois > 12:
##        exit("mois invalide dans le fichier CSV")
##    x["mois"] = mois
##    x ["annee"]=int( x["annee"])

import csv
fichier = open("Resultat-des-lycees.csv")
table = list(csv.DictReader(fichier, delimiter=";"))

print(type(table[4000]["Taux Brut de Reussite serie S"]))

for x in table:
    if x["Taux Brut de Reussite serie S"] != '':
        print("je ne convertis pas")
    else:
       x["Taux Brut de Reussite serie S"] = int (x["Taux Brut de Reussite serie S"])



print(type(table[4000]["Taux Brut de Reussite serie S"]))
print(table[4000]["etablisssement"])

