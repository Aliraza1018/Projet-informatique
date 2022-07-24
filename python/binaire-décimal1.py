def bindec(nb):

    i=1

    ndec2=0

    nb2=0

    chaine=str(nb)

    for k in range(len(chaine)-1,-1,-1):

##        print(chaine[k])

##    while nb>0:

        ndec=int(chaine[k])*i

        ndec2=ndec+ndec2

##        nb=nb2

        i=i*2

    print(ndec2)
