def nhap():
    fi = open('XDS.inp','r')
    n,m = list(map(int,fi.readline().split()))
    A = list(map(int,fi.readline().split()))
    B = list(map(int,fi.readline().split()))
    return n,m,A,B
n,m,A,B = nhap()
print(len(A))
def xuli():
    sum = []
    dem = 0
    for i in range(len(A)):
        for j in range(i,len(A)):
            sum.append(A[i]+A[j])
    for i in sum:
        if i in B:
             dem +=1
    return dem      
x = xuli()

def xuat():
    fo = open('XDS.out', 'w')
    fo.write(f'{x}')
xuat()