def nhap():
    fi = open('CHESS.inp' , 'r')    
    n,m = list(map(int,fi.readline().split()))
    B = []
    for i in range(n):
        tam = fi.readline().split()
        for i in tam:
            B.append(i)
    for i in range(len(B)):
        B[i] = [ char for char in B[i]]
    return n,m,B
n,m,B = nhap()
print(n,m,B)
def xuli():
    print(B)
X = xuli()
print(X)
