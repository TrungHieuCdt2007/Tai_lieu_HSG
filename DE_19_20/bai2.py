def nhap():
    fi = open('MAHOA.inp', 'r')
    n = int(fi.readline())
    p = fi.readline().split()
    p = list(map(int, p[0]))
    K = fi.readline().split()
    K = list(map(str,K[0]))
    fi.close()
    return n,p,K
n,p,K = nhap()

def xuli():
    A = []
    B = []
    D = []
    C = []
    if len(K) % 2 != 0:
        K.append(' ')
    A = K[:len(K)//2]
    B = K[(len(K)//2):]
    for i in p  :
        i = i - 1
        C.append(A[i])
        D.append(B[i])
    for i in D: C.append(i)
    return C
C = xuli()     

def xuat():
    fo = open('MAHOA.out', 'w')
    for i in C :
        fo.write(f'{i}')   
    fo.close()
xuat()