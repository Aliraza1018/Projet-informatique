import csv
fichier = open("exo 2.csv")
table =list(csv.DictReader(fichier,delimiter=";"))
##
for x in table:
    x["REF"]= int (x["REF"])
    x["QTE"] = int (x["QTE"])
    x["PRIX"]= float (x["PRIX"])


##Exercice 1:

def verifie_quantites(table):
    if x["QTE"] >0:
        return "true"


def nombre_produit(table):
    nbr_de_produit =0
    for x in table:
        if x["QTE"] >0:
            nbr_de_produit += x["QTE"]
    print(nbr_de_produit)

def purge_commande(table):
    purge_commande =[]
    for x in table:
        if x["QTE"] >0:
            purge_commande.append(x)
    return purge_commande

def prix(table):
    prix=0
    purge_commande(table)
    for x in table:
        if x["QTE"]>0:
            prix+=x[ "QTE"]*x["PRIX"]
    return prix

poids_produit={18635:100,15233:200,20112:300}
def poids_commande(table):
    poids_commande=0
    for x in table:
        if x["QTE"]>0:
##            poids_commande+=poids_produit[x["REF"]]*x["QTE"]
            poids_commande+=poids_produit.get(x["REF"])*x["QTE"]
    return poids_commande

def articles_lourds(table):
    bon_de_commande=[]
    for x in table:
        if poids_produit[x["REF"]] >=200:
            bon_de_commande.append(x)
    return bon_de_commande










