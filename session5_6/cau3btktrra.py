# Mô phỏng chức năng xuất kho an toàn. Giả sử mặt hàng "Bàn phím cơ" đang có Tồn kho = 100.
# Khai báo biến ton_kho = 100.
# Sử dụng vòng lặp while để yêu cầu thủ kho nhập vào Số lượng muốn xuất.
# Ràng buộc dữ liệu (Validation):
# Nếu số lượng xuất < 0: Báo lỗi "Không được nhập số âm, vui lòng nhập lại!" (Vòng lặp tiếp tục).
# Nếu số lượng xuất > ton_kho: Báo lỗi "Kho không đủ hàng, vui lòng nhập lại!" (Vòng lặp tiếp tục).
# Nếu nhập số lượng hợp lệ (từ 0 đến 100):
# Trừ đi tồn kho hiện tại.
# In ra thông báo "=> Xuất kho thành công!".
# In ra "Tồn kho còn lại: [Số lượng còn]".
# Thoát khỏi vòng lặp (Sử dụng lệnh break).

ton_kho = 100
while True:
    export = int(input('nhập số lượng bạn muốn xuất'))
    if export < 0:
        print('không được nhập số âm vui lòng nhập lại')
    elif export > ton_kho :
        print('số bạn nhập lớn hơn số lượng tồn kho')
    else:
        ton_kho-=export
        break
print('xuất kho thành công',ton_kho)