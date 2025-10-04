def nhap():
    fi = open('SSNT.inp' , 'r')
    N = int(fi.readline())
    n = 10 ** N
    return n,N
n,N = nhap()
print(n)
def KtrSNT(x):
    if x <= 3 : return x > 1
    if x % 2 == 0 or x % 3 == 0 : return False
    for i in range(5,int(x**(1/2)+1),6):
        if x % i == 0 or x % (i+2) == 0 : return False
    return True

def KtrSSNT(y):
    while y > 0:
        if KtrSNT(y) == False : return False 
        y = y // 10
    return True

def xuli():
    kq = []
    for i in range(n):
        if KtrSSNT(i) and i > 10 ** (N-1):
            kq.append(i)
            
    print(kq)       
            
xuli()