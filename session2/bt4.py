# (1) Phân tích & Đề xuất giải pháp
# Phân tích Input / Output
# Input
# Hệ thống yêu cầu nhập 3 thông tin:
# Tuổi (Age) → kiểu số nguyên
# Huyết áp tâm thu (Systolic Blood Pressure) → kiểu số nguyên
# Đường huyết (Blood Sugar) → kiểu số nguyên
# Điều kiện đạt phẫu thuật
# Bệnh nhân chỉ được phẫu thuật khi:
# tuổi dưới 75
# huyết áp từ 90 đến 140
# đường huyết dưới 150
# Phải thỏa mãn tất cả điều kiện cùng lúc.
# Output
# Nếu đạt:
# ĐỦ ĐIỀU KIỆN PHẪU THUẬT
# Nếu không đạt:
# TỪ CHỐI PHẪU THUẬT
# Nếu dữ liệu âm hoặc sai:
# Dữ liệu nhập vào không hợp lệ
# Đề xuất giải pháp
# Giải pháp 1: Gộp điều kiện (Flat Logic)
# Dùng một câu lệnh if chứa tất cả điều kiện bằng toán tử and.
# Ví dụ:
# tuổi < 75
# và huyết áp nằm trong khoảng an toàn
# và đường huyết < 150
# Nếu tất cả đúng thì cho phép phẫu thuật.
# Ưu điểm
# code ngắn
# dễ viết
# phù hợp bài cơ bản
# Nhược điểm
# khó biết bệnh nhân trượt ở điều kiện nào
# thông báo chưa chi tiết
# Giải pháp 2: Điều kiện lồng nhau (Nested If)
# Kiểm tra từng điều kiện theo từng bước.
# Ví dụ:
# kiểm tra tuổi trước
# sau đó mới kiểm tra huyết áp
# cuối cùng kiểm tra đường huyết
# Nếu sai ở bước nào thì báo ngay bước đó.
# Ưu điểm
# dễ kiểm soát logic
# có thể báo lỗi chi tiết
# giống hệ thống y khoa thực tế hơn
# Nhược điểm
# code dài hơn
# nhiều thụt lề hơn
# Bảng so sánh hai giải pháp
# Tiêu chí	Flat Logic	Nested If
# Độ ngắn gọn	Ngắn gọn hơn	Dài hơn
# Độ dễ đọc	Dễ nhìn lúc đầu	Nhiều thụt lề hơn
# Thông báo chi tiết	Khá chung chung	Chi tiết hơn
# Giá trị y khoa	Chỉ biết đạt hay không	Biết bệnh nhân trượt ở đâu
# Kiểm soát logic	Ít linh hoạt	Linh hoạt hơn

# Em chọn giải pháp Nested If.
# Lý do là vì hệ thống y khoa cần kiểm tra từng bước rõ ràng để tránh sai sót.
# Ngoài việc biết bệnh nhân đạt hay không, hệ thống còn có thể cho biết bệnh nhân bị từ chối do tuổi, huyết áp hay đường huyết.
# Tuy code dài hơn một chút nhưng dễ mở rộng và phù hợp với thực tế hơn.
# (2) Triển khai code
print("===== HỆ THỐNG ĐÁNH GIÁ PHẪU THUẬT =====")
try:
    age = int(input("Nhập tuổi bệnh nhân: "))
    blood_pressure = int(input("Nhập huyết áp tâm thu: "))
    blood_sugar = int(input("Nhập đường huyết: "))
    if age < 0 or blood_pressure < 0 or blood_sugar < 0:
        print("Dữ liệu nhập vào không hợp lệ")
    else:
        if age < 75:
            if 90 <= blood_pressure <= 140:
                if blood_sugar < 150:
                    print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
                else:
                    print("TỪ CHỐI PHẪU THUẬT - Đường huyết quá cao")
            else:
                print("TỪ CHỐI PHẪU THUẬT - Huyết áp không an toàn")
        else:
            print("TỪ CHỐI PHẪU THUẬT - Tuổi vượt giới hạn cho phép")
except ValueError:
    print("Dữ liệu nhập vào không hợp lệ")