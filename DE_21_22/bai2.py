def nhap():
    D = []
    fi = open('TDOAN.inp' , 'r')
    n1 = fi.readline().split()
    n2 = fi.read().split()
    o,k = list(map(int,n1))
    n = list(map(int,n2))
    return n,k

n,k = nhap()

def xuli():
    K = []
    X = []
    # Dùng thuật toán tham lam để quyật đoạn
    for i in range(len(n)):
        t = 0 # khởi tạo lại các biến thi duyệt lần nx
        D  = []
        for j in range(i,len(n)): # duyệt từ i đến n 
            t += n[j] # Tổng sẽ được cộng vào
            D.append(n[j]) # D sẽ thêm giá trị n[j]
            if t == k : # nếu t = k thì 
                K.append(D) # thêm vào bảng K
                X.append(i + 1) # thêm i + 1 vào Mảng vị trị
                t = 0 # reset các biến
                D = []
    for i in range(len(K)): # tìm mảng có số phần tử nhỏ nhất và vị trị của phần tử đầu cảu mảng
        if len(K[i]) < len(K[i - 1]) :
            max = len(K[i])
            vx = X[i]
    return max , vx
max , vx = xuli()

def xuat():
    fo = open("TDOAN.out", "w")
    fo.write(f'{vx} {max}')
xuat()
    