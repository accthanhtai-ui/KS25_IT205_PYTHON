#cách 1
patient_code = input('Nhập mã bệnh nhân: ')
temperature = float(input('Nhập nhiệt độ: '))
heart_rate = int(input('Nhập nhịp tim: '))
print('\n===== THÔNG TIN BỆNH NHÂN =====')
print('Mã bệnh nhân:', patient_code)
print('Nhiệt độ cơ thể:', temperature)
print('Nhịp tim:', heart_rate)
# kiểm tra kiểu dữ liệu
print('\n===== KIỂM TRA KIỂU DỮ LIỆU =====')
print('Kiểu dữ liệu nhiệt độ:', type(temperature))
print('Kiểu dữ liệu nhịp tim:', type(heart_rate))



# cách 2
print('===== HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN =====')
# nhập dữ liệu
patient_code = input('Nhập mã bệnh nhân: ')
temperature_input = input('Nhập nhiệt độ cơ thể: ')
heart_rate_input = input('Nhập nhịp tim: ')
# ép kiểu dữ liệu
temperature = float(temperature_input)
heart_rate = int(heart_rate_input)
# hiển thị thông tin
print('\n===== THÔNG TIN BỆNH NHÂN =====')
print('Mã bệnh nhân:', patient_code)
print('Nhiệt độ cơ thể:', temperature)
print('Nhịp tim:', heart_rate)
# kiểm tra kiểu dữ liệu
print('\n===== KIỂM TRA KIỂU DỮ LIỆU =====')
print('Kiểu dữ liệu nhiệt độ:', type(temperature))
print('Kiểu dữ liệu nhịp tim:', type(heart_rate))