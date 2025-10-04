def nhap():
    N = []
    fi = open('chiamang.inp', 'r')
    a = fi.readline().split()
    N = fi.readline().split()
    N = list(map(int, N)) 
    return N
N = nhap()
def xuli(N):
    max = 0
    k = 0
    # k = 0
    # z = 0
    # c = int(a[0])
    # for i in range(c):
    #     k += int(N[i])
    # if k % 2 == 0:
    #     for l in range(len(N)):
    #         z += int(N[l])
    #         if z == k // 2: 
    #             return l
    #  Cách 2
    for j in N:
        max += j # tính tổng các giá trị của mảng
    if max % 2 == 0: 
        for i in range(len(N)):
            k += N[i]
            if k == max // 2: # Tính n giá trị cho đến khi mà bằng 1/2 giá trị của mảng
                return i
l = xuli(N)

def xuat():
    fo = open('chiamang.out', 'w')
    if l == None :
        fo.write('0')
    else :
        fo.write(str(l))
xuat() 
    