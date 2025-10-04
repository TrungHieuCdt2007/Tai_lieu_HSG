fi = open('vd1.inp','r')

fo = open('vd1.out','w')

n = fi.readline().split()
r,c = map(int,n)

l = []
for i in range(r):
    tam = fi.readline().split()
    tam = list(map(int,tam))
    tam.insert(0,float('-inf'))
    tam.append(float('-inf'))
    l.append(tam)
    
t = [float('-inf')]* ( r+2)
l.insert(0,t)
l.append(t)

count = 0
A = []
for i in range(1,r +1):
    for j in range(1,c+1):
        if max(l[i][j],l[i-1][j],l[i+1][j],l[i][j-1],l[i][j+1]) == l[i][j]:
            count + 1 
            print(l[i][j])
            A.append(l[i][j])
print(A)
for i in A:
    fo.write(f'{i} ')