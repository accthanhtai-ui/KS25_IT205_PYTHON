# (1) Phân tích và thiết kế giải pháp
# Phân tích Input / Output
# Input
# Hệ thống yêu cầu HR nhập:
# Mã nhân viên → kiểu chuỗi
# Họ và tên nhân viên → kiểu chuỗi
# Phòng ban công tác → kiểu chuỗi
# Chương trình sẽ lặp lại 3 lần để nhập cho 3 nhân viên.
# Output
# Nếu dữ liệu hợp lệ:
# In ra Phiếu Hồ Sơ Điện Tử gồm:
# Mã nhân viên
# Họ tên
# Phòng ban
# Nếu dữ liệu không hợp lệ:
# Hiển thị cảnh báo lỗi
# Không in phiếu hồ sơ cho nhân viên đó
# Đề xuất giải pháp
# Em sẽ dùng:
# vòng lặp for để nhập 3 nhân viên
# câu lệnh if để kiểm tra dữ liệu hợp lệ
# hàm strip() để kiểm tra trường hợp nhập khoảng trắng
# Nếu:
# mã nhân viên bị trống
# hoặc họ tên bị trống
# hoặc chỉ nhập khoảng trắng
# thì hệ thống sẽ báo lỗi và bỏ qua việc in phiếu.
# Nếu dữ liệu hợp lệ thì mới in hồ sơ.
# Thiết kế thuật toán (Pseudocode)
# Bắt đầu chương trình
# Lặp 3 lần:
#     Nhập mã nhân viên
#     Nhập họ tên
#     Nhập phòng ban

#     Nếu mã nhân viên rỗng
#     hoặc họ tên rỗng
#     hoặc chỉ chứa khoảng trắng:

#         In cảnh báo lỗi
#         Bỏ qua in phiếu

#     Ngược lại:

#         In phiếu hồ sơ điện tử
# Kết thúc chương trình
# (2) Triển khai code
print("===== HỆ THỐNG QUẢN LÝ HỒ SƠ NHÂN VIÊN =====")

for employee_number in range(1, 4):

    print("\n===== NHÂN VIÊN", employee_number, "=====")

    employee_id = input("Nhập mã nhân viên: ")
    employee_name = input("Nhập họ tên nhân viên: ")
    department = input("Nhập phòng ban: ")

    if employee_id.strip() == "" or employee_name.strip() == "":
        print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")

    else:
       
        print("\n===== PHIẾU HỒ SƠ ĐIỆN TỬ =====")
        print("Mã nhân viên:", employee_id)
        print("Họ và tên:", employee_name)
        print("Phòng ban:", department)

print("\nĐã hoàn tất nhập hồ sơ cho 3 nhân viên.")
# Giải thích xử lý Edge Cases
# Trường hợp bỏ trống dữ liệu
# Ví dụ:
# Nhập mã nhân viên:
# không nhập gì rồi Enter.
# Hệ thống sẽ báo lỗi và không in hồ sơ.
# Trường hợp nhập toàn khoảng trắng
# Ví dụ:
# "     "
# Hàm strip() sẽ xóa khoảng trắng.
# Sau khi xóa mà chuỗi rỗng thì hệ thống xem là dữ liệu không hợp lệ.