# (1) Phân tích lỗi (Code Review)
# Lỗi IndexError: tuple index out of range  
# Với Levi, tuple có đủ 3 phần tử (Tên, Số trận, MMR), nên p[2] lấy được MMR. Nhưng với SofM, tuple chỉ có 2 phần tử (Tên, Số trận). Khi chương trình cố lấy p[2], Python báo lỗi vì không tồn tại phần tử thứ 3 → IndexError.

# Nếu dữ liệu SofM được sửa thành đầy đủ, lỗi tiếp theo ở Optimus là gì?  
# Với Optimus, MMR = "N/A". Khi chạy đến dòng int(r), Python không thể ép chuỗi "N/A" thành số nguyên, dẫn đến lỗi ValueError: invalid literal for int() with base 10: 'N/A'.

# Kỹ năng Debug với print("Đang xử lý:", p)  
# Lệnh này giúp ta biết chương trình đang xử lý bản ghi nào trước khi sập. Nhờ đó, dễ dàng xác định dữ liệu gây lỗi (ví dụ: thấy đang xử lý "SofM" thì biết lỗi do thiếu trường MMR).

# Đặt tên biến theo Clean Code

# ds → player_records

# p → record

# t → name

# m → matches

# r → mmr

# b → bonus

# (2) Refactoring + Exception Handling

# Dữ liệu từ API: (Tên, Số trận, MMR)
# Dữ liệu từ API: (Tên, Số trận, MMR)
data = [
    ("Levi", 120, 2500),      
    ("SofM", 150),          
    ("Optimus", 100, "N/A")   
]

def calculate_bonus(matches, mmr):
    return (matches * 10) + (mmr * 0.5)

def process_player_records(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    for record in player_records:
        name = record[0]
        try:
            matches = record[1]
            mmr = record[2]  

           
            mmr = int(mmr)

            bonus = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {name} nhận được {bonus:.1f} RP")

        except IndexError:
            print(f"Tuyển thủ {name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue
        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue
    print("--- HOÀN TẤT ---")

process_player_records(data)
