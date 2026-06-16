# I. PHÂN TÍCH KIẾN TRÚC HỆ THỐNG

# Hệ thống được thiết kế theo mô hình package-based Python CLI, gồm 3 tầng:

# data/: chứa dữ liệu đầu vào
# utils/: xử lý logic nghiệp vụ (business logic)
# reports/: xử lý hiển thị + xuất báo cáo
# main.py: điều phối chương trình
# II. PHÂN TÍCH MODULE
# 1. Module: utils/score_utils.py
# Vai trò:

# Xử lý toàn bộ nghiệp vụ liên quan đến điểm số:

# Tính trung bình
# Phân loại học lực
# Xử lý dữ liệu điểm không hợp lệ
# Các hàm chính:
# calculate_average(scores)
# classify_student(average)
# Kiểu import sử dụng:
# import utils.score_utils
# from utils.score_utils import calculate_average
# 2. Module: utils/string_utils.py
# Vai trò:

# Chuẩn hóa dữ liệu chuỗi tên sinh viên.

# Các hàm chính:
# normalize_student_names(records)
# Kiểu import:
# from utils.string_utils import normalize_student_names
# 3. Module: utils/random_utils.py
# Vai trò:

# Sinh mã bài tập ngẫu nhiên theo format yêu cầu.

# Các hàm chính:
# generate_assignment_code()
# Kiểu import:
# import random
# import string
# import utils.random_utils as ru
# 4. Module: reports/report_generator.py
# Vai trò:
# Hiển thị danh sách sinh viên
# Xuất báo cáo học tập ra file
# Các hàm chính:
# display_student_scores(records)
# export_learning_report(records)
# Kiểu import:
# from utils.score_utils import calculate_average, classify_student
# from datetime import datetime
# from colorama import Fore
# 5. Module: main.py
# Vai trò:

# Điều phối luồng chương trình CLI (menu 1–5)

# Hàm chính:
# main()
# Kiểu import:
# from utils.score_utils import *
# from utils.string_utils import normalize_student_names
# from utils.random_utils import generate_assignment_code
# from reports.report_generator import *
# III. PHÂN TÍCH HÀM NGHIỆP VỤ
# 1. Hàm: calculate_average(scores)
# Input:
# scores: list (có thể chứa số hoặc dữ liệu sai)
# Output:
# float (điểm trung bình)
# Module:

# utils/score_utils.py

# Luồng xử lý:
# lọc danh sách scores:
#     chỉ giữ int hoặc float

# nếu danh sách hợp lệ rỗng:
#     return 0

# tổng = sum(valid_scores)
# trung bình = tổng / len(valid_scores)

# return round(trung bình, 2)
# Edge cases bắt buộc:
# scores = [] → return 0
# "chín" hoặc string → bỏ qua
# tất cả invalid → return 0
# 2. Hàm: classify_student(average)
# Input:
# average: float
# Output:
# str
# Module:

# utils/score_utils.py

# Luồng xử lý:
# IF average >= 8.0:
#     return "Giỏi"
# ELIF average >= 6.5:
#     return "Khá"
# ELIF average >= 5.0:
#     return "Trung bình"
# ELSE:
#     return "Yếu"
# 3. Hàm: display_student_scores(records)
# Input:
# records: list[dict]
# Output:
# None (print terminal)
# Module:

# reports/report_generator.py

# Luồng xử lý:
# IF records rỗng:
#     print "Hệ thống chưa có dữ liệu sinh viên"
#     STOP

# FOR từng student:
#     avg = calculate_average(student["scores"])
#     level = classify_student(avg)

#     print:
#         student_id
#         name
#         scores
#         avg (format 2 số lẻ)
#         level
# Dependency bắt buộc:
# calculate_average()
# classify_student()
# 4. Hàm: normalize_student_names(records)
# Input:
# records: list[dict]
# Output:
# list[dict]
# Module:

# utils/string_utils.py

# Luồng xử lý:
# FOR từng student:
#     name = strip()
#     name = split theo nhiều space → join lại 1 space
#     name = title case

# return records
# Edge case:
# nhiều khoảng trắng
# ký tự đầu/cuối dư
# 5. Hàm: generate_assignment_code()
# Input:
# None
# Output:
# str dạng PY-XXXX
# Module:

# utils/random_utils.py

# Luồng xử lý:
# chars = string.ascii_uppercase + string.digits

# code = random.choices(chars, k=4)

# return "PY-" + "".join(code)
# 6. Hàm: export_learning_report(records)
# Input:
# records: list[dict]
# Output:
# file learning_report.txt
# Module:

# reports/report_generator.py

# Luồng xử lý:
# IF records rỗng:
#     print "Hệ thống chưa có dữ liệu sinh viên"
#     STOP

# total = len(records)
# pass_count = số SV có avg >= 5
# fail_count = còn lại

# time = datetime.now()

# open file learning_report.txt

# write:
#     TIME CREATED
#     TOTAL STUDENTS
#     PASS COUNT
#     FAIL COUNT

# close file

# print màu xanh (Fore.GREEN):
#     "Xuất báo cáo thành công"
# Bắt buộc dùng:
# datetime (module chuẩn)
# colorama (third-party)
# 7. Hàm: main()
# Input:
# None
# Output:
# None
# Module:

# main.py

# Luồng xử lý:
# WHILE True:
#     print menu

#     TRY:
#         choice = int(input)

#         CASE 1:
#             display_student_scores()

#         CASE 2:
#             normalize_student_names()

#         CASE 3:
#             generate_assignment_code()

#         CASE 4:
#             export_learning_report()

#         CASE 5:
#             print "Cảm ơn bạn"
#             break

#         DEFAULT:
#             print "Chức năng không hợp lệ"

#     EXCEPT ValueError:
#         print "Chức năng không hợp lệ"
from data.students import student_records

import utils.string_utils as str_utils
from utils.random_utils import generate_assignment_code
from reports.report_generator import display_student_scores, export_learning_report


def main():

    while True:
        print("\n===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====")
        print("1. Xem danh sách sinh viên và điểm trung bình")
        print("2. Chuẩn hóa tên sinh viên")
        print("3. Sinh mã bài tập ngẫu nhiên")
        print("4. Xuất báo cáo học tập")
        print("5. Thoát chương trình")
        print("====================================================")

        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            display_student_scores(student_records)

        elif choice == "2":
            str_utils.normalize_student_names(student_records)

        elif choice == "3":
            generate_assignment_code()

        elif choice == "4":
            export_learning_report(student_records)

        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break

        else:
            print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")


main()