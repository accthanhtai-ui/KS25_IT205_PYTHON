class Student:
    def __init__(self, id, name, theory_score, practice_score, project_score):
        self.__id = id
        self.__name = name
        self.__theory_score = theory_score
        self.__practice_score = practice_score
        self.__project_score = project_score
        self.__final_score = 0
        self.__academic_rank = "Chưa có cập nhật"

    def calculate_final_score(self):
        self.__final_score == (self.__theory_score * 0.2) + (self.__practice_score * 0.3) + (self.__project_score * 0.5)

    def classify_academic_rank(self):
        if (self.__final_score < 0 or self.__final_score > 10):
            print("Điểm tổng kết hiện tại không hợp lệ!")
            return
        if self.__final_score < 5:
            self.__academic_rank = "Yếu"
        if self.__final_score < 7:
            self.__academic_rank = "Trung Bình"
        if self.__final_score < 8.5:
            self.__academic_rank = "Khá"
        else: self.__academic_rank = "Giỏi"

        @property
        def id(self):
            return self.__id
        @property
        def name(self):
            return self.__name
        @property
        def theory_score(self):
            return self.__theory_score
        @property
        def practice_score(self):
            return self.__practice_score
        @property
        def project_score(self):
            return self.__project_score
        @property
        def final_score(self):
            return self.__final_score
        @property
        def acadimic_score(self):
            return self.__acadimic_score

class StudentManager:
    def __init__(self):
        self.students: list[Student] = []

    def add_student(self):
        while True:
            student_id = input("Nhập mã sinh viên: ")
            if not student_id:
                print("ID sinh viên không được để trống!")
                continue

            for value in self.students:
                if value.id == student_id:
                    print("Mã sinh viên đã tồn tại!")
                    return
            break

        while True:
            student_name = input("Nhập tên sinh viên: ")
            if not student_name:
                print("Tên sinh viên không được để trống!")
                continue
            break

        while True:
            student_theory_score = float(input("Nhập điểm lý thuyết: "))
            student_practice_score = float(input("Nhập điểm thực hành: "))
            student_project_score = float(input("Nhập điểm đồ án: "))
            if not (student_theory_score or student_practice_score or student_project_score):
                print("Các điểm của sinh viên không được để trống!")
                continue
            break

        new_student = Student(student_id, student_name, student_theory_score, student_practice_score, student_practice_score, student_project_score)
        new_student.caculate_final_score()
        new_student.classify_academic_rank()

        print("Thêm sinh viên thành công!")

  