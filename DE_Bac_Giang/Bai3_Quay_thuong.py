def xuat(n,max):
    fo = open('THUONG.out', 'w')
    for i in n:
        fo.write(f'{i} ')
    fo.write('\n'+ f'{max}')

def xuli(n,k):
    ktr = 0
    tong = 0
    p = 0
    for i in k :
        if i in n :
            n.remove(i)
    for i in n:
        ktr = n.count(i)
        if ktr > tong :
            tong = ktr
            p = i
    max = tong * p
    xuat(n,max)

def nhap():
    fi = open('THUONG.INP', 'r')
    n = fi.readline().split()
    n = list(map(int, n))
    k = fi.readline().split()
    k = list(map(int,k))
    xuli(n,k)
nhap()







