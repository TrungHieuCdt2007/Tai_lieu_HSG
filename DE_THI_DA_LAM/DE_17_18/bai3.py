def nhap():
    fi = open('HV.inp','r')
    n,k = list(map(int, fi.readline().split()))
    B = []
    N = []
    for i in range(k):
        tam = list(map(int,fi.readline().split()))
        B.append(tam)
    for i in range(n):
        tam = list(map(int,fi.readline().split()))
        N.append(tam)
    return n,k,B,N
n,k,B,N = nhap()

def xuli():
    hang = len(B)
    cot = len(B[0])
    dem = 0
    ti = 0
    h = 0
    for i in range(n):
        h = 0 
        ti = 0
        for j in range(n):
            if N[i][j] == B[0][ti]:
                ti+=1 
                if ti == hang :
                    ti = 0
                    dem += 1
                if dem == cot:
                    return 1
            else:
                h += 1 
                if h == len(N):
                    dem = 0
                return 0
                    
x = xuli()
print(x)
def xuat():
    fo = open('HV.out', 'w')
    fo.write(f'{x}')
xuat()