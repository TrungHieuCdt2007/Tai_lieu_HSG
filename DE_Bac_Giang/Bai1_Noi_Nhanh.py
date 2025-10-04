def nhap():
    fi = open('NOINHANH.inp', 'r')
    n = list(map(int,fi.readline().split()))
    return n
n = nhap()

def xuat(x):
    fo = open('NOINHANH.out', 'w')
    for i in x:
        fo.write(f'{i} ')
    fo.close()

def xuli():
    tong = 0
    A = []
    for i in range(len(n)):
        tong += n[i]
        A.append(tong)
        xuat(A)
xuli()
