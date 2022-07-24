nombre=int(input("un nombre entier: "))

nombre_decimal=0

if nombre==0:

    print("Le nombre 0 en base.")


else:
    n=1
    while nombre>0:


        quotient=nombre//10


        reste=nombre%10




        nombre=quotient

        if reste==1:
            reste=1*n

        n=n*2

        nombre_decimal=reste + nombre_decimal

print("Le nombre hexa est" ,nombre_decimal,)
