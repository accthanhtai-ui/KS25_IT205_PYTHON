def menu():
    print("="*50)
    print(" QUẢN LÝ KHO HÀNG - GROCERY STORE ".center(50, "="))
    print("="*50)
    print("1. Xem danh sách hàm tồn kho\n" \
    "2. Nhập thêm hàng hóa mới\n" \
    "3. Cập nhật số lượng tồn kho theo ID\n" \
    "4. Thoát chương trình")
    print("="*50)

def show_inventory(inventory):
    if not inventory:
        print("Kho hàng hiện tại đang trống!")
        return
    print(f"{"ID":<5} | {"Tên hàng hóa":<20} | {"Số lượng tồn kho":<18}")
    print("-"*50)
    for value in inventory:
        print(f"{value.get("id"):<5} | {value.get("name"):<20} | {value.get("quantity"):<18}")
    print("-"*50)

def add_inventory(inventory):
    while True:
        new_id = input("Nhập mã đơn hàng mới: ")
        if not new_id:
            print("Nhập liệu không được để trống!")
            continue
        if not new_id[0] == "G":
            print("Sai định dạng mã ('G' + 'mã số')")
            continue
        flag = False
        for value in inventory:
            if value.get("id") == new_id:
                print("Mã hàng hóa bạn nhập bị trùng!")
                flag = True
                break
        if not flag:
            break

    new_name = input("Nhập tên hàng hóa: ")
    while True:
        new_quantity = input("Nhập số lượng tồn kho: ")
        if not (new_quantity.isdigit() and int(new_quantity) > 0):
            print("Số lượng tồn kho là số nguyên dương lớn hơn 0!")
            continue
        new_quantity = int(new_quantity)
        break
    inventory.append({'id': new_id, 'name': new_name, 'quantity': new_quantity})
    print("Thêm hàng hóa thành công!")

def edit_quantity(inventory):
    while True:
        search_id = input("Nhập mã đơn hàng muốn cập nhật: ")
        if not search_id:
            print("Nhập liệu không được để trống!")
            continue
        if not search_id[0] == "G":
            print("Sai định dạng mã ('G' + 'mã số')")
            continue
        flag = False
        for value in inventory:
            if value.get("id") == search_id:
                flag = True
                print(f"Tìm thấy đơn hàng: {value.get("name")} (Số lượng hiện tại: {value.get("quantity")})")
                while True:
                    new_quantity = input("Nhập số lượng tồn kho mới: ")
                    if not (new_quantity.isdigit() and int(new_quantity) > 0):
                        print("Số lượng tồn kho là số nguyên dương lớn hơn 0!")
                        continue
                    new_quantity = int(new_quantity)
                    break
                value["quantity"] = new_quantity
                print("Cập nhật số lượng thành công!")
                return
        if not flag:
            print(f"Không tìm thấy đơn  hàng có mã [{search_id}]")

inventory = [
    {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
    {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
]

while True:
    menu()
    choice = input("Nhập chức năng: ")
    match choice:
        case '1':
            print()
            print("--- DANH SÁCH HÀN TỒN KHO ---")
            show_inventory(inventory)
            print()
        case '2':
            print()
            print("--- NHẬP HÀNG HÓA MỚI ---")
            add_inventory(inventory)
            print()
        case '3':
            print()
            print("--- CẬP NHẬT SỐ LƯỢNG TỒN KHO ---")
            edit_quantity(inventory)
            print()
        case '4':
            print()
            print("Thoát chương trình!")
            break
        case _:
            print()
            print("Chức năng nhập không hợp lệ!")
            print()