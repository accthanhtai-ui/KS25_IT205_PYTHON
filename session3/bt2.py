# (1) Phân tích lỗi
# Dò luồng thực thi khi nhập số ngày công = 0
# Khi chương trình chạy và nhập:
# working_days = 0
# thì chương trình sẽ kiểm tra điều kiện:
# if working_days <= 0:
# Điều kiện này đúng nên hệ thống in ra cảnh báo:
# CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.
# Nhưng sau đó chương trình vẫn chạy tiếp xuống bên dưới để tính thưởng và gửi email.
# Lúc này:
# bonus_amount = 0 * 200000
# kết quả bằng 0
# nên hệ thống vẫn gửi email chúc mừng nhận thưởng 0 đồng.
# Nguyên nhân lỗi
# Lỗi nằm ở chỗ sau khi vào nhánh cảnh báo, chương trình không dừng lại mà vẫn tiếp tục thực hiện các dòng code phía dưới.
# if chỉ quyết định có chạy khối lệnh bên trong hay không
# sau khi chạy xong, chương trình vẫn tiếp tục đọc các dòng tiếp theo từ trên xuống dưới
# Do đó dù nhân viên không đủ điều kiện, hệ thống vẫn tính thưởng và gửi email.
# Đây là lỗi logic khá phổ biến khi mới học if và vòng lặp.
# (2) Sửa lỗi
# Cách sửa
# Khi phát hiện số ngày công nhỏ hơn hoặc bằng 0 thì hệ thống chỉ nên:
# in cảnh báo
# bỏ qua phần tính thưởng
# chuyển sang nhân viên tiếp theo
# Không được gửi email thưởng trong trường hợp này.
# Có thể dùng:
# continue
# để bỏ qua toàn bộ phần code bên dưới và quay lại vòng lặp tiếp theo.
# Code sau khi sửa
print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")
for employee_number in range(1, 4):
    print("\n--- Đang xử lý nhân viên số", employee_number, "---")
    working_days = int(input("Nhập số ngày công trong tháng: "))
    if working_days <= 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        continue
    bonus_amount = working_days * 200000
    print("=> Đã gửi Email: Chúc mừng nhận được", bonus_amount, "VNĐ tiền thưởng!")
print("\nĐã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")