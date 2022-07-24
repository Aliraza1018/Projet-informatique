a=0
n=int(input("nombre"))
while n != 1:
    if n % 2==0:
        n=n//2
        a+=1
        print(n,"nombre d'etape",a)
    elif n % 2 ==1:
        n= n*3+1
        a+=1
        print(n,"nombre d'etape",a)
print(n)
