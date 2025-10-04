def nhap():
    fi = open('DULICHDN.inp')
    n = list(map(int,fi.readline().split()))
    x = list(map(int,fi.readline().split()))
    y = list(map(int,fi.readline().split()))
    return n[0],x,y
n,x,y = nhap()

def xuli():
    t = 1
    for i in range(n):
        for j in range(i,n):
            if x[i] > x[j] and y[i] < y[j]:
                t+=1
    return t
t = xuli()
print(t)
def xuat():
    fo = open('DULICHDN.out', 'w')
    fo.write(f'{t}')
xuat()
    