# ==============================
# CHƯƠNG TRÌNH QUẢN LÍ BỆNH NHÂN
# ==============================

# Input:
# - Tên bệnh nhân
# - Mã bệnh án
# - Khoa / phòng khám

# Output:
# - Hiển thị phiếu khám bệnh đầy đủ thông tin

# Thuật toán:
# Bước 1: Nhập tên bệnh nhân
# Bước 2: Nhập mã bệnh án
# Bước 3: Nhập khoa/phòng khám
# Bước 4: Hiển thị phiếu khám bệnh
# Bước 5: Thông báo tiếp nhận thành công

print("========= QUẢN LÍ BỆNH NHÂN =========")

# Nhập dữ liệu
name = input("Nhập tên bệnh nhân: ")
patient_id = input("Nhập mã bệnh án: ")
department = input("Nhập khoa/phòng khám: ")

# Hiển thị phiếu khám bệnh
print("\n========== PHIẾU KHÁM BỆNH ==========")
print("Tên bệnh nhân :", name)
print("Mã bệnh án    :", patient_id)
print("Khoa/Phòng    :", department)
print("=====================================")

# Thông báo
print("Tiếp nhận bệnh nhân thành công!")
