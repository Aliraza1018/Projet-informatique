
##nombre=int(input("un nombre entier: "))
def conv(nombre):
    nombre_decimal=""

    if nombre==0:

        print("Le nombre 0 en base 2.")

    else:

        while nombre>0:

            quotient=nombre//2

            reste=nombre%2

            nombre_decimal=str(reste) + nombre_decimal

            nombre=quotient

    print("Le nombre binaire est" ,nombre_decimal,)
