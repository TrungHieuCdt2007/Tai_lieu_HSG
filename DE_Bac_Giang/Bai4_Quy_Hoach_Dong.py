def nhap():
    fi = open('TichBaSo.inp', 'r')
    n = int(fi.read())
    return n
n = nhap()

def xuli():
    # Cách tạo khi tính tổng bước 
    A = [[1]*n]*n # Tạo list 2 chiều
    
    # Cách tạo khi tính tổng bước ở vị trí cụ thể nào đó 
    # A = []
    # for i in range(n):
    #     A.append([])
    # for j in range(len(A)):
    #     for i in range(n):
    #         A[j].append(1)
    
    k = n - 1
    for i in range(k - 1,-1,-1):
        for j in range(k - 1,-1,-1):
            A[i][j] = A[i][j+1] + A[i+1][j] # Công thức truy hồi ( QUy Hoạch Động) , Vị trí (X,Y) = Tổng hai vị trí (X+1,Y) + (X,Y+1)
            print(i,j)                      #
    return A[0][0]                          #    20 10 4 1  
A = xuli()                                  #     10 6 3 1
                                            #      4 3 2 1 
                                            #      1 1 1 1 
def xuat():
    fo = open('TichBaSo.out', 'w')
    fo.write(f'{A}')
xuat()
print(A)