numbers = (1, 2, 3, 4, 5)
products = ("P001", "P002", "P003", "P004")
info = ("Phúc Nguyên", 19, "Có người yêu", True)

#info[0] = "Minh Nghĩa"
#print(info[0])
#Cách1
#for i in range(len(info))
#    print(info[i])
#Cách 2
#for item in info:
#    print(item)
#cách 3
#for index, value in enumerate(info, start=1):
 #   print(value)


#users = {
#    "name": "Nhân Đức",
 #   "age": 17,
 #   "status": "alone"
#}
#Cách 1
#print(users["status"])
#cách 2 lấy từ Nhân Đức
#print(users.get("name"))

#Cách 3 muốn hiện thị ra tất cả

#print(user.get("name", "Không có"))
#user["phone"] = "0932323232"
#user["phone"] = "0892382122"

#users.pop("status")
#del users("status")
#print(users["status"])
#for value in users.values():
#    print(value)

#for key, value in users.items():
#    print(key, value)
#list_user = ("user001", "user002", "user003")
#users = {
#    "list_user[0]": {"name": "Bảo", "age": 18},
#    "list_user[1]": {"name": "Phúc", "age": 20},
#    "list_user[2]": {"name": "Tín", "age": 19},
#}
#cách 1
#print(users["user002"]["name"])
#Cách 2
#print(users.get("user002").get("name"))
#dùng biến tuple :
# print(users.get(list_user[0]).get("name"))

# Yêu cầu: tạo 1 danh sách user. []
# Thêm 5 phần tử vào danh sách.
# Mỗi phần tử là 1 dict {}
# Hiển thị toàn bộ thông tin user ra màn hình for

users = [
    { "name": "Tuấn", "age": 25 },
    { "name": "Trường", "age": 25 },
    { "name": "Bảo", "age": 25 },
]

for i in range(len(users)):
    print(f"Sinh viên: {users[i]['name']:<10} | tuổi: {users[i]['age']}")