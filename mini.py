def display_orders(orders):
    if not orders:
        print("Danh sách đơn hàng trống!")
        return
    print(f"{'Mã ĐH':<10}{'Tên đại lý':<25}{'Giá trị (VND)':>15}{'Trạng thái':>12}")
    print("-" * 65)
    for order in orders:
        print(f"{order['id']:<10}{order['name']:<25}{order['price']:>15,}{order['status']:>12}")

def add_order(orders):
    while True:
        order_id = input("Nhập mã đơn hàng: ").strip()
        if order_id == "":
            print("Mã đơn hàng không được để trống!")
            continue
        if any(order['id'] == order_id for order in orders):
            print("ERR-01: Mã đơn hàng đã tồn tại, hủy thao tác!")
            return
        break

    while True:
        agent_name = input("Nhập tên đại lý: ").strip()
        if agent_name == "":
            print("Tên đại lý không được để trống!")
            continue
        break

    while True:
        try:
            price = int(input("Nhập giá trị đơn hàng (VND): "))
            if price <= 0:
                print("Giá trị phải lớn hơn 0!")
                continue
            break
        except ValueError:
            print("Giá trị phải là số nguyên!")

    orders.append({'id': order_id, 'name': agent_name, 'price': price, 'status': 'Unpaid'})
    print("Thêm đơn hàng thành công!")


def update_status(orders):
    order_id = input("Nhập mã đơn hàng cần cập nhật: ").strip()
    for order in orders:
        if order['id'] == order_id:
            if order['status'] == 'Unpaid':
                order['status'] = 'Paid'
                print("Cập nhật trạng thái thành công!")
                return
            else:
                print("ERR-04: Đơn hàng đã thanh toán trước đó!")
                return
    print("ERR-03: Không tìm thấy mã đơn hàng!")


def calculate_revenue(orders):
    revenue = sum(order['price'] for order in orders if order['status'] == 'Paid')
    discount_rate = 0.05 if revenue >= 100_000_000 else 0.0
    discount_amount = revenue * discount_rate
    return revenue, discount_rate * 100, discount_amount


def main():
    orders = [
        {'id': 'HD01', 'name': 'Đại lý Hoàng Long', 'price': 45000000, 'status': 'Paid'},
        {'id': 'HD02', 'name': 'Tạp hóa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}
    ]

    while True:
        print("\n===== MENU QUẢN LÝ ĐƠN HÀNG =====")
        print("1. Xem danh sách đơn hàng")
        print("2. Tạo mới đơn hàng")
        print("3. Cập nhật trạng thái thanh toán")
        print("4. Tính tổng doanh thu & Chiết khấu")
        print("5. Thoát chương trình")

        try:
            choice = int(input("Nhập lựa chọn (1-5): "))
        except ValueError:
            print("Vui lòng nhập số từ 1 đến 5!")
            continue

        match choice:
            case 1:
                display_orders(orders)
            case 2:
                add_order(orders)
            case 3:
                update_status(orders)
            case 4:
                revenue, discount_rate, discount_amount = calculate_revenue(orders)
                print(f"Tổng doanh thu: {revenue:,} VND")
                print(f"Chiết khấu: {discount_rate:.0f}%")
                print(f"Số tiền chiết khấu: {discount_amount:,} VND")
            case 5:
                print("Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập từ 1 đến 5!")

main()
