total_invoice = int(input('nhập số tiền hóa đơn ban đầu'))
if(total_invoice >= 500000):
    discount_price = total_invoice * 0.1
    total_invoice *= 0.9
print('hiển thị')
print('sô tiền được giảm',discount_price)
print('số tiền khách phải trả',total_invoice)