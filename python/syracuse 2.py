nbt=0
a=0

##n=int(input("nombre"))
for n in range(1,21):
    nt=0
    nv=n

    print(nv)

    while n != 1:
        if n % 2==0:
            n=n//2
##         nt+=1
##         print(n,"nombre d'etape",nbt)
        elif n % 2 ==1:
            n= n*3+1

        nt=nt+1
        if n > a:
            print(n)
            a=n
            b=nv


##        print(n,"nombre d'etape",nbt)
    print(nt)
    if nt>nbt:
        nbt=nt
        ns=nv
##    if a > n:
print(nbt,ns,a,b)
