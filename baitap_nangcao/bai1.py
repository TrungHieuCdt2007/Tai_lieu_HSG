def nhap():
    fi = open('can.txt', 'r')
    N = fi.readline().split()
    n = int(N[0])
    m = int(N[1])
    l = fi.readline().split()
    l = l = [int(x) for x in l]
    return n,m,l
n,m,l = nhap()
x = [0] * (n+1)
sum = 0

def xuli1():
    global sum
    fo = open('can.out' , 'w')
    if sum == m:
        for i in range(1,n+1):
            if x[i] == 1 :
               print(i)

def xuli2(i):
    global sum
    if sum > m :
        return
    for j in range(2):
        x[i] = j
        sum = sum + x[i]*l[i - 1]
        if i == n:
            xuli1()
        else :
            xuli2(i+1)
        sum =sum - x[i]*l[i - 1]
xuli2(1)