product_info = ("SP001", "Áo polo nam", "Size L", 299000)
# Tuple có 4 phần tử, đánh số index từ 0

# product_info[1] lấy "Áo polo nam" (index 1), không phải mã SP
# "SP001" nằm ở index 0
product_code = product_info[0]

# product_info[2] lấy "Size L" (index 2), không phải tên SP
# "Áo polo nam" nằm ở index 1
product_name = product_info[1]

# product_info.length() tuple không có method .length()
# Phải dùng hàm len() có sẵn của Python
product_length = len(product_info)

# product_info[3] = 279000 tuple không cho phép sửa trực tiếp
# Tạo tuple mới: giữ 3 phần tử đầu, ghép thêm giá mới vào sau
updated_product_info = product_info[:3] + (279000,)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", updated_product_info)