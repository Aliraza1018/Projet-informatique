#addition de nombre binaire avec 1

def nb_relatif(prem):
    deu = "00000001"
    resultat = ""
    retenu = 0
    somme = 0
    for k in range ((len (prem)-1),-1,-1):
        bit1 = int(prem[k])
        bit2 = int(deu[k])

        if (bit1+bit2+retenu) == 3:
            retenu = 1
            somme = 1

        elif bit1+bit2+retenu == 2:
            retenu = 1
            somme = 0

        elif bit1+bit2+retenu == 1:
            retenu = 0
            somme = 1
        else:
            retenu = 0
            somme = 0
        resultat = str(somme) + resultat
    print("nombre=", resultat)

# inverser le nombre binaire

def inverse(nb):
    nb=str(nb)
    resultat=""
    for k in range (len (nb)):
        nombre = int(nb[k])
        if nombre == 1:
            nombre = 0
        elif nombre == 0:
            nombre = 1
        resultat=resultat + str(nombre)
    print (resultat)
