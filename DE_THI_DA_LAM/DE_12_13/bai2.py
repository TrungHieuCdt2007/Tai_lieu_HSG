def nhap():
    fi = open('BAOTRI.inp', 'r')
    n,k = list(map(int,fi.readline().split()))
    N = list(map(int,fi.readline().split()))
    a,b = list(map(int,fi.readline().split()))
    return n,k,N,a,b
n,k,N,a,b = nhap()
print(n,k,N,a,b)
def xuli():
    A = []
    for i in range(a,b+1):
        dem = 0
        for j in N:
            if i % j == 0:
                dem += 1
        if dem >= k:
            A.append(i)
    return A
x = xuli()
def xuat():
    fo = open('BAOTRI.out', 'w')
    fo.write(f'{len(x)}')
    fo.close()
xuat()