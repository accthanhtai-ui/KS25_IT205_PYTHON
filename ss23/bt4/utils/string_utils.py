def normalize_student_names(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("--- CHUẨN HÓA TÊN SINH VIÊN ---")

    for r in records:
        name = r["name"]
        name = " ".join(name.strip().split())
        name = name.title()
        r["name"] = name
        print(f"{r['student_id']}: {r['name']}")

    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")