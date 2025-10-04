

def modify_global_list():
    global my_global_list
    my_global_list.append(4)
    my_global_list.remove(2)
def hai():
    modify_global_list()
# In danh sách trước khi thay đổi
my_global_list = [1, 2, 3]
print("Danh sách trước khi thay đổi:", my_global_list)

# Gọi hàm để thay đổi danh sách
hai()

# In danh sách sau khi thay đổi
print("Danh sách sau khi thay đổi:", my_global_list)
