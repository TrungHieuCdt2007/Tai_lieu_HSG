def nhap():
    fi = open('CARDS.inp','r')
    K =[]
    S1 = []
    S2= []
    n,x = list(map(int,fi.readline().split()))
    for i in range(x):
        s1,s2 = list(map(int,fi.readline().split()))
        S1.append(s1)
        S2.append(s2)
    return n,x,K,S1,S2
n,x,K,S1,S2 = nhap()

def xuli():
    N=[]
    dem = 0
    for i in range(1,n+1):
        N.append(i)
    N.append(0)
    while i < len(S1):
        if S2[i] == n:
            tam = N[S1[i]-1]
            N[S1[i]-1] = N[n]
            N[n] = tam
           
        else:
            tam = N[S1[i]-1]
            N[S1[i]-1] = N[S2[i]-1]
            N[S2[i]-1] = tam
        i+=1
    i = 0 ; j = 1
    while i < n and j < n :
        if N[j] - N[i] != 1:
            for k in range(j,n):
                if N[k] - N[i] == 1:
                    tam = N[k]
                    N[k] = N[j]
                    N[j] = tam
                    dem +=1
                    break
        i +=1 ; j +=1
    return dem
dem = xuli()
def xuat():
    fo = open('CARDS.out', 'w')
    fo.write(f'{dem}')
xuat()
    