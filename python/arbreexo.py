def log2(n):
    if n==1:
        return 0
    else:
        return 1+log2(n//2)


##arbre = (12,noeud_6(6,none,9),arbre_1)
def est_feuille(mon_arbre):
    '''renvoie un booléen permettant de savoir si mon_arbre est une feuille'''
    if mon_arbre[0]!=None:
        return mon_arbre[1]==None and mon_arbre[2]==None