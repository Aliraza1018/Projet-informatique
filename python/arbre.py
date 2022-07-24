def sous_arbre_gauche(arbre):
    return arbre[1]


def sous_arbre_droit(arbre):
    return arbre[2]

def vide(arbre):
    return arbre == None
print (sous_arbre_gauche(arbre1))





noeud_4=("D",None,None)
noeud_5=("F",None,None)
noeud_6=("G",None,None)
noeud_3= ("E",noeud_5,noeud_6)
noeud_2= ("B",None,noeud_4)
noeud_1=("A",noeud_2,noeud_3)