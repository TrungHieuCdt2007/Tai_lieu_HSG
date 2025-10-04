from time import perf_counter
def nhap():
    fi = open('coins.inp', 'r')
    n,k = list(map(int,fi.readline().split()))
    M = []
    L = []
    for i in range(n):
        m,l = list(map(int,fi.readline().split()))
        M.append(m)
        L.append(l)
    return n,k,M,L
n,k,M,L = nhap()
print(n,k)
def xuli():
    j = k // 2
    sum = 0
    TT = []; KQ = []; SL = []
    i = len(M)-1
    
    if k % 2 == 0:  
        while i > - 1 :
            while sum < j and M[i] < j and j - sum > M[i] and L[i] != 0 : 
                    sum += M[i]
                    L[i] = L[i] - 2
                    TT.append(M[i])
            i -= 1  
        if j - sum == 1: TT.append(1)
        TT = TT * 2
        for i in TT:
            if i not in KQ: KQ.append(i) ; SL.append(TT.count(i))
        return KQ,SL
    return 0,0 
KQ,SL = xuli()
def xuat():
    fo = open('coins.out', 'w')
    if KQ:
        for i in range(len(KQ)-1,-1,-1):
            fo.write(f'{KQ[i]} {SL[i]}' + str('\n')) 
    else: fo.write(str(0))
bd = perf_counter()
xuat()
kt = perf_counter()
print(kt-bd)