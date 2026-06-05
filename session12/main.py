cart_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]
while True:
    print(''' 
=============================================
|        SHOPPY CART MANAGEMENT SYSTEM      |
=============================================
|1. Xem chi tiết giỏ hàng và tính tổng tiền |
|2. Thêm sản phẩm mới/cộng dồn số lượng     |
|3. Cập nhật số lượng của một sản phẩm      |
|4. Xóa sản phẩm khỏi giỏ hàng              |
|5.Thoát trương trình                       |
=============================================
''')
    choice = input('mời bạn nhập chức năng: ')
    match choice:
        case '1':
            sum_quantity = 0
            sum_money = 0
            print('chi tiết giỏ hàng')
            print(f"{"STT":<7}|{"Mã SP":<7}|{"Tên Sản Phẩm":<40}|{"SL":<5}|{"Đơn giá":<15}|{"Thành tiền":<10}")
            for index,item in enumerate(cart_items,start=1):
                print(f'{index:<7}|{item.get("id"):<7}|{item.get("name"):<40}|{item.get("number"):<5}|{item.get("price"):<15,}|{item.get("number")*item.get("price"):<10,}|')
                sum_quantity += item.get("number")
                sum_money_product = item.get("number")*item.get("price")
                sum_money += sum_money_product
            print('='*90)
            print(f'tổng số lượng trong giỏ là : {sum_quantity:,}')
            print(f"tổng tiền thanh toán: {sum_money:,}")
        case '2':
            pro_id = input('nhập mã sản phẩm: ')
            pro_name = input('nhập tên sản phẩm: ')
            while True:
                pro_number = input('nhập số lượng sản phẩm: ')
                if pro_number.isdigit():
                    pro_number =int(pro_number)
                    break
                else:
                    print('không hợp lệ vui lòng nhập lại số lượng')
                    continue
            while True:
                pro_price = input('nhập giá sản phẩm: ')
                if pro_price.isdigit():
                    pro_price =int(pro_number)
                    break
                else:
                    print('không hợp lệ vui lòng nhập lại giá')
                    continue

            found = False
            for index,value in enumerate(cart_items):
                if pro_id == value.get("id"):
                    print('có tồn tại tiến hành cập nhật!')
                    cart_items[index]["number"] += pro_number
                    print('cập nhật thành công')
                    found = True
                    break

                if not found:
                    print('không tồn tại tiến hành thêm mới')
                    new_product = {
                        "id":pro_id,
                        "name":pro_name,
                        "number":pro_number,
                        "price":pro_price
                    }
                    cart_items.append(new_product)
        case '3':
            pro_id = input('nhập mã sản phẩm: ')
            while True:
                pro_number = input('nhập số lượng sản phẩm muốn cập nhật: ')
                if pro_number.isdigit():
                    pro_number =int(pro_number)
                    break
                else:
                    print('không hợp lệ vui lòng nhập lại số lượng')
                    continue

            found = False
            for index,value in enumerate(cart_items):
                if pro_id == value.get("id"):
                    print('có tồn tại tiến hành cập nhật!')
                    cart_items[index]["number"] = pro_number
                    print('cập nhật thành công')
                    found = True
                    break
                if not found:
                    print('không tồn tại')
                    break
        case '4':
            pro_id = input('nhập mã sản phẩm cần xóa: ')
            found = False
            for index,value in enumerate(cart_items):
                if pro_id == value.get("id"):
                    print('có tồn tại tiến hành xóa!')
                    cart_items.pop(index)
                    print('xóa thành công')
                    found = True
                    break
                if not found:
                    print('không tồn tại')
                    break
        case '5':
            print("thoát trương trình")
            break
        case _:
            print('lựa chọn không hợp lệ')