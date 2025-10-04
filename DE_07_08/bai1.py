def nhap():
    fi = open('LINE.inp')
    a,b = list(map(int,fi.readline().split()))
    n = int(fi.readline())
    AB = []
    for i in range(n):
        tam = list(map(int,fi.readline().split()))
        AB.append(tam)
    return a,b,n,AB
a,b,n,AB = nhap()

def xuli():
    CD = []
    tam = []
    KQ =[]
    ktr = 0
    for i in range(a,b):
        tam = []
        tam.append(i)
        tam.append(i+1)
        CD.append(tam)
    for i in range(len(CD)):
        ktr = 0
        for j in range(len(AB)):
            if CD[i][0] != AB[j][0] and CD[i][0] not in KQ:
                ktr += 1
            if ktr == n:
                ktr = 0
                KQ.append(CD[i])
    if len(KQ) == 0:
        return '*'
    return KQ
x = xuli()
def xuat():
    fo = open('LINE.OUT', 'w')
    for i in range(len(x)):
        for j in range(len(x[i])):
            fo.write(f'{x[i][j]} ')
        fo.write(str('\n'))
    
xuat()