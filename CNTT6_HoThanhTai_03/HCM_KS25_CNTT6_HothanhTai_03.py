def menu(users):
    print('''
1. hiển thị danh sách khách hàng
2. đăng kí khách hàng mới
3. cập nhật thông tin giao dịch
4. xóa dữ liệu khách hàng
5. tìm kiếm khách hàng
6. thống kê phân loại thành viên
7. phân hạng khách hàng tự động
8. thoát
''')
def validate_input(prompt: str, type: str = 'str'):
    while True:
        value = input(prompt)

        if not value:
            print('không được để trống, nhập lại!')
            continue
        if type == 'int':
            try:
                value_int = int(value)
                if value_int < 0:
                    print('vui lòng nhập số nguyên dương')
                    continue
                return value_int
            except ValueError:
                print('dữ liệu sai, nhập lại!')
                continue
        return value
def xep_hang(total_money):
    if total_money < 5:
        return 0.05, "đồng"
    elif total_money < 15000000:
        return 0.02, "Bạc"
    elif total_money < 30000000:
        return 0.0, "vàng"
    else: 
        return 0.1, "kim cương"
def display_user(users):
    if not users:
        print("hiện tại danh sách đang rỗng")
        return
    print(f'{"Mã":<8}|{"Họ tên":<20}|{"SĐT":<15}|{"Tổng tiền":<15}|{"Số lần mua":<12}|{"Chiết khấu":<12}|{"Hạng":<10}')
    for user in users:
        print(f'{user["id"]:<8}|{user["name"]:<20}|{user["phone"]:<15}|{user["sum"]:<15}|{user["number"]:<12}|{user["discount"]:<12}|{user["rank"]:<10}')
def add_users(users):
    customer_id = validate_input("nhập mã khách hàng: ")
    name = validate_input("nhập họ tên: ")
    phone = validate_input("nhập số điện thoại: ")
    total_money = validate_input("nhập tổng chi tiêu ban đầu: ", "int")
    number_buy = validate_input("nhập số lần mua ban đầu: ", "int")

    discount, rank = xep_hang(total_money)

    users.append({
        "id": customer_id,
        "name": name,
        "phone": phone,
        "sum": total_money,
        "number": number_buy,
        "discount": discount,
        "rank": rank
    })

    print("đăng kí khách hàng thành công!")
def update_user(users):
    customer_id = validate_input("nhập mã khách hàng cần cập nhật: ")
    for user in users:
        if user["id"] == customer_id:
            user["sum"] = validate_input("nhập tổng chi tiêu mới: ", "int")
            user["number"] = validate_input("nhập số lần mua mới: ", "int")

            user["discount"], user["rank"] = xep_hang(user["sum"])

            print("cập nhật thành công!")
            return
    print("không tìm thấy thông tin khách hàng")
def del_user(users):
    customer_id = validate_input("nhập mã khách hàng cần xóa: ")
    for user in users:
        if user["id"] == customer_id:
            confirm = input("bạn có chắc muốn xóa không? (Y/N): ")

            if confirm.upper() == "Y":
                users.remove(user)
                print("xóa thành công!")
            else:
                print("đã hủy xóa")

            return
    print("không tìm thấy thông tin khách hàng")

def search_users(users):
    input_search = validate_input("nhập mã hoặc họ tên: ")
    found = False
    for user in users:
        if input_search == user["id"]:
            display_user([user])
            found = True
        elif input_search.lower() in user["name"].lower():
            display_user([user])
            found = True
    if not found:
        print("không tìm thấy khách hàng")
def main():
    users = [
        {
            "id": "KH001",
            "name": "Trần Minh Cường",
            "phone": "0987654321",
            "sum": 12500000,
            "number": 5,
            "discount": 0.05,
            "rank": "Vàng"
        }
    ]
    while True:
        menu(users)
        choice = input("vui lòng chọn chức năng: ")
        match choice:
            case '1':
                display_user(users)
            case '2':
                add_users(users)
            case '3':
                update_user(users)
            case '4':
                del_user(users)
            case '5':
                search_users(users)
            case '6':
                print()
            case '7':
                print()
            case '8':
                print("đã thoát chương trình")
                break
            case _:
                print("nhập không hợp lệ, vui lòng nhập lại!")
main()
