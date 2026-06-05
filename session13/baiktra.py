
staff_company = [
    {"id": "101", "name": "Nguyễn Văn A", "salary": 10},
    {"id": "102", "name": "Le Thi B", "salary": 15}
]
while True:
    print('''
=============================================
       QUẢN LÝ NHÂN SỰ-STAFF MANAGER
=============================================
1.Thêm nhân viên mới
2.Danh sách nhân viên
3.Xóa nhân viên khỏi hệ thống
4.Thoát trương trình
=============================================
''')
    choice=input('nhập vào chức năng bạn muốn dùng: ')
    match choice:
        case '1':
            if len(staff_company) == 0:
                new_id = 101
            else:
                new_id = int(staff_company[-1]["id"]) + 1

            while True:
                name = input("Nhập tên nhân viên: ").strip()
                if name != "":
                    break
                print("Tên không được để trống!")

            salary_new = float(input('nhập lương vào'))
                
        case '2':
            if len(staff_company) != 0:
                    print(f'{'id':<7}|{'tên':<15}|{'lương':<15}')
                    for index,value in enumerate(staff_company):
                        print(f'{value.get('id'):<7}|{value.get('name'):<15}|{value.get('salary'):<15}')
            else:
                print('Chưa có dữ liệu nhân sự')
                    
        case '3':
            del_id = input("Nhập vào id cần xóa: ") 
            found = False; 
            for index, value in enumerate(staff_company):
                if (del_id == value.get("id")):
                    print("Có tồn tại, tiến hành xóa!")
                    del staff_company[index]                        
                    found = True
                    break
                if (not found):        
                    print("Không có tồn tại nhân viên")
        case '4':
            print('thoát trương trình')
            break
        case _ :
            print('chọn không đúng chức năng vui lòng chọn lại')
