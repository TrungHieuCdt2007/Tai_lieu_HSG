n = 3
k = 2
def xuat(h):
    print(h)
def xuli(k, thu):
    for i in range(1,n+1):
        m.append(i)
    if k == 0:  
        xuat(a) 
        return
    for j in range(n):
        if thu[j] == 'Sai':
            a.append(m[j])
            thu[j] = 'Dung'
            xuli(k-1,thu)
            a.pop()
            thu[j] = 'Sai'
m = []           
a = []
thu = ['Sai'] * n
xuli(k,thu)
