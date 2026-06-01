while True:
    print("""+============================================+
    |     HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK       |
    +============================================+
    | 1. Nhập và phân tích thông tin video       |
    | 2. Chuẩn hóa tên tài khoản                 |
    | 3. Kiểm tra tính hợp lệ của hashtag        |
    | 4. Tìm kiếm và thay thế từ khóa trong mô tả|
    | 5. Thoát chương trình                      |
    +============================================+
    """)
    x = input("> Mời bạn chọn chức năng (1-5): ")
    match x:
        case '1':
            while True:
                name_user = input("Nhập tên tài khoản người đăng video: ")
                if name_user.strip() == "":
                    print("tên tài khoản không được rỗng vui lòng nhập lại")
                    continue
                title_video = input("Nhập vào - Tiêu đề video: ")
                content_video = input("Nhập Mô tả video: ")
                if content_video.strip() == "":
                    print('mô tả không được để trống vui lòng nhập lại!!')
                    continue
                hastag_video = input("Nhập danh sách hashtag, cách nhau bởi dấu phẩy: ")

                print(f'tên tài khoản :  {name_user.strip()}')
                print(f'mô tả độ dài video :  {title_video.strip().title()}')
                print(f'mô tả video :  {content_video.strip()}')
                print(f'độ dài mô tả video :  {len(content_video)}')
                print(f'số lượng từ mô tả :  {len(content_video.split())}')
                temp_hagtag = hastag_video.split(',')
                new_hagtag_video = ''.join(temp_hagtag)
                print(f'danh sách hagtag là: {new_hagtag_video.strip()}')
                print(f'số lượng hagtag là : {len(hastag_video.split(','))}')
                print(f'Mô tả video được chuyển toàn bộ sang chữ thường: {content_video.lower()}')
                print(f'Mô tả video được chuyển toàn bộ sang chữ HOA: {content_video.upper()}')
                break
        case '2':
            print(f'tên tài khoản ban đầu là: {name_user}')
            print(f'tên tài khoản sau khi được chuẩn hóa: @{name_user.lower()}')
        case '3':
            while True:
                new_hastag = input('nhập vào hastag mới: ')
                if new_hastag  == '':
                    print('hastag không được để trống vui lòng nhập lại ')
                elif not(new_hastag.startswith('#')):
                    print('hastag phải bắt đầu bằng #')
                elif ' ' in new_hastag:
                    print('hastag không được chứa khoảng trắng')
                elif len(new_hastag) < 2:
                    print('hastag phải chứa ít nhất 2 kí tự')
                else:
                    print('hastag hợp lệ!')
                    hastag_video += new_hastag
                    print(f'danh sách hastag mới là {hastag_video}')
                    break
        case '4':
            find_work = input('nhập vào từ khóa cần tìm: ')
            up_work = input('nhập từ khóa cần thay vào đó: ')
            count_work = content_video.find(find_work)
            if count_work >= 0:
                content_video = content_video.replace(find_work,up_work)
                print(f'mô tả sau khi sữa lại là {content_video}')
            print(f'số lượng tìm được là {count_work}')
        case '5':
            print('kết thúc trương trình')
            break
        case _:
            print('không hợp lệ hãy nhập lại')
