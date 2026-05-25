#bài tập sữa lại
print('hệ thống nhập chỉ số sinh tồn');
name_patient = str(input('nhập tên'));
#lỗi là ở đây do không có float trong phần nhập để ràng buộc dữ liệu số thực
weight = float(input('nhập cân nặng'));
print('kiểm tra dữ liệu');
print('tên bệnh nhân',name_patient);
print('cân nặng',weight);

print('kiểu dư liệu đang lưu là',type(weight));