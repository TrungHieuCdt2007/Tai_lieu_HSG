def nhap():
    fi = open('CAYKHE.inp' , 'r')
    n,m = list(map(int,fi.readline().split()))
    W = [0]
    V = [0]
    for i in range(n):
        wi,vi = list(map(int,fi.readline().split()))
        W.append(wi); V.append(vi)
    return n,m,W,V    
n,m,W,V = nhap()
def xuli():
    kq = [[0] * ( m + 1) for i in range(n+1) ]
    for i in range(1,n+1):
        for j in range(1,m+1):
            kq[i][j] = kq[i-1][j]
            if j >= W[i]:
                kq[i][j] = max(kq[i-1][j],kq[i-1][j-W[i]] + V[i])
    print(kq)
    i = n ; j = m ; S = []
    while i:
        if kq[i][j] != kq[i-1][j]:
            S.append(i)
            j = j - W[i]
        i -=1
    print(S)
    return S, kq[n][m]
S , kq = xuli()
def xuat():
    fo = open('CAYKHE.out', 'w')
    fo.write(f'{kq}' + str('\n'))
    for i in range(len(S)-1,-1,-1):
        fo.write(f'{S[i]} ')
    fo.close()
xuat()
    