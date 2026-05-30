# Input:
# Người dùng nhập số lượng phiếu đăng ký (int)
# Người dùng nhập chuỗi đăng ký theo format:
# Họ tên | Tên khóa học | Mã học viên | Email

# Output:
# In ra phiếu đăng ký đã chuẩn hóa
# Nếu dữ liệu sai -> thông báo lỗi và bỏ qua phiếu

# Giải pháp:
# 1. Kiểm tra số lượng phiếu:
#    nếu <= 0 -> báo lỗi và kết thúc chương trình
#
# 2. Với mỗi phiếu đăng ký:
#    dùng split("|") để tách dữ liệu
#    nếu không đủ 4 phần -> bỏ qua phiếu
#
# 3. Chuẩn hóa dữ liệu:
#    Họ tên: strip() + title()
#    Khóa học: strip() + title()
#    Mã học viên: strip() + upper()
#    Email: strip() + lower()
#
# 4. Kiểm tra dữ liệu hợp lệ:
#    Email phải chứa "@"
#    Mã học viên phải có độ dài >= 5
#
# 5. Tạo mã xác nhận:
#   ghép mã học viên + tên khóa học
#   viết hoa và thay khoảng trắng bằng "-"


# Nhập số lượng phiếu đăng ký
number_of_forms = int(input("Nhập số lượng phiếu đăng ký: "))

if number_of_forms <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")

else:
    for form_index in range(1, number_of_forms + 1):

        print(f"\nNhập phiếu đăng ký thứ {form_index}")

        raw_data = input(
            "Nhập dữ liệu (Họ tên | Khóa học | Mã HV | Email): "
        )

        # TÁCH DỮ LIỆU
        parts = raw_data.split("|")

        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        student_name = parts[0].strip().title()

        course_name = parts[1].strip().title()

        student_code = parts[2].strip().upper()

        email = parts[3].strip().lower()

        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        if len(student_code) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        confirm_course = course_name.upper().replace(" ", "-")

        confirmation_code = f"{student_code}_{confirm_course}"
 
        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")

        print("Học viên:", student_name)

        print("Khóa học:", course_name)

        print("Mã học viên:", student_code)

        print("Email:", email)

        print("Mã xác nhận:", confirmation_code)