print("--- BLOOD DONOR SCREENING SYSTEM ---")

donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

# Hệ thống kiểm tra điều kiện hiến máu
if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")

else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")
   # 1 Phân tích lỗi
# Ở đoạn này chương trình đang dùng or nên bị sai logic.
# Em test với:
# tuổi = 16
# cân nặng = 55
# thì chương trình vẫn báo đủ điều kiện.
# Lý do là vì:
# tuổi 16 → không đủ
# nhưng cân nặng 55 → đủ
# Do dùng or nên chỉ cần đúng một cái là chương trình cho qua luôn.
# Trong khi đi hiến máu thì phải đủ cả tuổi lẫn cân nặng mới được.
# or = chỉ cần đúng 1 điều kiện
# and = phải đúng hết tất cả điều kiện
# Cho nên lỗi nằm ở chỗ dùng sai toán tử logic.
# 2 Sửa lỗi
# Để sửa thì em đổi or thành and.
# Vì quy định hiến máu là:
# từ 18 tuổi trở lên
# cân nặng từ 50kg trở lên
# nên phải đạt cùng lúc cả hai điều kiện.
# Sau khi sửa
# nếu thiếu tuổi hoặc thiếu cân nặng thì hệ thống sẽ báo không đủ điều kiện
# chỉ khi nào đạt đủ cả hai thì mới được hiến máu
# Như vậy chương trình sẽ kiểm tra đúng hơn và không bị cho nhầm những trường hợp chưa đủ điều kiện.