# Yêu cầu: Tạo 1 menu gôm 3 chức năng. Menu phải dùng hàm
# Chức năng 1: Nhập sinh viên vào danh sách (Nhập số lượng sv, rồi nhập từng sv vào)
# Chức năng 2: HIển thị danh sách sinh viên ra màn hình
# Chức năng 3: Tìm kiếm sinh viên theo tên (tìm tương đối)
# Lưu ý: tất cả đều dùng hàm để gọi vào trong mỗi case
def get_validate_input(prompt: str,input_type: str = 'str'):
    while True:
        user_input = input(prompt)
        if not user_input:
            print('không để trống , nhập lại')
            continue
        if input_type == 'int':
            # if user_input.isdigit():
            #     value = int(user_input)
            #     return value
            # else:
            #     print('vui lòng nhập số,nhập lại')
            #     continue

def menu():
    print("=" * 60)
    print("=====Menu=======")
    print("1. Nhập danh sách sinh viên\n" +
          "2. Hiển thị danh sách sinh viên\n" +
          "3. Tìm kiếm danh sách sinh viên theo tên\n" +
          "4. Thoát chương trình!\n"
    )
    print("=" * 60)

def input_std(students):
    # global students; 
    num_std = int(input("Nhập số lượng sinh viên: "))
    for i in range(num_std):
        print(f"Nhập sinh viên thứ {i + 1}")
        id_std = input("Nhập vào id sinh viên: ")
        name_std = input("Nhập vào tên sinh viên: ")
        new_std = { "id": id_std, "name": name_std }
        students.append(new_std)

def show_std(students):
    # global students;
    print("Danh sách sinh viên!")
    for index, value in enumerate(students):
        print(f"Sinh viên thứ {index + 1}: Id: {value.get("id")} - Tên: {value.get("name")}")

def search_std(students):
    print()
    print("Tìm sinh viên")
    inp_name = input("Nhập từ khóa tên mà bạn muốn tìm: ").strip().lower()
    for index, value in enumerate(students):
        if inp_name in value.get("name").lower():
            print(f"STT: {index} - Id: {value.get("id")} - Tên: {value.get("name")}")

def main():
    students = []; 
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                input_std(students)
            case "2":
                show_std(students)
            case "3":
                search_std(students)
            case "4":
                print("Thoát chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

main()