student_name = " nguYEn vAn a "
student_code = " rk-001-python "
email = " Student01@GMAIL.COM "

student_name = student_name.strip()
student_name = student_name.title()

student_code = student_code.strip()
student_code = student_code.upper()

email = email.strip()
email = email.lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)


#  PHÂN TÍCH LỖI 
# 1. Vì sao student_name.strip() không làm thay đổi trực tiếp biến student_name?
# Vì strip() chỉ xử lý chuỗi rồi trả về kết quả mới,
# nhưng chương trình chưa gán lại vào biến student_name
# nên giá trị cũ vẫn giữ nguyên.

# 2. Vì sao student_name.title() không tạo ra kết quả "Nguyen Van A"?
# Vì title() chỉ tạo chuỗi mới viết hoa chữ cái đầu,
# nhưng không lưu lại vào student_name
# nên khi in ra vẫn là dữ liệu cũ.

# 3. Vì sao student_code.upper() không làm mã học viên chuyển thành chữ hoa?
# Vì upper() chỉ chuyển thành chữ hoa tạm thời,
# nếu không gán lại vào student_code thì biến sẽ không thay đổi.

# 4. Vì sao email.lower() không làm email chuyển thành chữ thường?
# Vì lower() chỉ trả về chuỗi mới viết thường,
# nhưng chưa được lưu lại nên email vẫn giữ nguyên.

# 5. Muốn các phương thức xử lý chuỗi có hiệu lực cần làm gì?
# Cần gán kết quả lại vào biến.
