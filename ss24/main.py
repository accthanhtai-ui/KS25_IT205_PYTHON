class PTITStudent:
    # hàm khởi tạo thuộc tính
    def __init__(self, name, GPA):
        self.name = name
        self.__gpa = GPA
    # khởi tạo hành vi - Method
    def say_sound(self, nick_name):
        print(f"Tôi là {self.name} tôi thích bạn nữ tên là {nick_name}")
student_tuxa = PTITStudent("Trọng Nguyên","7.0")
student_doanhnghiep = PTITStudent("Thanh tài","8.0")
student_chinhquy = PTITStudent("NTN","6.0")

student_tuxa.say_sound("nhí cute phô mai hột vịt cút lộn trà trái cây pizza takoyaki")
    # yêu cầu: tạo method để phân loại sinh viên, trên 3.6 in ra xuất sắc, còn lại in ra khá
    
# print(f"Sinh viên {student_tuxa.name} có GPA là: {student_tuxa.gpa}")
# print(f"Sinh viên {student_doanhnghiep.name} có GPA là: {student_doanhnghiep.gpa}")
# print(f"Sinh viên {student_chinhquy.name} có GPA là: {student_chinhquy.gpa}")