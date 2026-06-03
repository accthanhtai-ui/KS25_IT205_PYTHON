# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyen Van An",
    "department": "Python Backend",
    "status": "probation"
}
# Dictionary co 4 key: employee_id, full_name, department, status

# employee[0] gay loi KeyError vi dictionary khong dung index so nguyen
# Dictionary truy cap bang key, phai viet employee["employee_id"]
employee_id = employee["employee_id"]

# employee["name"] gay loi KeyError vi key "name" khong ton tai trong dictionary
# Key dung de lay ho ten la "full_name"
full_name = employee["full_name"]

# employee["employee_status"] = "official" tao them 1 key moi ten "employee_status"
# khong cap nhat duoc gi vi key trang thai trong dictionary la "status"
employee["status"] = "official"

# employee.append() gay loi vi dictionary khong co phuong thuc append()
# append() chi dung cho list, muon them key moi vao dictionary thi gan truc tiep
employee["base_salary"] = 15000000

# del employee["team"] gay loi KeyError vi key "team" khong ton tai
# Key chua thong tin phong ban la "department"
del employee["department"]

print("Ma nhan vien:", employee_id)
print("Ho ten nhan vien:", full_name)
print("Thong tin nhan vien sau xu ly:", employee)