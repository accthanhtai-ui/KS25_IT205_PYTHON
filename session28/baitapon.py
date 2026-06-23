class DeliveryOrder:
    def __init__(self, order_id, receiver_name, base_fee, distance, surcharge):
        self.order_id = order_id
        self.receiver_name = receiver_name
        self.base_fee = base_fee
        self.distance = distance
        self.surcharge = surcharge
        self.total_delivery_cost = 0
        self.delivery_status = 'Chưa cập nhật'
        self.calculate_total_cost()
        self.classify_delivery_status()

    def calculate_total_cost(self):
        self.total_delivery_cost = (self.base_fee * self.distance) + self.surcharge

    def classify_delivery_status(self):
        if self.total_delivery_cost >= 600000:
            self.delivery_status = 'Đơn hàng Đặc biệt (Ưu tiên cao -Rủi ro cao)'
        elif self.total_delivery_cost >= 300000:
            self.delivery_status = 'Đơn hàng Đường dài (Cần giám sát)'
        elif self.total_delivery_cost >= 100000:
            self.delivery_status = 'Đơn hàng Cận tỉnh'
        else: self.delivery_status = 'Đơn hàng Tiêu chuẩn (Nội thành)'

class OrderManager:
    def __init__(self):
        self.orders: list[DeliveryOrder] = []

    def add_order(self):
        while True:
            or_id = input("Nhập mã vận đơn: ").strip()
            if not or_id:
                print("Nhập liệu không được để trống! Nhập lại!")
                continue
            for value in self.orders:
                if or_id == value.order_id:
                    print("Mã vận đơn đã tồn tại! Nhập lại!")
                    break
            else:
                break

        while True:
            or_receiver_name = input("Nhập tên người nhận: ").strip()
            if not or_receiver_name:
                print("Nhập liệu không được để trống! Nhập lại!")
                continue
            break

        while True:
            try: 
                or_base_fee = float(input("Nhập cước phí nền cơ bản: ").strip())
                if not or_base_fee:
                    print("Nhập liệu không được để trống! Nhập lại!")
                    continue
                if or_base_fee <= 0:
                    print("Giá cước phí nền cơ bản phải lớn hơn 0! Nhập lại!")
                    continue
                break
            except ValueError:
                print("số tiền bạn nhập không phù hợp dữ liệu! Nhập lại!")
                continue

        while True:
            try: 
                or_surcharge = float(input("Nhập phụ phí hàng cồng kềnh / phát sinh: ").strip())
                if not or_surcharge:
                    print("Nhập liệu không dược để trống! Nhập lại!")
                    continue
                if or_surcharge <= 0:
                    print("Giá phụ phí phải lớn hơn 0! Nhập lại!")
                    continue
                break
            except ValueError:
                print("số tiền bạn nhập không phù hợp dữ liệu! Nhập lại!")
                continue

        while True:
            try:
                or_distance = int(input("Nhập khoảng cách giao hàng - km: ").strip())
                if not or_distance:
                    print("Nhập liệu không được để trống! Nhập lại!")
                    continue
                if or_distance < 1 or or_distance > 5000:
                    print("Khoảng cách giao hàng chỉ nằm trong khoản 1km đến 5000km! Nhập lại!")
                    continue
                break
            except value:
                print("khoảng cách giao hàng không hợp lệ! Nhập lại!")
                continue

        new_order = DeliveryOrder(or_id, or_receiver_name, or_base_fee, or_distance, or_surcharge)

        self.orders.append(new_order)

        print("Thêm thành công vận đơn mới!\n")



    def show_all_order(self):
        if not self.orders:
            print("hiện tại không có đơn nào!")
            return
        print("=" * 150) 
        print(f"{'Mã Đơn':<6} | {'Tên người nhận':<25} | {'Cước nền':<10} | {'Khoản cách (km)':<20} | {'Phụ phí':<10} | {'Tổng chi phí':<12} | {'Trạng thái đơn':<20}")
        print("=" * 150) 
        for value in self.orders:
            print(f"{value.order_id:<6} | {value.receiver_name:<25} | {value.base_fee:<10} | {value.distance:<20} | {value.surcharge:<10} | {value.total_delivery_cost:<12} | {value.delivery_status:<20}")

    def update_order(self):
        if not self.orders:
            print("hiện tại không có đơn nào!")
            return
        while True:
            or_id = input("Nhập mã vận đơn: ").strip()
            if not or_id:
                print("Nhập liệu không được để trống! Nhập lại!")
                continue
            for value in self.orders:
                if or_id == value.order_id:
                    print(f"tìm thấy mã vận đơn {value.order_id} - {value.receiver_name} - {value.total_delivery_cost}")
                    while True:
                        try: 
                            or_base_fee = float(input("Nhập cước phí nền cơ bản: ").strip())
                            if not or_base_fee:
                                print("Nhập liệu không được để trống! Nhập lại!")
                                continue
                            if or_base_fee <= 0:
                                print("Giá cước phí nền cơ bản phải lớn hơn 0! Nhập lại!")
                                continue
                            break
                        except ValueError:
                            print("số tiền bạn nhập không phù hợp dữ liệu! Nhập lại!")
                            continue

                    while True:
                        try: 
                            or_surcharge = float(input("Nhập phụ phí hàng cồng kềnh / phát sinh: ").strip())
                            if not or_surcharge:
                                print("Nhập liệu không dược để trống! Nhập lại!")
                                continue
                            if or_surcharge <= 0:
                                print("Giá phụ phí phải lớn hơn 0! Nhập lại!")
                                continue
                            break
                        except ValueError:
                            print("số tiền bạn nhập không phù hợp dữ liệu! Nhập lại!")
                            continue

                    while True:
                        try:
                            or_distance = int(input("Nhập khoảng cách giao hàng - km: ").strip())
                            if not or_distance:
                                print("Nhập liệu không được để trống! Nhập lại!")
                                continue
                            if or_distance < 1 or or_distance > 5000:
                                print("Khoảng cách giao hàng chỉ nằm trong khoản 1km đến 5000km! Nhập lại!")
                                continue
                            break
                        except value:
                            print("khoảng cách giao hàng không hợp lệ! Nhập lại!")
                            continue

                    value.base_fee = or_base_fee
                    value.distance = or_distance
                    value.surcharge = or_surcharge
                    print("Cập nhật thành công!")
                    return
            else:
                print("Không tìm thấy vận đơn nào mang mã này!")
                return

    def delete_order(self):
        if not self.orders:
            print("hiện tại không có đơn nào!")
            return
        while True:
            or_id = input("Nhập mã vận đơn: ").strip()
            if not or_id:
                print("Nhập liệu không được để trống! Nhập lại!")
                continue
            for value in self.orders:
                if or_id == value.order_id:
                    print(f"tìm thấy mã vận đơn {value.order_id} - {value.receiver_name} - {value.total_delivery_cost}")
                    while True:
                        confirm = input("Bạn có chắc muốn xóa vận đơn này khỏi hệ thống không? (Y/N): ").strip().upper()
                        match confirm:
                            case 'Y':
                                self.orders.remove(value)
                                print("Xóa vận đơn thành công!")
                                return
                            case 'N':
                                print("Hoàn thành với thao tác không xóa!")
                                return
            else:
                print("Không tìm thấy vận đơn nào mang mã này!")
                return

    def search_by_receiver(self):
        if not self.orders:
            print("hiện tại không có đơn nào!")
            return
        while True:
            or_receiver_name = input("Nhập tên người nhận: ").strip()
            if not or_receiver_name:
                print("Nhập liệu không được để trống! Nhập lại!")
                continue
            break

        flag = False
        print("=" * 150) 
        print(f"{'Mã Đơn':<6} | {'Tên người nhận':<25} | {'Cước nền':<10} | {'Khoản cách (km)':<20} | {'Phụ phí':<10} | {'Tổng chi phí':<12} | {'Trạng thái đơn':<20}")
        print("=" * 150) 
        for value in self.orders:
            if or_receiver_name.lower() in value.receiver_name.lower():
                print(f"{value.order_id:<6} | {value.receiver_name:<25} | {value.base_fee:<10} | {value.distance:<20} | {value.surcharge:<10} | {value.total_delivery_cost:<12} | {value.delivery_status:<20}")
                flag = True
        else:
            if not flag:
                print('\nKhông có vận đơn nào phù hợp')
                return



def main():
    current_manager = OrderManager()
    current_manager.orders = [
        DeliveryOrder("OD001", "Nguyen Văn A", 50000, 6, 25000),
        DeliveryOrder("OD002", "Tran Thao C", 100000, 10, 30000)
    ]
    while True:
        print()
        print(" MENU ".center(50, "="))
        print("1. Hiển thị danh sách vận đơn trong hệ thống\n" \
        "2. Nhập vận đơn mới\n" \
        "3. Cập nhật thông tin vận đơn\n" \
        "4. Xóa vận đơn khỏi hệ thống\n" \
        "5. Tìm kiếm vận đơn theo tên người nhận\n" \
        "6. Thoát")
        print("=" * 50)

        choice = input("Nhập lựa chọn của bạn: ")

        match choice:
            case '1':
                current_manager.show_all_order()
            case '2':
                current_manager.add_order()
            case '3':
                current_manager.update_order()
            case '4':
                current_manager.delete_order()
            case '5':
                current_manager.search_by_receiver()
            case '6':
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý vận đơn!")
                return
            case _:
                print("Lựa chọn không hợp lệ! Nhập lại!")
                continue

if __name__ == "__main__":
    main()