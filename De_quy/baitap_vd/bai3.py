import math

def kiem_tra_so_chinh_phuong(n):
    # Tính căn bậc hai của n
    can_bac_hai = math.sqrt(n)
    print(can_bac_hai**2)
    # Kiểm tra xem căn bậc hai có phải là số nguyên hay không
    if can_bac_hai.is_integer():
        return True
    else:
        return False

# Ví dụ
so_can_kiem_tra = 2
if kiem_tra_so_chinh_phuong(so_can_kiem_tra):
    print(f"{so_can_kiem_tra} là số chính phương.")
else:
    print(f"{so_can_kiem_tra} không phải là số chính phương.")
