# Phân tích lỗi
# Sau khi chạy:
# python
# express_orders.insert(0, "GE100-FAST")
# → "GE100-FAST" được chèn vào đầu danh sách, các phần tử cũ dịch sang phải. Danh sách thành:
# ["GE100-FAST", "GE101", "GE102-WRONG", "GE103-CANCEL", "GE104"].
# Vì sao sửa nhầm đơn hàng "GE101"?
# python
# express_orders[1] = "GE102-UPDATED"
# Sau khi chèn "GE100-FAST", "GE102-WRONG" nằm ở index 2, còn index 1 là "GE101". Vì vậy lệnh này sửa nhầm "GE101".
# Sau khi chèn "GE100-FAST", "GE102-WRONG" nằm ở đâu?  
# → Index 2.
# Vì sao dòng sau không xóa đúng đơn hàng bị hủy?
# python
# express_orders.pop(3)
# → pop(3) xóa phần tử ở vị trí index 3, nhưng sau khi chèn "GE100-FAST", index 3 lại là "GE103-CANCEL" chỉ khi chưa thêm GE104. Nhưng vì đã thêm "GE104" trước đó, "GE103-CANCEL" nằm ở index 3, "GE104" ở index 4. Tuy nhiên dùng pop() không rõ ràng, dễ gây nhầm lẫn. Đúng ra phải dùng remove("GE103-CANCEL").

# Muốn xóa đúng đơn hàng "GE103-CANCEL":
# python
# express_orders.remove("GE103-CANCEL")
# Phương thức pop() không truyền index:  
# → Lấy phần tử cuối cùng trong danh sách.
# Vì sao lấy sai đơn hàng đang giao?
# python
# current_order = express_orders.pop()
# → Vì pop() mặc định lấy phần tử cuối cùng, nên lấy "GE104" thay vì "GE100-FAST".
# Muốn lấy đơn hàng đầu tiên để giao:
# python
# current_order = express_orders.pop(0)
# Muốn chương trình cho ra kết quả đúng, cần sửa:
# Sửa "GE102-WRONG" ở index 2.
# Xóa "GE103-CANCEL" bằng remove().
# Lấy đơn hàng đầu tiên bằng pop(0).

# Danh sách đơn hàng ban đầu
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
express_orders.append("GE104")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
express_orders.insert(0, "GE100-FAST")

# Sửa mã đơn hàng bị nhập sai (GE102-WRONG -> GE102-UPDATED)
# Sau khi chèn GE100-FAST, GE102-WRONG nằm ở index 2
express_orders[2] = "GE102-UPDATED"

# Xóa đơn hàng bị khách hủy
express_orders.remove("GE103-CANCEL")

# Lấy đơn hàng đầu tiên ra để bắt đầu giao
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)
