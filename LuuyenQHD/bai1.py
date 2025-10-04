def nhap():
    fi = open('bai1.inp')
    n,w = list(map(int,fi.readline().split()))
    W = [0]
    K = [0]
    for i in range(n):
        wi,ki = list(map(int,fi.readline().split()))
        W.append(wi)
        K.append(ki)
    return n,w,W,K
n,w,W,K = nhap()

def xuli():
    dp =[ [0] * (w+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            dp[i][j] = dp[i-1][j]
            if j >= W[i]:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-W[i]] + K[i] )
    print(dp)
    i = n ; j = w ; S= []
    while i :
        if dp[i][j] != dp[i-1][j]:
            S.append(i)
            j -= W[i]
        i -=1
    print(S)
xuli()