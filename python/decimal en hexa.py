nombre=int(input("un nombre entier: "))

nombre_decimal=""

if nombre==0:

    print("Le nombre 0 en base 16.")

else:

    while nombre>0:

        quotient=nombre//16

        reste=nombre%16



        nombre=quotient

        if reste==10:
            reste=('A')
        if reste==11:
            reste=('B')
        if reste==12:
            reste=('C')
        if reste==13:
            reste=('D')
        if reste==14:
            reste=('E')
        if reste==15:
            reste=('F')
        nombre_decimal=str(reste) + nombre_decimal

print("Le nombre hexa est" ,nombre_decimal,)
