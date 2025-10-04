
k = [9 ,3 ,5, 4]
n = 4
max = 0
def xuat():
    global max
    ktr = 0
    tong = 0
    for i in range(n):
        if X[i] == 0:
            if ktr > 2:
                return
            else:
                ktr += 1
                tong += k[i]
            if tong > max:
                max = tong
        else:
            ktr = 0
    # print()

def xuli(i):
    for j in range(2):
        X[i] = int(j)
        if i == ( n - 1):
            xuat()
        else:
            xuli(i+1)

X = ['']*n
xuli(0)
print(max)