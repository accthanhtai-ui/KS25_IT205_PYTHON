# Cuối ngày, thủ kho cần đếm số lượng các sản phẩm bị lỗi từ các quầy gửi về.
# Khai báo một biến để lưu trữ Tổng số hàng lỗi (ban đầu bằng 0).
# Sử dụng vòng lặp vô hạn (while True) để yêu cầu người dùng liên tục nhập số lượng hàng lỗi của từng quầy.
# Nếu người dùng nhập vào số -1: Chương trình hiểu là đã thống kê xong, kết thúc vòng lặp bằng lệnh break.
# Nếu người dùng nhập số khác -1: Cộng dồn số lượng đó vào tổng số hàng lỗi.
# Khi thoát vòng lặp, in ra kết quả: "Tổng số hàng lỗi thu hồi trong ngày là: [Tổng]".
defective_goods = 0
total = 0
while True:
    value = int(input('nhập số lượng hàng bị lỗi'))
    if value <= 0:
        print('đã thống kê xong')
        break
    else:
        total+= value
print('tổng hàng lỗi là',total)