def nhap():
    fi = open('DIV.inp')
    n,k = list(map(int,fi.readline().split()))
    N = list(map(int,fi.readline().split()))
    return n,k,N
n,k,N = nhap()
print(N)
x = [0] * (n)
sum = N[0]; ok = False

def xuli(i):# Xử lí đệ quy nhị phân
    global sum,ok
    for j in range(2):
        x[i] = j
        if x[i] == 1 : # khi bằng 1 thì sẽ cho phép tính cộng nếu ko thì trừ
            sum += N[i]
        else:
            sum -= N[i]
        if i == (n-1): # nếu i bằn n thì check
            if sum % k == 0: # nếu sum của mình chia hết cho k thì ok
                 ok = True
        else: xuli(i+1) # nếu i chưa bằng n thì gọi hàm lần nx 
        if ok: 
            return
        
        if x[i] == 1: # Phần này ngc lại phần trên, tính phép trừ
            sum -= N[i]
        else:
            sum += N[i]
xuli(1)

def xuat():
    fo = open('DIV.out','w')
    fo.write(f'{ok}')
xuat()
        
        
