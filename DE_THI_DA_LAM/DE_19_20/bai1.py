def nhap():
    fi = open('SOK.inp', 'r')
    n,k = list(map(int,fi.readline().split()))
    fi.close()
    return n,k
n,k = nhap()

def xuli():
    A = []
    B = []
    for i in range(n):
        if i % 2 != 0: A.append(i)
        else: B.append(i)
    for i in B: A.append(i)
    return A
A = xuli()

def xuat():
    fo = open('SOK.out', 'w')
    fo.write(f'{A[k-1]}')
    fo.close()
xuat()