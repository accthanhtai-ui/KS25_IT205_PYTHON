print("--- EMERGENCY TRIAGE SYSTEM ---")

heart_rate = int(input("Enter patient's heart rate (bpm): "))

if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")

elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")

elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")

else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")

# Phân tích lỗi
# Khi em test với nhịp tim bằng 135 thì chương trình sẽ kiểm tra điều kiện từ trên xuống dưới.
# Đầu tiên chương trình gặp điều kiện nhịp tim lớn hơn 100. Vì 135 lớn hơn 100 nên chương trình chạy luôn vào mức YELLOW.
# Sau khi đã chạy vào một điều kiện đúng thì các điều kiện bên dưới sẽ không được kiểm tra nữa. Vì vậy dù 135 cũng lớn hơn 120 nhưng phần RED đã bị bỏ qua.
# Cấu trúc if-elif-else hoạt động theo kiểu điều kiện nào đúng trước thì chạy trước. Nên thứ tự đặt điều kiện rất quan trọng.
# Lỗi ở đây là do em đặt điều kiện lớn hơn 100 phía trên điều kiện lớn hơn 120. Thành ra các trường hợp nguy hiểm đáng lẽ phải vào RED lại bị xếp nhầm sang YELLOW.
# Như vậy hệ thống sẽ phân loại sai mức độ nguy hiểm của bệnh nhân.
# Sửa lỗi
# Để sửa lỗi này thì em đổi lại thứ tự kiểm tra điều kiện.
# Em sẽ cho chương trình kiểm tra mức nguy hiểm cao nhất trước, rồi mới kiểm tra các mức thấp hơn.
# Tức là
# kiểm tra RED trước
# sau đó mới tới YELLOW
# rồi tới BLUE
# cuối cùng là GREEN
# Làm như vậy thì khi nhập nhịp tim 135, chương trình sẽ nhận ra đây là trường hợp nguy hiểm và đưa vào mức RED ngay.
# Sau khi sửa thì hệ thống sẽ phân loại đúng hơn và tránh bị sai ở những trường hợp nhịp tim quá cao.