# (1) Phân tích và thiết kế giải pháp
# Phân tích Input / Output
# Input
# Hệ thống yêu cầu lễ tân nhập:
# Họ và tên bệnh nhân → kiểu chuỗi
# Tuổi bệnh nhân → kiểu số nguyên
# Output
# Nếu dữ liệu hợp lệ:
# In phiếu khám gồm:
# Họ tên
# Tuổi
# Kết quả phân luồng
# Nếu dữ liệu không hợp lệ:
# In thông báo lỗi
# Kết thúc chương trình
# Không in phiếu khám
# Đề xuất giải pháp
# Đầu tiên hệ thống sẽ kiểm tra dữ liệu nhập vào trước.
# Kiểm tra:
# tên có bị bỏ trống hay chỉ chứa khoảng trắng không
# tuổi có nhỏ hơn 0 hoặc lớn hơn 150 không
# Nếu dữ liệu sai:
# báo lỗi ngay
# không cho phân luồng
# Nếu dữ liệu đúng:
# dùng if-elif-else để phân loại bệnh nhân theo độ tuổi
# Phân luồng:
# dưới 6 tuổi → bệnh nhi
# từ 80 tuổi trở lên → người cao tuổi
# còn lại → khám thường
# Thiết kế thuật toán
# Pseudocode
# Bắt đầu chương trình
# Nhập họ tên
# Nhập tuổi
# Nếu tên rỗng hoặc chỉ chứa khoảng trắng
#     In lỗi
#     Kết thúc
# Nếu tuổi < 0 hoặc tuổi > 150
#     In lỗi
#     Kết thúc
# Nếu tuổi < 6
#     Phân luồng bệnh nhi
# Ngược lại nếu tuổi >= 80
#     Phân luồng người cao tuổi
# Ngược lại
#     Phân luồng khám thường
# In phiếu khám
# Kết thúc chương trình
print("===== HỆ THỐNG TIẾP NHẬN BỆNH NHÂN =====")
patient_name = input("Nhập họ và tên bệnh nhân: ")
try:
    patient_age = int(input("Nhập tuổi bệnh nhân: "))
    if patient_name.strip() == "" or patient_age < 0 or patient_age > 150:
        print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
        exit()
    if patient_age < 6:
        result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
    elif patient_age >= 80:
        result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
    else:
        result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."
    print("\n===== PHIẾU KHÁM BỆNH =====")
    print("Họ tên:", patient_name)
    print("Tuổi:", patient_age)
    print("Kết quả phân luồng:", result)
except:
    print("LỖI: Tuổi phải là số nguyên!")