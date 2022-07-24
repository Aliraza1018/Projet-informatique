
##score=int(input("Votre Score"))
nc=0
totale=0
score=0
while (nc != 2 and score!=10):
    score=int(input("Votre Score"))
    if nc==0 and score==10:
        print("STRIKE!!!")
    elif nc==0 and score !=10:
        nc=1
        totale=score
    elif nc==1 and score+totale ==10:
        print("SPARE")



