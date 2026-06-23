class DeliveryOrder:
    def __init__(self,order_id  ,receiver_name   ,base_fee   ,distance  ,surcharge):
        self.order_id  = order_id  # Mã vận đơn
        self.receiver_name  = receiver_name  # Tên người nhận
        self.base_fee  = base_fee  #Cước phí nền cơ bản 
        self.distance  = distance  #Khoảng cách giao hàng - km
        self.surcharge  = surcharge  #Phụ phí hàng cồng kềnh/phát sinh
        self.total_delivery_cost   = 0 #Tổng chi phí vận chuyển
        self.delivery_status  = "" #Trạng thái/Phân loại đơn hàng

    def calculate_total_cost(self):
        self.total_delivery_cost  = self.base_fee * self.distance + self.surcharge

    def classify_delivery_status(self):
        if self.calculate_total_value < 100000:
            self.delivery_status = "Đơn hàng Tiêu chuẩn (Nội thành)"
        elif self.calculate_total_value < 300000:
            self.delivery_status = "Đơn hàng Cận tỉnh"
        elif self.calculate_total_value < 600000:
            self.delivery_status = "Đơn hàng Đường dài (Cần giám sát)"
        else:
            self.delivery_status = "Đơn hàng Đặc biệt (Ưu tiên cao - Rủi ro cao)"



class OrderManager:
    def __init__(self):
        self.orders: list[DeliveryOrder] = []
    def add_order(self):
        while True:
            or_id = input("nhập mã đơn hàng")
            if not or_id:
                print("không được để trống")
            for item in self.orders:
                if or_id == item.order_id:
                    print("mã đơn hàng này đã tồn tại")
            else:
                break
        while True:
            name = input("nhập tên vào : ")
            if not name:
                print("không được dữ liệu trống")
            else :
                break


    def show_all_orders(self):
        if not self.orders:
            print("không được để trống")
            return
        else:
            print(f"{'Mã Đơn':<7}|{f'Tên người nhận':<18}|{'cước nền':<10}|{'Khoảng cách (km)':<18}|{'Phụ phí':<10}|{'Tổng chi phí':<18}|{'Trạng thái đơn':<20}")
            for item in self.orders:
                print(f"{item.order_id:<7}|{item.receiver_name:<18}|{item.base_fee:<10}|{item.distance:<18}|{item.surcharge:<10}|{item.total_delivery_cost:<18}|{item.delivery_status:<20}")

    def update_order(self):
        if not self.orders:
            print("không được để trống")
            return
        pass
    def delete_order(self):
        if not self.orders:
            print("không được để trống")
            return
        pass
    def search_by_receiver(self):
        if not self.orders:
            print("không được để trống")
            return
        pass

def main():
    current_manager = OrderManager()
    current_manager.orders = [
        DeliveryOrder("C1","Trần Hà Linh" ,30000 ,5 ,5000),
        DeliveryOrder("C2","Trần Đức Bo" ,40000 ,12 ,10000)

    ]
    while True:
        print("""
================ MENU =======================
1. Hiển thị danh sách vận đơn trong hệ thống
2. Nhập vận đơn mới
3. Cập nhật thông tin vận đơn
4. Xóa vận đơn khỏi hệ thống
5. Tìm kiếm vận đơn theo tên người nhận
6. Thoát
=============================================
""")
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                current_manager.show_all_orders()
            case "2":
                print()
            case "3":
                print()
            case "4":
                print()
            case "5":
                print()
            case "6":
                print("thoát trương trình")
                break
            
main()