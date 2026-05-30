transaction = " nguyEn vAn a | PYTHON-01 | 15000000 | paid "

transaction = transaction.strip()

parts = transaction.split("|")

student_name = parts[0].strip().title()
course_code = parts[1].strip().upper()
amount = int(parts[2].strip())
status = parts[3].strip().upper()

print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", f"{amount:,}", "VND")
print("Trạng thái:", status)


#  PHÂN TÍCH LỖI 
# 1. Vì sao transaction.strip() không làm thay đổi trực tiếp chuỗi ban đầu?
# Vì strip() chỉ tạo ra chuỗi mới đã xóa khoảng trắng,
# nhưng không tự thay đổi dữ liệu cũ.
# Nếu không gán lại:
# transaction = transaction.strip()
# thì transaction vẫn giữ nguyên giá trị ban đầu.

# 2. Chuỗi giao dịch thực tế được phân tách bằng ký tự nào?
# Chuỗi giao dịch được ngăn cách bằng dấu |

# 3. Vì sao transaction.split("-") là sai?
# Vì chương trình đang tách bằng dấu -
# trong khi dữ liệu thật được ngăn cách bằng dấu |
# nên việc chia dữ liệu bị sai.

# 4. Sau khi tách sai delimiter, dữ liệu trong parts bị lệch như thế nào?
# Ví dụ transaction.split("-") sẽ làm:
# "PYTHON-01" bị cắt thành "PYTHON" và "01"
# làm số lượng phần tử bị lệch.
# Khi lấy parts[2], parts[3]
# dữ liệu có thể sai hoặc gây lỗi.

# 5. Vì sao cần .strip() lại từng phần sau khi split()?
# Vì sau khi tách bằng dấu |
# các dữ liệu thường còn khoảng trắng ở đầu hoặc cuối.
# cần strip() để xóa khoảng trắng cho dữ liệu sạch hơn.

# 6. Vì sao cần chuyển amount từ chuỗi sang số trước khi định dạng tiền?
# Vì amount lấy từ split() là kiểu chuỗi (string),
# chưa phải số.
# Muốn format tiền hoặc tính toán thì phải đổi sang số bằng int().