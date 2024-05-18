from itertools import permutations

N,M = map(int,input().split())
res = list(permutations(range(1,N+1),M))
res.sort()
for el in res : 
    for c in el:
        print(c,end=" ")
    print()