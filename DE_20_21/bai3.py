def nhap():
    fi = open("MUSIC.txt", "r")
    l,k = list(map(int,fi.readline().split()))
    ti = list(map(int,fi.readline().split()))
    zi = list(map(int,fi.readline().split()))
    return k,ti,zi
k,ti,zi = nhap()
def xuli():
    tam = 0
    tam1 = 0
    i1 = 0
    max = []
    for i in range(len(ti)):
        for o in range(i+1,len(ti)):
            if ti[i] > ti[o]:
                tam = ti[i] ; ti[i] = ti[o] ; ti[o] = tam
                tam1 = zi[i] ; zi[i] = zi[o] ; zi[o] = tam1
    print(ti,zi)
    max = 0
    for i in range(len(ti)):
        t = 0
        sum = 0
        for j in range(i, len(ti)):
            if ti[j] - t >= k:
                t += k
                sum +=zi[j]
        if sum > max :
            max = sum
    return max
max = xuli()

def xuat():
    fo = open('MUSIC.out', 'w')
    fo.write(f'{max}')
xuat()