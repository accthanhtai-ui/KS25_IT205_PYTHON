#students = list()
# students =[1,2,3,4,5]
# students =["Trọng Nguyên",18,1.78,True]

# students = ["Sang","khương"]
# # students.append("Nguyên")
# students.insert(2, "ưng")

# students.extend(("Tú","Minh"))
# print(students)

# students.extend(["Tú","Minh"])
# print(students)
# students = ["Sang", "Khương", "Việt"]

# for i in range(len(students)):
#     print(f"Sinh viên thứ {i+1}:", students[i])
# students = ["Sang", "Khương", "Việt"]

# for index, item in enumerate(students, start=1):
#     print(f"Sinh viên thứ {index}: {item}")

# yêu cầu: tạo 1 danh sách sinh viên, cho người dùng nhập vào số lượng sinh viên
# chức năng 1, nhập vào từng sinh viên(nhập sinh viên thứ 1:....)
# chức năng 2, hiển thị ra từng sinh viên(sinh viên thứ 1 là :.....)

students = []
quanity =int(input("Nhập vào số lượng sinh viên: "))
for i in range(quanity):
    name=input(f"Nhập sinh viên thứ {i+1}:")
    students.append(name)
for index, name in enumerate(students, start=1):
     print(f"Sinh viên thứ {index} là: {name}")
