total_invoice = int(input('nhập số lượng hóa đơn trong ca'))
max = None
min = None
for i in range(1,total_invoice+1):
    value_invoce = float(input(f'nhập giá trị đơn thứ {i}'))
    if max is None or value_invoce > max:
        max = value_invoce
    if min is None or value_invoce < min:
        min = value_invoce
print('hóa đơn có gia trị cao nhất',max)
print('hóa đơn có gia trị nhỏ nhất',min)
