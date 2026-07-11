p,q,r = map(int,input().split())
AtoB = {}
BtoC={}

for _ in range(p):
    i,j = map(int,input().split())
    AtoB[i]=j
    
for _ in range(q):
    j2, k = map(int,input().split())
    BtoC[j2] = k 

for x in range(1, p+1):  
    print(x, BtoC[AtoB[x]])