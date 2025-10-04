from time import perf_counter
def nhap():
    fi = open('NGTO.inp', 'r')
    n = fi.read().split()
    n = list(map(int, n))
    return n
n = nhap()

    
def xuli():
    dem = 1
    C = []
    A = []
    
    for i in n:
        dem = 2
        c = 2
        B = []
        sb = ""
        for j in range(2, ( i // 2 ) + 1 ):
            if i % j == 0:
                dem +=1
        A.append(dem)
       
        while i > 1:
            if i % c ==0:
                i = i / c
                B.append(c)
            else: c +=1
        if len(B) == 0:
            B.append(i)
            
        size = len(B)
        for i in range(0, size - 1):
            sb = sb + str(B[i]) + " x "
        sb = sb + str(B[size-1])
        C.append(sb)
    return A,C
A,C = xuli()


def xuat(A,C):
    fo = open('NGTO.out', 'w')
    for i in range(0, len(A)):
        fo.write(f'{A[i]} ' + f'{C[i]}' + str('\n') )
bd = perf_counter()
xuat(A,C)        
kt = perf_counter()
print(kt-bd)