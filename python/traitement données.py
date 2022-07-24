#import csv
#fichier = open("K:\profil\Bureau\eleves.csv")
#table = list (csv.reader(fichier))

import csv
##fichier = open("K:\profil\Bureau\eleves.csv")
##table = list (csv .DictReader (fichier))
fichier = open ("K:\profil\Bureau\Resultat-des-lycees.csv")
table = list(csv.DictReader(fichier, delimiter=";"))


print(type(table[4000]["Taux Brut de Reussite serie S"]))


for x in table:
    if  x["Taux Brut de Reussite serie S"]!='':
        x["Taux Brut de Reussite serie S"] = int (x["Taux Brut de Reussite serie S"])

print(type(table[4000]["Taux Brut de Reussite serie S"]))
print(table[4000]["Etablissement"])