from time import perf_counter
def nhap():
    fo = open('DOCAO.INP', 'r')
    n = fo.readline().split()
    k = fo.readline().split()
    k = list(map(int, k))
    return k

k = nhap()
print(k)
def xuli():
    T = 0
    # # # cách 2 
    n = len(k) - 1
    while (k[n] == 0): # duyệt từ phải sang trái coi số nào mà khác 0
        n -= 1 # có thì n - 1
        j = n # j = n
        
    while (k[j] == k[n] ): # Duyệt từ phải sang trái , băt đầu thì vị trí j ms kiếm được
        j -=1 # Cho quyệt j lần nữa
    if j == 0: # nếu j mà = 0 tức là dãy số đó giảm, ko có số sát sau
        return T
    else: 
        k[j] +=1   # nếu có thì k[j] +=1
        k[n] -=1  #  k[n] -=1
        T = 1 # T = 1
# # # cách 1: Code khác nhưng hướng làm vẫn như cách trên
    # n = len(k) - 1
    # for i in range(n,-1,-1):
    #     if k[i] > 0:
    #         j =  i - 1
    #         break
    # for h in range(j,-1,-1): 
    #         if k[h] < k[i]:
    #             k[h] +=1
    #             k[i] -=1
    #             T = 1 
    #             break
    #         if k[i] == 0:
    #             return T
    
    
    # Lật đoạn i+1 đến n ( bắt buộc phải lật)
    while ( j < n) :
        t = k[n]
        k[n] = k[j]
        k[j] = t
        j +=1
        n -= 1
    return k , T
k,T = xuli()

def xuat(x,H):
    fo = open('DOCAO.out','w')
    fo.write(f'{H}' + str('\n') )
    if H != 0:
        for i in x :
            fo.write(f'{i} ')
bd = perf_counter()        
xuat(k,T)
kt = perf_counter()
print(kt-bd)