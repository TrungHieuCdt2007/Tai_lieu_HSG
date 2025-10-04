def nhap():
    fi = open('CHUOI08.inp')
    S = []
    n,m,x = fi.readline().split(); n = int(n) ; m = int(m)
    s = fi.readline()
    for i in s :
        S.append(i)
    return n,m,x,S
n,m,x,S = nhap()

def xuat(S):
    fo = open('CHUOI08.out', 'w')
    fo.write(f'{len(S)}' + str('\n'))
    for i in S:
        fo.write(f'{i}')

def xuli():
    i = 0
    while len(S) < m :
        if S[i] != str(x):
            S.append(S[i])
        i+=1
    xuat(S)
xuli()
