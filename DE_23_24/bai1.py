def nhap():
    fi = open("GB.inp", 'r')
    n = list(map(int,fi.readline().split()))
    N = list(map(int,fi.read().split()))
    return n[0],N
n,N = nhap()

def xuli():
    Kq = [[0,0]] * (n+1)
    k = 0
    for o in N:
        k+=1
        dp = [True] * o
        Snt = []
        for i in range(2,o):
            for j in range(i*i,o,i):
                dp[j] = False
        for i in range(2,o):
            if dp[i]:
                Snt.append(i)
        for i in range(len(Snt)):
            dem = []
            for j in range(i,len(Snt)):
                if Snt[i] + Snt[j] == o :
                    dem.append(Snt[i])
                    dem.append(Snt[j])
                    Kq[k] = dem
    return Kq
Kq = xuli()
print(Kq[3])
def xuat():
    fo = open('GB.out','w')
    for i in range(1,len(Kq)):
        for j in range(len(Kq[i])):
            if Kq[i][j] != 0:
                fo.write(f'{Kq[i][j]} ')
            else:
                fo.write(str('khong'))
                break
        fo.write(str('\n'))
xuat()