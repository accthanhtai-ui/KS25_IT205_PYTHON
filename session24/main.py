class PTITStudent:
    #hàm khởi tại thuộc tính
    def __init__(self,name,gpa):
        self.name = name
        self.__gpa = gpa

    #khởi tạo hành vi-method
    def say_hi(self,nick_name):
        print(f"tôi là {self.name} tôi có GPA là {self.__gpa}")
    #yêu cầu tạo method phân loại sinh viên,trên 3.6 là in ra suất sắc ,còn lại khá
    def score_gpa(self):
        if self.__gpa >= 3.6:
            print(f"{self.name} xuất sắc")
        else :
            print(f"{self.name} loại khá")
        
    @property
    def gpa(self):
        return self.__gpa
    
    
student_TX = PTITStudent("thanh tài",3.0)
student_rikkei = PTITStudent("tài ròm",3.6)


student_TX.say_hi('thích chơi đá')
student_rikkei.say_hi('thích hít sì ke')

print(f"sinh viên đại học {student_TX.name}")
