def nhap():
    fi = open('atm.txt', 'r')
    N = fi.readline().split()
    n = int(N[0])
    m = int(N[1])
    l = fi.readline().split()
    l = l = [int(x) for x in l]
    return n,m,l
n,m,l = nhap()
print(n,m,l)
x = [0] * (n+1)
print
sum = 0
def xuli1():
    global sum
    fo = open('atm.out' , 'w')
    if sum == m:
        for i in range(0,n):
            if x[i] == 1 :
               print(l[i])
               
        exit()

def xuli2(i):
    global sum
    if sum > m :
        return
    for j in range(2):
        x[i] = j
        sum = sum + x[i]*l[i - 1]
        print(sum)
        if i == n:
            xuli1()
        else :
            xuli2(i+1)
        sum =sum - x[i]*l[i - 1]
xuli2(1)
print(sum)