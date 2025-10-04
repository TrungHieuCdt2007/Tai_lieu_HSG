def nhap():
    N = []
    fo = open('dayso.inp' , 'r')
    n = fo.readline().split()
    return n
n = nhap() 

def xuli(n):
    K = []
    H = [n[0],n[1],n[2]]
    Kq= []
    t = 1
    for i in range(3,len(n)):
        for j in range(t,i+1):
            K.append(n[j])
        t += 1
        if K[0] < K[1] < K[2] :
            if K[0] > H[0] or K[1] > H[1] or K[2] > H[2]:
                Kq = K
                H = K
                print(1)
                K = []
            else: 
                Kq = H
                H = H    
                print(2) 
                K = []
        else:
            K= []
    return Kq
Kq = xuli(n)

def xuat(Kq):
    fi = open('dayso.out', 'w')
    for i in Kq:
        fi.write(str(i)  + ' ')
xuat(Kq)
    
