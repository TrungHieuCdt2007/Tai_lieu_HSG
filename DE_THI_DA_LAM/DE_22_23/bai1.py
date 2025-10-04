
def nhap():
    fi = open('chuoi.inp', 'r')
    K = fi.read().split()
    fi.close()
    return K
K = nhap()
Kq = []
A =[]
B =[]
C = []
Dem = []
So = 0
def xuli():
    for i in range(0,len(K)): # sắp xếp các phần tử ( bên trái và bên phải )
        if i % 2 == 0:
            A.append(K[i])
    
        else:
            B.append(K[i])
    
    for j in reversed(range(0,len(B))):
        C.append(B[j]) # đảo nược phần tử bên trái
        
    for o in range(len(C)):
        A.append(C[o]) # cho các phần tử bên trái vào list A
    for t in A:
        if t not in Dem :
            Dem.append(t) # tính các số màu
    return Dem,A
Dem,A = xuli()

print(Dem,A)

def xuat(Dem,A):
    fo = open('CHUOI.OUT', 'w')
    for i in A:
        fo.write(i + ' ' )
    fo.write(str('\n' + str(len(Dem))))

xuat(Dem,A)

