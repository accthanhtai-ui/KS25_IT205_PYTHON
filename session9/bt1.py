# Phân tích lỗi
# Sau khi chạy dòng lệnh:

# python
# delivery_orders.insert(0, "GE000")
# → "GE000" được chèn vào đầu danh sách, các phần tử cũ dịch sang phải. Danh sách trở thành: ["GE000", "GE001", "GE002", "GE003-CANCEL", "GE004"].

# Vì sao dòng sau sửa sai đơn hàng cần cập nhật?

# python
# delivery_orders[1] = "GE002-UPDATED"
# Sau khi chèn "GE000" vào đầu, "GE002" không còn ở vị trí index 1 nữa, mà nằm ở index 2. Do đó lệnh này sửa nhầm "GE001".

# Sau khi chèn "GE000" vào đầu danh sách, "GE002" đang nằm ở index nào?  
# → Index 2 (vì danh sách lúc này là ["GE000", "GE001", "GE002", "GE003-CANCEL", "GE004"]).

# Vì sao dòng sau gây lỗi?

# python
# delivery_orders.remove(3)
# → remove() xóa theo giá trị, không phải theo chỉ số. Ở đây giá trị 3 không tồn tại trong danh sách nên báo lỗi.

# Phương thức remove() xóa phần tử theo giá trị hay theo vị trí?  
# → Theo giá trị.

# Muốn xóa đơn hàng "GE003-CANCEL", cần viết lệnh như thế nào?

# python
# delivery_orders.remove("GE003-CANCEL")
# Phương thức pop() có tác dụng gì?  
# → Xóa phần tử theo chỉ số (mặc định là cuối danh sách) và trả về phần tử vừa bị xóa.

# Vì sao chương trình báo lỗi khi in biến transferred_order?  
# → Vì chưa gán giá trị trả về của pop() cho biến transferred_order.

# Muốn lưu lại đơn hàng vừa lấy ra bằng pop(), cần viết lệnh như thế nào?

# python
# transferred_order = delivery_orders.pop()

# Danh sách đơn hàng ban đầu
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
delivery_orders.append("GE004")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
delivery_orders.insert(0, "GE000")

# Sửa mã đơn hàng GE002 thành GE002-UPDATED
# Sau khi chèn GE000, GE002 nằm ở index 2
delivery_orders[2] = "GE002-UPDATED"

# Xóa đơn hàng bị khách hủy
delivery_orders.remove("GE003-CANCEL")

# Lấy đơn hàng cuối cùng ra để bàn giao cho tài xế khác
transferred_order = delivery_orders.pop()

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)
