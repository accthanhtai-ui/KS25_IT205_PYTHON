# (1) Phân tích lỗi (Code Review)
# Vì sao xuất hiện ZeroDivisionError?  
# Khi xử lý tuyển thủ ShowMaker, biến deaths = "0". Sau khi ép kiểu thành số nguyên, ta có int(deaths) = 0. Công thức KDA (kills + assists) / deaths trở thành phép chia cho 0, gây ra lỗi ZeroDivisionError: division by zero. Python không cho phép chia cho 0 nên chương trình sập ngay tại đây.

# Nếu xóa ShowMaker, lỗi gì xảy ra với Chovy?  
# Với Chovy, dữ liệu deaths = "ba". Khi gọi int("ba"), Python không thể chuyển đổi chuỗi "ba" thành số nguyên, dẫn đến lỗi ValueError: invalid literal for int() with base 10: 'ba'.

# Đánh giá cách đặt tên biến  
# Các biến ds, x, n, k, d, a đều viết tắt, khó hiểu, không tự giải thích. Theo chuẩn Clean Code, nên đổi thành:

# ds → player_stats_list

# x → player_stats

# n → name

# k → kills

# d → deaths

# a → assists

# Lợi ích của việc tách hàm calculate_kda

# Giúp tái sử dụng công thức KDA nhiều nơi mà không cần viết lại (nguyên tắc DRY).

# Dễ dàng bảo trì: nếu công thức thay đổi, chỉ cần sửa trong một hàm.

# Code trở nên rõ ràng và module hóa, dễ đọc và dễ test.

# (2) Refactoring + Exception Handling


data = [
    ("Faker", "10", "2", "8"),      
    ("ShowMaker", "15", "0", "10"), 
    ("Chovy", "12", "ba", "5")      
]


def calculate_kda(kills, deaths, assists):
    return (kills + assists) / deaths


def process_player_stats(player_stats_list):
    print("--- BẢNG XẾP HẠNG KDA ---")
    for player_stats in player_stats_list:
        name, kills, deaths, assists = player_stats
        try:
            kills = int(kills)
            deaths = int(deaths)
            assists = int(assists)

            kda = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda:.2f}")

        except ZeroDivisionError:
            print(f"Tuyển thủ{name}: KDA Hoàn hảo (Perfect Game)!")
            continue
        except ValueError:
            print(f"{name}: Lỗi dữ liệu không hợp lệ!")
            continue
process_player_stats(data)