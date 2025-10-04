def nhap():
    fi = open('dayso.inp') 
    n = fi.readline().split()
    return n 
n = nhap()

def xuli(n):
    a = 0
    K =[]
    Kq = []
    M = [int(n[0]),int(n[1])]
    for b in range(2,len(n)+1):
        for i in range(a,b):
            K.append(int(n[i]))
        a += 1
        if sum(K) > sum(M):
            Kq = K 
            M = K
            K = []
        else:
            Kq = M 
            M = M
            K= []    
            
    return Kq
Kq = xuli(n)

def xuat(Kq):
    fo = open('Dayso.out' , 'w' )
    for i in Kq:
        fo.write(str(i) + ' ' )
xuat(Kq)