def nhap():
    fi = open('SOSATSAU.inp')
    n = list(map(int,fi.readline().split()))
    a = fi.readline()
    A = []
    for i in a:
        A.append(int(i))
    return n[0],A
n,A = nhap()

def xuli():
    global A
    i = n - 2
    while i > -1:
        if A[i] < A[i+1]:
            break
        i-=1
    else: return 0
    j = n -1
    while j > -1 :
        if A[j] > A[i] :
            tam1 = A[j]
            A[j] = A[i]
            A[i] = tam1
            break
        j -= 1
    j = n - 1
    i = i + 1
    while j > i:
        x = A[j]
        A[j] = A[i]
        A[i] = x
        j -= 1
        i += 1
x = xuli()
print(x)
print(A)
def xuat():
    fo = open('SOSATSAU.out', 'w')
    if x != 0:
        for i in A:
            fo.write(f'{i}')
    else:
        fo.write(f'{0}')
xuat()