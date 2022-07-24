##def addition(prem,deu):
##
##    resultat=""
##    retenu=0
##    somme=0
##    for k in range ((len (prem)-1),-1,-1):
##        bit1=int(prem[k])
##        bit2=int(deu[k])
##
##        if (bit1+bit2+retenu)==3:
##            retenu=1
##            somme=1
##
##        elif bit1+bit2+retenu==2:
##            retenu=1
##            somme=0
##
##        elif bit1+bit2+retenu==1:
##            retenu=0
##            somme=1
##        else:
##            retenu=0
##            somme=0
####        print("retenu=",retenu)
####        print("somme=",somme)
##        resultat=str(somme)+resultat
##    print("nombre=",resultat)


def inverse(nmbr):
    nmbr=str(nmbr)
    resultat=""
    for k in range (len (nmbr)):
        nombre=int(nmbr[k])
        if nombre==1:
            nombre=0
            resultat+=str(nombre)

        elif nombre==0:
            nombre=1
            resultat+=str(nombre)
    return resultat



def addcomplement(prem):
    prem=str(prem)
    deu = "00000001"
    resultat=""
    retenu=0
    somme=0
    for k in range ((len (prem)-1),-1,-1):
        bit1=int(prem[k])
        bit2=int(deu[k])

        if (bit1+bit2+retenu)==3:
            retenu=1
            somme=1

        elif bit1+bit2+retenu==2:
            retenu=1
            somme=0

        elif bit1+bit2+retenu==1:
            retenu=0
            somme=1
        else:
            retenu=0
            somme=0
##        print("retenu=",retenu)
##        print("somme=",somme)
        resultat=str(somme)+resultat

    return resultat


