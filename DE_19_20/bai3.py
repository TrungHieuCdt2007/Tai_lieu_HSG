def nhap():
    fi = open('wifi.inp', 'r')
    n,k = list(map(int,fi.readline().split()))
    N = list(map(int,fi.readline().split()))
    K = list(map(int,fi.readline().split()))
    return n,k,N,K
n,k,N,K = nhap()
print(n,k,N,K)

def xuli():
    max = 0
    for i in range(1,n+1):
        sum = K[0]
        x = 0
        if i != n :
            for j in range(i,n - 1):
                if N[j] - N[x] >= k:
                    x = j
                    sum += K[j]
            sum += K[n-1]
        if sum > max : max = sum
    print(max)
xuli()