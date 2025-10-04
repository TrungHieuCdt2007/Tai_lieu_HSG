def Nhap():
    fi = open("messages.inp", 'r')
    n, m = map(int, fi.readline().split())
    C =[]
    for i in range(1, n + 1):
       tam = list(map(int, fi.readline().split()))
       C.append(tam)
    for i in range(len(C)): C[i].insert(0,0)
    C.insert(0,[0]*n)
    print(C)
    return n,m,C
n,m,C = Nhap()

SoGoi = [[0] * (n+2) for _ in range(m+2)]  # SoGoi[i][j]-so goi tin chuyen theo kenh j
p = [0] * (m + 2)

def XuLi():
    global p, n, m,  SoGoi # Khởi tạo
    SoGoi = [[0] * (5+2) for _ in range(4+2)] # Khởi tạo
    p[0] = 0 # Khởi tạo
    for i in range(1, n + 1): # chi phí chuyển i gói in trên kênh đầu với chi phi C[i][1]
        p[i] = C[i][1]
        SoGoi[i][1] = i
    # Tính chi phí chuyển i gói tin kênh j đầu tiên
    for j in range(2, m): 
        for i in range(n, 0, -1):
            for k in range(1, i + 1):
                if p[i] > p[i - k] + C[k][j]: # Công thức truy hồi
                    p[i] = p[i - k] + C[k][j]
                    SoGoi[i][j] = k
    # tính chi phí chuyển i gói tin ở kênh cuối cùng
    for k in range(1, n + 1): 
        if p[n] > p[n - k] + C[k][m]:
            p[n] = p[n - k] + C[k][m]
            SoGoi[n][m] = k
XuLi()   
def Xuat():
    fo = open("messages.out",'w')
    fo.write(str(p[n]))  # chi phi min
    i = n
    # thực hiện truy vết
    for j in range(m, 0, -1):
        p[j] = SoGoi[i][j]
        i = i - SoGoi[i][j]  # so goi con lai
    for i in range(1, m + 1):
        fo.write(f"\n{p[i]}")
Xuat()

print(p)