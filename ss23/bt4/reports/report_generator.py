from datetime import datetime
from colorama import Fore, init

from utils.score_utils import calculate_average, classify_student

init(autoreset=True)


def display_student_scores(records):

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("--- DANH SÁCH ĐIỂM SINH VIÊN ---")

    for i, r in enumerate(records, 1):
        avg = calculate_average(r["scores"])
        level = classify_student(avg)

        print(f"{i}. [{r['student_id']}] {r['name']} | Điểm: {r['scores']} | ĐTB: {avg:.2f} - {level}")

    print("---------------------------------")


def export_learning_report(records):

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total = len(records)
    pass_count = 0
    fail_count = 0

    for r in records:
        avg = calculate_average(r["scores"])
        if avg >= 5.0:
            pass_count += 1
        else:
            fail_count += 1

    report = f"""===== LEARNING REPORT =====
Created: {datetime.now()}

Total students: {total}
Passed (>=5.0): {pass_count}
Need improvement (<5.0): {fail_count}
"""

    with open("learning_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(f"Tổng số sinh viên: {total}")
    print(f"Số sinh viên đạt yêu cầu: {pass_count}")
    print(f"Số sinh viên cần cải thiện: {fail_count}")

    print(Fore.GREEN + ">> Đã xuất báo cáo ra file learning_report.txt")