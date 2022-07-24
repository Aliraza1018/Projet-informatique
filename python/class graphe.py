class Graphe:
    def __init__(self):
        self.Liste={}

    def addArete(self,u,v):
        if v not in self.Liste:
            #acompléter
        if u not in self.Liste:
            #acompléter




        self.Liste[u].append(v)

    def affiche(self,M, sommets):
        for i in range(#acompléter):
            for j in range(i,len(M)):
                if M[i][j]==1:
                    self.addArete(#acompléter,#acompléter)
        for key, value in self.Liste.items():
            print(key, ":", value)


M=[
    [0,1,1,0,1,0],
    [1,0,1,1,0,1],
    [1,0,0,1,1,1],
    [0,1,1,0,1,0],
    [1,0,1,1,0,1],
    [0,1,1,0,1,0]

    ]
G=Graphe()
sommets=['A','B','C','D','E','F']
G.affiche(M,sommets)