# (1) Phân tích & Đề xuất giải pháp
# Phân tích Input / Output
# Input
# Hệ thống yêu cầu HR nhập:
# số lượng nhân sự mới trong tháng
# kiểu dữ liệu: số nguyên
# Output
# Nếu nhập đúng:
# [THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản...
# Nếu nhập sai:
# [LỖI] Số lượng không hợp lệ!
# Đề xuất giải pháp
# Giải pháp 1: Dùng if thông thường

# Kiểm tra:

# nếu số nhập lớn hơn 0 → chấp nhận
# ngược lại → báo lỗi
# Ưu điểm
# code ngắn
# dễ viết
# Nhược điểm
# nếu nhập sai thì chương trình kết thúc luôn
# HR phải chạy lại chương trình
# Giải pháp 2: Dùng vòng lặp validation
# Dùng vòng lặp để bắt nhập lại liên tục cho đến khi dữ liệu hợp lệ.
# Nếu:
# nhập số âm
# nhập số 0
# thì hệ thống sẽ báo lỗi và yêu cầu nhập lại.
# Ưu điểm
# tiện cho người dùng
# đúng yêu cầu nghiệp vụ hơn
# không cần chạy lại chương trình
# Nhược điểm
# code dài hơn một chút
# Bảng so sánh
# Tiêu chí	If thông thường	Validation Loop
# Độ ngắn gọn	Ngắn hơn	Dài hơn
# Dễ hiểu	Dễ	Khó hơn chút
# Trải nghiệm người dùng	Chưa tốt	Tốt hơn
# Xử lý nhập sai	Kết thúc luôn	Bắt nhập lại
# Chốt lựa chọn
# Em chọn giải pháp dùng vòng lặp validation.
# Vì cách này giúp hệ thống hoạt động thực tế hơn.
# Nếu HR nhập sai thì chương trình không bị dừng ngay mà sẽ yêu cầu nhập lại cho đến khi đúng.
# Như vậy sẽ thuận tiện và tránh thao tác lại nhiều lần.
# (2) Triển khai code
print("=== HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ===")
while True:
    new_employee = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))

    if new_employee <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.")
    else:
        print("[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho", new_employee, "nhân sự mới!")
        break
print("=== CHƯƠNG TRÌNH KẾT THÚC ===")
# Giải thích xử lý Edge Cases
# Trường hợp nhập số 0
# Ví dụ:
# 0
# Hệ thống sẽ báo lỗi vì nghiệp vụ yêu cầu số lượng phải lớn hơn 0.
# Trường hợp nhập số âm
# Ví dụ:
# -3
# Hệ thống xem đây là dữ liệu không hợp lệ và yêu cầu nhập lại.