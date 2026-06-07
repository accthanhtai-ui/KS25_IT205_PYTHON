student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]

def calculate_average(student):
    return (student["math"] + student["physics"] + student["chemistry"]) / 3
def get_rank(average_score):
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    return "Yếu"

def validate_score(score):
    try:
        score = float(score)
        if 0 <= score <= 10:
            return True
        return False
    except ValueError:
        return False
def find_student_by_id(records, student_id):
    for index, student in enumerate(records):
        if student["student_id"] == student_id:
            return index
    return -1
def display_grades(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")
    for index, student in enumerate(records, start=1):
        average = calculate_average(student)
        rank = get_rank(average)

        print(f"{index}. [{student['student_id']}] {student['name']} | Toán: {student['math']} | Lý: {student['physics']} | Hóa: {student['chemistry']} | ĐTB: {average:.2f} - {rank}")
    print("---------------------------")
def update_student_score(records):
    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    index = find_student_by_id(records, student_id)
    if index == -1:
        print(f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!")
        return
    while True:
        subject_choice = input("Chọn môn học (1-Toán, 2-Lý, 3-Hóa): ").strip()
        if subject_choice in ["1", "2", "3"]:
            break
        print("Lựa chọn môn học không hợp lệ!")
    while True:
        new_score = input("Nhập điểm mới: ")
        if validate_score(new_score):
            new_score = float(new_score)
            break

        print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
    subject_map = {"1": "math", "2": "physics", "3": "chemistry"}
    subject_name = {"1": "Toán", "2": "Lý", "3": "Hóa"}

    records[index][subject_map[subject_choice]] = new_score
    print(f">> Đã cập nhật điểm {subject_name[subject_choice]} của sinh viên '{records[index]['name']}' thành {new_score}.")
def generate_report(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    total_students = len(records)
    passed_students = 0
    failed_students = 0
    for student in records:
        average = calculate_average(student)
        if average >= 5.0:
            passed_students += 1
        else:
            failed_students += 1
    passed_percent = (passed_students / total_students) * 100
    failed_percent = (failed_students / total_students) * 100
    print("\n--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số lượng qua môn (ĐTB >= 5.0): {passed_students} sinh viên (Chiếm {passed_percent:.2f}%)")
    print(f"Số lượng trượt (ĐTB < 5.0): {failed_students} sinh viên (Chiếm {failed_percent:.2f}%)")
    print("----------------------")
def find_valedictorian(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    top_student = records[0]
    highest_average = calculate_average(top_student)
    for student in records:
        average = calculate_average(student)
        if average > highest_average:
            highest_average = average
            top_student = student
    print("\n--- VINH DANH THỦ KHOA ---")
    print(f"Sinh viên: {top_student['name']} (Mã: {top_student['student_id']})")
    print(f"Điểm Trung Bình: {highest_average:.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")
    print("--------------------------")
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
    print("1. Xem bảng điểm và học lực")
    print("2. Cập nhật điểm thi sinh viên")
    print("3. Báo cáo thống kê (Đỗ/Trượt)")
    print("4. Tìm sinh viên Thủ khoa")
    print("5. Thoát chương trình")
    print("======================================================")
    choice = input("Chọn chức năng (1-5): ").strip()
    match choice:
        case "1":
            display_grades(student_records)
        case "2":
            update_student_score(student_records)
        case "3":
            generate_report(student_records)
        case "4":
            find_valedictorian(student_records)
        case "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")