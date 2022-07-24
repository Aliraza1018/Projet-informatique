def bindec(nb):
    chaine= str(nb)
##    print(type(chaine))
    for i in range(len(chaine)-1,-1,-1):
        print(chaine[i])

nombre_decimal =0
n=1
while chaine[i]>0:


        quotient=chaine[i]//10


        reste=chaine[i]%10




        chaine[i]=quotient

        if reste==1:
            reste=1*n

        n=n*2

        nombre_decimal=reste + nombre_decimal

print("Le nombre hexa est" ,nombre_decimal,)
