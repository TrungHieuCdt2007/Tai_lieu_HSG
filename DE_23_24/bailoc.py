def nhap():
    fi=open('CARDS.INP','r')
    k,N=fi.readline().split()
    a=list(map(int,fi.read().split()))
    k=int(k)
    n=[]
    s=[]
    for i in range(1,k+1):
        n.append(i)
    for i in range(len(a)):
        s.append(int(a[i])-1)
    return n,N,s
    fi.close()
n,N,s=nhap()
print(n,N,s)
def xuli(n,s):
    tam=0
    luu=0
    the=len(s)-1
    for i in range(1,the+1,2):
        if s[i]==len(n)-1:
            luu=n[s[i-1]]
            n.remove(n[s[i-1]])
            n.append(luu)
        else:
            tam=n[s[i-1]]
            n[s[i-1]]=n[s[i]]
            n[s[i]]=tam
    return n
n=xuli(n,s)
def sapxep(n):
    min=len(n)+1
    tam=0
    kq=0
    for j in range(len(n)):
        for z in range(j+1,len(n)):
            if n[z]==1:
                tam=n[z]
                n[z]=n[j]
                n[j]=tam
                kq=kq+1
            if n[j]>n[z] and n[z]-n[j-1]==1:
                    tam=n[z]
                    n[z]=n[j]
                    n[j]=tam
                    kq=kq+1
    return kq
kq=sapxep(n)
def xuat(kq):
    fo=open('CARDS.OUT','w')
    fo.write(str(kq))
    fo.close()
xuat(kq)
    
