def nhap():
    fo = open('GANE.inp' , 'r')
    n = fo.readline().split()
    k = fo.readline().split()
    return k
k = nhap()
max = 0
n = len(k)

# Dùng đệ quy nhị phân để giải

def xuat():
    tong = 0
    ktr = 0
    global max
    for i in range(n):
        if x[i] == '0': # Nếu X[i] đc xử lí trong hàm xuli() = 0 thì 
            if ktr > 2: # Check biến ktr có vượt quá 2 hay ko 
                return # nếu có thì return
            else:
                ktr += 1 # Nếu chưa thì mình cho cộng 
                tong += int(k[i]) # Cộng vô cho biến tổng ngay chô k[i] sao cho x[i] = 0
                if tong > max:
                    max = tong # kiểm tra số nào lớn hơn thì lấy
        else:
            ktr = 0
def xuli(i):
    # Phần hàm đệ quy nhị phân
    for j in range(2):
        x[i] = str(j)
        if i == ( n -1 ):
            xuat()
        else:
            xuli(i+1)
x = []
for i in range(n):
    x.append('')
xuli(0)
print(max)
def xuat():
    fi = open('GAME.out','w')
    fi.write(str(max))
xuat()
    