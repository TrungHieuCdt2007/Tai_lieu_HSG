def nhap():
    fi = open('DAYCON.inp', 'r')
    n = list(map(int,fi.readline().split()))
    N = list(map(int,fi.readline().split()))
    return n[0],N
n,N = nhap()

def xuli():
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(n):
        for j in range(i,n):
            if N[i] > N[j]:
                dp[j] = max(dp[j],dp[i]+1)
    return max(dp)
dp = xuli()

def xuat():
    fo = open('DAYCON.out','w')
    fo.write(f'{dp}')
xuat()