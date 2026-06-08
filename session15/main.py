inventory_stock = 100
total_revenue = 0.0

def add_stock(amount):
    global inventory_stock
    inventory_stock += amount
    print('đã nhập thành công {amount} sản phẩm')


def process_sale(quantity):
    global inventory_stock
    if quantity > inventory_stock:
        print(f'lỗi : không đủ hàng trong kho!!! chỉ còn lại : {inventory_stock}')
    else: 
        return 0
    
def calculate_final_price(quantity,price):
    discount = 0
    global inventory_stock, total_revenue
    # Khi tổ xác nhận đủ hàng, hệ thống mới gọi hàm tính toán chi phí
    # Tính tổng tiền tạm tính = quantity * price.
    total_temp = quantity * price
    # Nếu tổng tiền >= 1000, giảm giá 10% (Tạo biến cục bộ discount trong hàm).
    if total_temp >= 1000:
        discount = total_temp * 0.1
    # Cộng thêm 8% thuế VAT vào tổng tiền sau giảm giá.
    vat = (total_temp - discount) * 0.08
    # return giá trị tổng tiền cuối cùng (final_total).
    final_total = total_temp - discount + vat
    # Hoàn tất giao dịch (Trừ kho và ghi nhận doanh thu):
    # Trừ đi số lượng bán trong inventory_stock.
    inventory_stock -= quantity
    # Cộng final_total vào tổng doanh thu toàn cục (total_revenue).
    total_revenue += final_total

    bill = f'''
        tạm tính : {total_temp}
        tiền được giảm : {discount}
        thuế vat: {vat}
        tổng tiền thanh toán : {final_total}
    '''
    print(bill)

def print_report():
    global inventory_stock,total_revenue
    report = f'''
số lượng còn trong kho: {inventory_stock}
tổng tiền thu được: {total_revenue}
'''
    print(report)

def validate(quantity):
    if quantity.isdigit():
        print('chỉ được nhập số dương')
        return True

menu = '''
        ===========================================
        +  Hệ Thống Quản Lý Kho Hàng & Doanh Thu  +
        ===========================================
        +   1.Nhập thêm vào kho                   +
        +   2.Bán hàng (tính toán hóa đơn)        +
        +   3.xem báo cáo tổng quan               +
        +   4.thoát trương trình                  +
        ===========================================
    '''

try:
    while True:
        print(menu)
        select = int(input('chọn chức năng(1-4): '))
        if select == 1:
            print('-----nhập hàng-----')
            amount = input('nhập số lượng sản phẩm muốn thêm')
        
            add_stock(amount)
        elif select == 2:
            print('---bán hàng---')
            quantity = int(input('nhập số lượng mua'))
            price = int(input('nhập giá tiền : '))
            if process_sale(quantity) == 0:
                calculate_final_price(quantity,price)
        elif select == 3:
            print_report()
        elif select == 4:
            print('thoát')
            break
        else:
            print('vui lòng chọn đúng chức năng')
except ValueError:
    print('bạn cần nhập số yêu cầu nhập lại')
