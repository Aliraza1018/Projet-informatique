def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return fact(n-1)*n

def factorielle(n):
    p=1
    for k in range(1,n+1):
        p=p*k
    return p

def fibo(n):
    a=1
    b=1
    for k in range(n):
        c=a+b
        a=b
        b=c
    return c

def pgcd(a,b):
    if a<b:
        return pgcd(b,a)
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)


def C(n,p):
    if p==0 or p==n:
        return 1
    else:
        return (C(n-1,p)+C(n-1,p-1))