def menu():
    print("=" * 50)
    print("1. Hiển thị danh sách cầu thủ\n" +
          "2. Tiếp nhận cầu thủ mới\n" +
          "3. Cập nhật thông tin và chỉ số\n" +
          "4. Xóa cầu thủ\n" +
          "5. Tìm kiếm cầu thủ\n" +
          "6. Thống kê loại phong độ\n" +
          "7. Đánh giá phong độ tự động\n" +
          "8. Thoát!")
    print("=" * 50)
    print()


def display_CT(players):
    if not players:
        print('danh sách cầu thủ đang trống!')
    print('========danh sách cầu thủ========')
    print(f"{'Mã CT':<5}|{'họ tên':<25}|{'số trận':<15}|{'số bàn ghi':<15}|{'số kiến tạo':<15}|{'hiệu suất':<15}|{'phân loại':<15}")
    for CT in players:
        print(f"{CT.get('id'):<5}|{CT.get('name'):<25}|{CT.get('match'):<15}|{CT.get('goal'):<15}|{CT.get('assist'):<15}|{CT.get('perform','chưa tính toán'):<15}|{CT.get('rank','chưa tính toán'):<15}")


def validate_input(prompt : str,type: str = 'str'):
    while True:
        value = input(prompt)
        if not value:
            print('không được để trống lệnh gọi ,nhập lại')
            continue

        if type == 'int':
            try:
                value_int = int(value)
                if value_int < 0:
                    print('vui lòng nhập số nguyên dương')
                    continue
                return value_int
            
            except ValueError:
                print('dư liệu sai nhập lại!')
                continue

        if type == 'match':
            try:
                value_match = int(value)
                if value_match < 0 or value_match >50:
                    print('nhập trong vòng 0-50 , nhập lại')
                    continue
                return value_match
            except ValueError:
                print('dư liệu sai nhập lại!')
                continue
        return value



def add_CT(players):
    while True:
        id_input = validate_input('nhập mã cầu thủ: ')
        for CT in players:
            if id_input.lower() == CT.get('id').lower():
                print('cầu thủ này đã tồn tại,nhập lại')
                continue
        else:
            name_input = validate_input('nhập tên cầu thủ: ')
            match_input = validate_input('nhập số trận đấu: ','match')
            goal_input = validate_input('nhập vào số bàn ghi: ','int')
            assist_input = validate_input('nhập vào số kiến tạo: ','int')
            perform_new = (match_input*1)+(goal_input*3)+(assist_input*2)
            rank_new = set_rank(perform_new)
            list_new={
                "id":id_input,
                "name":name_input,
                "match":match_input,
                "goal":goal_input,
                "assist":assist_input,
                "perform":perform_new,
                "rank":rank_new
            }
            players.append(list_new)
            print('thêm thành công')
            break

def update_CT(players):
    id_update = input('nhập vào mã id cầu thủ cần cập nhật: ')
    for player in players:
        if id_update.lower() == player.get("id").lower():
            print('có tồn tại tiến hành cập nhật')

            match_new = validate_input('nhập vào số trận mới: ','match')
            goal_new = validate_input('nhập số bàn ghi mới: ','int')
            assist_new = validate_input('nhập vào số kiến tạo mới: ','int')
            perform_new = (match_new*1)+(goal_new*3)+(assist_new*2)
            rank_new = set_rank(perform_new)
            player["match"]=match_new
            player["goal"]=goal_new
            player["assist"]=assist_new
            player["perform"]=perform_new
            player["rank"]=rank_new
            print('đã cập nhật thành công')
            break
def remove_CT(players):
    if not players:
        print('danh sách đang rỗng')
        return
    id_del = validate_input('nhập vào  id hoặc tên cầu thủ bạn muốn xóa: ')
    for player in players:
        if id_del.lower() == player.get("id").lower() or id_del.lower() == player.get("name").lower():
            players.remove(player)
            print('đã thanh lý')
            break
    else:
        print('không tìm thấy cầu thủ')

def search_CT(players):
    if not players:
        print('danh sách bị rỗng vui lòng nhập vào: ')
        return
    input_id = validate_input('nhập id/tên Cầu thủ cần tìm: ')
    find = []
    for player in players:
        if input_id.lower() == player.get("id").lower() or input_id.lower() == player.get("name").lower():
            find.append(player)
            break
    if not find:
        print('không tìm thấy cầu thủ cần tìm!')
    else:
        display_CT(find)
        
def set_rank(perform_new):
    if perform_new < 15:
        return "cần thanh lý"
    elif perform_new < 30:
        return "Dự bị chiến lược"
    elif perform_new < 50:
        return "Trụ cột đội bóng"
    else:
        return "Ngôi sao đẳng cấp" 
    
def main():
    players = [
    {"id": "CT001","name":"Nguyen trong nguyen","match": 10,"goal": 5,"assist": 4},
    {"id": "CT002","name":"Hồ Thanh Tài","match": 11,"goal": 6,"assist": 3}
    ]
    while True:
        menu()
        choice = input('nhập vào chức năng bạn muốn chọn(1-8): ')
        match choice:
            case '1':
                display_CT(players)
            case '2':
                add_CT(players)
            case '3':
                update_CT(players)
            case '4':
                remove_CT(players)
            case '5':
                search_CT(players)
            case '6':
                print()
            case '7':
                print()
            case '8':
                print('thoát menu không chạy nữa')
            case _ :
                print()
main()