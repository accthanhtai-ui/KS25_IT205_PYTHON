qty_laptop = 0
qty_phone = 0
qty_tablet = 0

while True:
    print("--- HỆ THỐNG QUẢN LÝ KHO ---")
    print('1. Xem báo cáo tồn kho')
    print('2. Nhập kho')
    print('3. Xuất kho')
    print('4. Cảnh báo hàng tồn kho thấp')
    print('5. Thoát chương trình')
    choice = int(input('Chọn chức năng: '))
    
    if choice == 1:
        print(f'Laptop({qty_laptop}): {"*"*qty_laptop}')
        print(f'Laptop({qty_phone}): {"*"*qty_phone}')
        print(f'Laptop({qty_tablet}): {"*"*qty_tablet}')
        print()
    
    elif choice == 2:
        warehouse=int(input('Bạn muốn nhập hàng nào (1-Laptop, 2-Phone, 3-Tablet): '))
        if warehouse < 1 or warehouse > 3:
            print('Lựa chọn không hợp lệ\n')
        else:
            while True:
                enter_quantity = int(input('Nhập số lượng cần thêm: '))           
                if enter_quantity < 0:
                    print('Số lượng không hợp lệ, vui lòng nhập lại')
                else:
                    if warehouse == 1:
                        qty_laptop += enter_quantity
                    elif warehouse == 2:
                        qty_phone += enter_quantity
                    else:
                        qty_tablet += enter_quantity
                    print()
                    break
                
    
    elif choice == 3:
        export_from_warehouse=int(input('Bạn muốn xuất hàng nào (1-Laptop, 2-Phone, 3-Tablet): '))
        if export_from_warehouse < 1 or export_from_warehouse > 3:
            print('Lựa chọn không hợp lệ\n')
        else:
            while True:
                output_quantity = int(input('Nhập số lượng cần xuất: '))
                if output_quantity < 0:
                    print('Số lượng không hợp lệ, vui lòng nhập lại')
                else:
                    if export_from_warehouse == 1:
                        if output_quantity > qty_laptop:
                            print("Không đủ hàng")
                        else:
                            qty_laptop -= output_quantity
                    elif export_from_warehouse == 2:
                        if output_quantity > qty_phone:
                            print("Không đủ hàng")
                        else:
                            qty_phone -= output_quantity
                    else:
                        if output_quantity > qty_tablet:
                            print("Không đủ hàng")
                        else:
                            qty_tablet -= output_quantity
                    print()
                    break
    
    elif choice == 4:
        if qty_laptop < 10:
            print(f'[CẢNH BÁO] Mặt hàng Laptop sắp hết (Chỉ còn {qty_laptop} sản phẩm)')
        if qty_phone < 10:
            print(f'[CẢNH BÁO] Mặt hàng Điện thoại sắp hết (Chỉ còn {qty_phone} sản phẩm)')
        if qty_laptop < 10:
            print(f'[CẢNH BÁO] Mặt hàng Máy tính bảng sắp hết (Chỉ còn {qty_tablet} sản phẩm)')
        print()
    
    elif choice == 5:
        break
    
    else:
        print("Lựa chọn không hợp lệ\n")