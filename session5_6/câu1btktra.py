# Viết chương trình giúp thủ kho đánh giá nhanh tình trạng của một mặt hàng.
# Yêu cầu người dùng nhập vào Số lượng tồn kho của mặt hàng đó.
# Áp dụng logic phân loại bằng cấu trúc if/elif/else:
# Nếu Số lượng >= 50: In ra thông báo "Tình trạng: Hàng đầy kho".
# Nếu 10 <= Số lượng < 50: In ra thông báo "Tình trạng: Mức an toàn".
# Nếu Số lượng < 10: In ra thông báo "Tình trạng: Sắp hết hàng, cần báo cá	o nhập thêm".
quantity_stock = int(input('nhập vào số lượng tồn kho của mặt hàng'))
if quantity_stock >= 50:
    print('Tình trạng: Hàng đầy kho')
elif 10 <= quantity_stock and quantity_stock < 50:
    print('Tình trạng: Mức an toàn')
else:
    print('Tình trạng: Sắp hết hàng, cần báo cá	o nhập thêm')