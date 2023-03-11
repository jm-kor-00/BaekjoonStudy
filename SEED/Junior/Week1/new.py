a,b = map(int,input().split())
c = [31,28,31,30,31,30,31,31,30,31,30,31]
d = 0
for i in range(a-1):
    d = d+c[i]
d = d+b
print(d)