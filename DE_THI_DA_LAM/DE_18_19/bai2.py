def nhap():
    fi = open('GAMES1.inp', 'r')
    n,m = list(map(int,fi.readline().split()))
    A = [0]
    B = [0]
    for i in range(n):
        a,b = list(map(int,fi.readline().split()))
        A.append(a)
        B.append(b)
    return n,m,A,B
n,m,A,B = nhap()

def xuli():
    sum = 0
    kq = [ [0] * (m+1) for i in range(n+1) ]
    for i in range(1,n+1):
        for j in range(1,m+1):
            kq[i][j] = kq[i-1][j]
            if j >= A[i]:
                kq[i][j] = max(kq[i-1][j],kq[i-1][j-A[i]] + B[i])
                sum += kq[i][j]
    print(kq)
    return sum
sum = xuli()

def xuat():
    fo = open('GAMES1.out', 'w')
    fo.write(f'{sum}')
    fo.close()
xuat()