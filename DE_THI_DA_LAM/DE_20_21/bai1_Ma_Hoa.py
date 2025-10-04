from time import perf_counter
bd = perf_counter() 
def nhap():
    fi = open('MAHOA.inp','r')
    n = fi.readline()
    N = []
    for i in range(int(n)):
        k = fi.readline().split(' '+'\n')
        for i in k:
            N.append(i)
    for i in range(len(N)):
        N[i] = [char for char in N[i]]
        for j in range(len(N[i])):
            N[i][j] = N[i][j].lower()   
    return N
N = nhap()
def xuli():
    K = []
    L = []
    for i in range(len(N)):
        K.append([])
    for i in range(len(N)):
        k = 0
        for j in N[i]:
            if j != ' ' and j != '\n' and j not in K[i]:
                K[i].append(j)
        for j in K[i]:
            if j in N[i]:
                if N[i].count(j) >= 2:
                    k += N[i].count(j)
        L.append(k)
    return K,L
K,L = xuli()
print(K,L)
def xuat():
    fo = open('MAHOA.out', 'w')
    for i in range(len(K)):
        fo.write(f'{L[i]} ')
        fo.write('')
        for j in K[i]:
            fo.write(f'{j}')
        fo.write('\n')
xuat()
kt = perf_counter()
print(kt - bd)

