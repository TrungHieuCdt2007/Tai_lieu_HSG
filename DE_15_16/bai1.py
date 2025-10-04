from math import gcd
def nhap():
    fi = open('CN.inp')
    x,dx = list(map(int,fi.readline().split()))
    d,dd = list(map(int,fi.readline().split()))
    t,dt = list(map(int,fi.readline().split()))
    v,dv = list(map(int,fi.readline().split()))
    return x,dx,d,dd,t,dt,v,dv
x,dx,d,dd,t,dt,v,dv = nhap()

def xuli():
    # Lí do ta tính BCNN và tính số đoạn của cặp xanh - tim và đỏ - vàng thay vì
    # Xanh - đỏ và Tím - vàng (Theo chiều kim đồng hồ của đề).
    # Tại đề yêu cầu ta tính diện tính hình chữ nhật lớn nhất thì phải cần chiều dài
    # và rộng, nếu tính theo cặp Xanh - đỏ và Tìm - vàng thì sẽ ko đảm bảo được diện tích
    # của các cặp màu bằng nhau vì khi đó ta đã tính tiếng chiều dài rộng của từng cặp màu
    # chỉ lấy được chiều dài và rộng lớn nhất của các cặp.
    # Cho nên ta sẽ tính các cặp màu là Xanh - tím và Đỏ - vàng để đảm bảo được :
    # Diện tích theo dài và rộng là lớn nhất và giữa các Cặp màu là bằng nhau
    bcnn_tx = ((dx*dt)//gcd(dx,dt)) #Tích bội chung nhủ nhất của đoạn thảnh x - t
    nx = bcnn_tx // dx # tìm số đoạn x trong cặp x - t
    nt = bcnn_tx // dt # tìm số đoạn t trong cặp x - t
    nxt = min(t // nt, x // nx) # chọn số đoạn nhỏ nhất trong mỗi cặp x - t
    nx = nxt * nx # số đoạn cần nhỏ = số đoạn nhỏ nhất với số đoạn trong mỗi cặp
    nt = nxt * nt
    
    bcnn_vd = ((dv*dd)//gcd(dv,dd))#Tích bội chung nhủ nhất của đoạn thảnh v - d
    nd = bcnn_vd // dd# tìm số đoạn x trong cặp d - v
    nv = bcnn_vd // dv# tìm số đoạn t trong cặp d - v
    ndv = min( v // nv , d // nd)
    nd = ndv * nd # số đoạn cần nhỏ = số đoạn nhỏ nhất với số đoạn trong mỗi cặp
    nv = ndv * nv
    Tich = ( nd * dd * nx*dx) # tính tích bằng tích của 2 cạnh rộng và dài tức là 2 màu xanh và đỏ
    # có thể đổi thàng Vàng và tím , theo chiều rộng và dài ( theo chiều kim đồng hồ của đề )
    return nx,nd,nt,nv,Tich
nx,nd,nt,nv,Tich = xuli()

def xuat():
    fo = open('CN.out','w')
    fo.write(f'{Tich}' + str('\n'))
    fo.write(f'{nx} {nd} {nt} {nv}')
    fo.close()
xuat()
