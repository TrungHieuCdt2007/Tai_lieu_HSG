def nhap():
    fi = open('SNT.inp')
    N = list(map(int,fi.read().split()))
    return N
N = nhap()
print(N)
X = []

def ktra(a,b):
    Ua = []
    Ub = []
    global X
    for i in range(2,(a//2)+1):
        while a % i == 0 :
          Ua.append(i)
          a = a // i  
    Ua = set(Ua)
    for i in range(2,(b//2)+1):
        while b % i == 0:
            Ub.append(i)
            b = b // i
    Ub = set(Ub)
    if Ua == Ub:
        X.append(1)
    else:
        X.append(0)
    
def xuli():
    for i in range(0,len(N),2):
        ktra(N[i],N[i+1])
xuli()
print(X)
def xuat():
    fo = open('SNT.out','w')
    for a in X:
        fo.write(f'{a}' + str('\n'))
xuat()
