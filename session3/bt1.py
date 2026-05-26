# (1) Phân tích lỗi
# Dò luồng thực thi chương trình
# Ban đầu chương trình chạy vòng lặp để nhập lương cho 3 nhân viên.
# Nhưng bên trong vòng lặp lại có dòng:
# total_budget = 0
# Điều này làm cho mỗi lần lặp mới thì biến total_budget lại bị reset về 0.
# Ví dụ chạy thử:
# Lần 1
# total_budget = 0
# nhập lương 5 triệu
# total_budget = 0 + 5 triệu
# kết quả lúc này = 5 triệu
# Lần 2
# total_budget lại bị gán về 0
# nhập lương 4 triệu
# total_budget = 4 triệu
# => mất luôn 5 triệu trước đó.
# Lần 3
# total_budget tiếp tục bị reset
# nhập 6 triệu
# total_budget = 6 triệu
# Nên cuối cùng chương trình chỉ giữ lương của người nhập cuối cùng.
# Nguyên nhân lỗi
# Lỗi nằm ở chỗ đặt biến total_budget = 0 bên trong vòng lặp.
# Biến tổng chỉ nên khởi tạo một lần trước khi lặp.
# Nếu đặt trong vòng lặp thì mỗi lần chạy sẽ xóa hết dữ liệu cũ và tính lại từ đầu.
# Đây là lỗi rất thường gặp khi mới học vòng lặp và cộng dồn dữ liệu.
# (2) Sửa lỗi
# Cách sửa
# Đưa dòng:
# total_budget = 0
# ra ngoài vòng lặp.
# Như vậy biến tổng sẽ được giữ lại trong suốt quá trình nhập dữ liệu.
# Mỗi lần nhập lương mới, chương trình sẽ cộng tiếp vào giá trị cũ thay vì xóa đi.
# Code sau khi sửa
print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")
total_budget = 0

for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)
    salary = int(input("Nhập mức lương (VND): "))
    total_budget = total_budget + salary
print("=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VND")