danh_sach_xe = [
    {
        "ma_cx": "CX001",
        "tuyen": "Sai Gon - Da Lat",
        "gia_ve": 300000,
        "ghe_trong": 5,
        "tong_ghe": 40,
        "doanh_thu": 10500000,
        "trang_thai": "Hut khach"
    },
    {
        "ma_cx": "CX002",
        "tuyen": "Sai Gon - Nha Trang",
        "gia_ve": 250000,
        "ghe_trong": 40,
        "tong_ghe": 40,
        "doanh_thu": 0,
        "trang_thai": "E khach"
    }
]

def lay_trang_thai(ghe_trong, tong_ghe):
    if ghe_trong == 0:
        return "Het ve"
    ty_le = (ghe_trong / tong_ghe) * 100
    if ty_le < 15:
        return "Hut khach"
    elif ty_le <= 80:
        return "Binh thuong"
    else:
        return "E khach"

def hien_thi_danh_sach(danh_sach):
    if len(danh_sach) == 0:
        print("-> Danh sach chuyen xe dang trong!")
        return
    print("\n" + "="*95)
    print("Ma CX | Tuyen duong           | Gia ve   | Trong/Tong | Doanh thu   | Trang thai")
    for xe in danh_sach:
        ghe_info = str(xe["ghe_trong"]) + "/" + str(xe["tong_ghe"])
        print(f"{xe['ma_cx']:<5} | {xe['tuyen']:<21} | {xe['gia_ve']:<8} | {ghe_info:<10} | {xe['doanh_thu']:<11} | {xe['trang_thai']}")
    print("="*95 + "\n")

def them_chuyen_xe():
    print("\n--- THEM CHUYEN XE MOI ---")
    ma = input("Nhap Ma CX: ").strip()
    if ma == "":
        print("-> Loi: Ma khong duoc de trong!")
        return
    for xe in danh_sach_xe:
        if xe["ma_cx"] == ma:
            print("-> Loi: Ma xe da ton tai!")
            return
            
    tuyen = input("Nhap Tuyen duong: ").strip()
    if tuyen == "":
        print("-> Loi: Tuyen duong khong de trong!")
        return
        
    gia = float(input("Nhap Gia ve: "))
    tong_so_ghe = int(input("Nhap Tong so ghe: "))
    if gia <= 0 or tong_so_ghe <= 0:
        print("-> Loi: Gia ve va ghe phai lon hon 0!")
        return
        
    chuyen_xe_moi = {
        "ma_cx": ma,
        "tuyen": tuyen,
        "gia_ve": gia,
        "ghe_trong": tong_so_ghe,
        "tong_ghe": tong_so_ghe,
        "doanh_thu": 0,
        "trang_thai": lay_trang_thai(tong_so_ghe, tong_so_ghe)
    }
    danh_sach_xe.append(chuyen_xe_moi)
    print("-> Them thanh cong!")

def dat_ve():
    print("\n--- DAT VE ---")
    ma = input("Nhap Ma CX muon dat: ").strip()
    xe_tim_thay = None
    for xe in danh_sach_xe:
        if xe["ma_cx"] == ma:
            xe_tim_thay = xe
            break
            
    if xe_tim_thay is None:
        print("-> Loi: Khong tim thay Ma CX!")
        return
        
    so_ve = int(input("Nhap so luong ve: "))
    if so_ve <= 0 or so_ve > xe_tim_thay["ghe_trong"]:
        print("-> Loi: So ve khong hop le hoac khong du ghe!")
        return
        
    xe_tim_thay["ghe_trong"] -= so_ve
    so_ghe_da_ban = xe_tim_thay["tong_ghe"] - xe_tim_thay["ghe_trong"]
    xe_tim_thay["doanh_thu"] = xe_tim_thay["gia_ve"] * so_ghe_da_ban
    xe_tim_thay["trang_thai"] = lay_trang_thai(xe_tim_thay["ghe_trong"], xe_tim_thay["tong_ghe"])
    print("-> Dat ve thanh cong!")

def huy_chuyen_xe():
    print("\n--- HUY CHUYEN XE ---")
    ma = input("Nhap Ma CX can xoa: ").strip()
    vi_tri = -1
    for i in range(len(danh_sach_xe)):
        if danh_sach_xe[i]["ma_cx"] == ma:
            vi_tri = i
            break
            
    if vi_tri == -1:
        print("-> Loi: Khong tim thay Ma CX!")
        return
        
    xac_nhan = input("Ban co chac muon xoa? (Y/N): ")
    if xac_nhan in ["Y", "y"]:
        danh_sach_xe.pop(vi_tri)
        print("-> Da xoa thanh cong!")
    else:
        print("-> Da huy xoa.")



def thong_ke_trang_thai():
    print("\n--- THONG KE ---")
    thong_ke = {"Het ve": 0, "Hut khach": 0, "Binh thuong": 0, "E khach": 0}
    for xe in danh_sach_xe:
        tt = xe["trang_thai"]
        thong_ke[tt] += 1
    for k, v in thong_ke.items():
        print(f"* {k}: {v}")

while True:
    print("\n======= MENU =======")
    print("1. Danh sach chuyen xe")
    print("2. Them chuyen xe")
    print("3. Dat ve")
    print("4. Huy chuyen xe")
    print("5. Tim kiem")
    print("6. Thong ke")
    print("8. Thoat")
    print("====================")
    
    lua_chon = input("Chon (1-8): ").strip()
    
    match lua_chon:
        case "1":
            hien_thi_danh_sach(danh_sach_xe)
        case "2":
            them_chuyen_xe()
        case "3":
            dat_ve()
        case "4":
            huy_chuyen_xe()
        case "5":
            print('em chưa xong')
        case "6":
            thong_ke_trang_thai()
        case "8":
            print("-> Tam biet!")
            break
        case _:
            print("-> Nhap lai tu 1 den 8!")