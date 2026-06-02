music_name = ['đi theo bong mặt trời','hãy trao cho anh','10 ngàn năm']
while True:
    print('''
+============MENU QUẢN LÝ DANH SÁCH PHÁT============+
+ 1.Thêm bài hát vào danh sách phát                 +
+ 2.Xem danh sách phát                              + 
+ 3.Xóa bài hát khỏi danh sách                      +  
+ 4.Xắp xếp và trích xuất danh sách                 +    
+ 5.Thoát trương trình                              +
+===================================================+                
''')
    choice = input('nhập vào chức năng cần làm: ')
    match choice:
        case '1':
            while True:
                print('''-----thêm bài hát-----
1.thêm vào cuối danh sách
2.chèn vào vị trí cụ thể''')
                select = input('nhập vào lựa chọn: ')
                music_name_new = input('nhập vào tên bài hát: ')
                match select:
                    case '1':
                        music_name.append(music_name_new)
                        print('thêm bài hát mới thành công!')
                        break
                    case '2':
                        music_name.insert(music_name_new)
                        print('chèn bài hát vào thành công!')
                        break
                    case _:
                        print('chỉ được chọn 1 hoặc 2,chọn lại')
                        continue
        case '2':
            if len(music_name) == 0:
                print('danh sách đang trống không có bài hát nào')
                continue
            else:
                for i,vl in enumerate(music_name,start=1):
                    print(f'bài hát {i}: {vl}')
        case '3':
            while True:
                print('''-----xóa bài hát-----
1.xóa bài hát theo tên
2.xóa bài hát theo vị trí''')
                select = input('nhập vào lựa chọn: ')
                match select:
                    case '1':
                        del_music = input('nhập vào tên bài hát: ')
                        if del_music in music_name:
                            music_name.remove(del_music)
                            print('xóa bài hát mới thành công!')
                            break
                        else:
                            print('tên bài hát không có trong danh sách,nhập lại')
                            continue
                    case '2':
                        del_index_music = int(input('nhập vào vị trí cần xóa: ')) - 1
                        if 0 < del_index_music and del_index_music <= len(music_name):
                            remove_music = music_name.pop(del_index_music)
                            print('xóa bài hát vào thành công!')
                            print(f'bài hát bạn vừa xóa là:  {remove_music}')
                            break
                        else:
                            print('vi trí nằm ngoài phạm vi hãy nhập lại')
                            continue
                    case _:
                        print('chỉ được chọn 1 hoặc 2,chọn lại')
                        continue
        case '4':
            while True:
                print('''-----xắp xếp    bài hát-----
1.sắp xếp bài hát theo thứ tự từ A-Z
2.Hiển thị 3 bài hát đầu tiên''')
                select = input('nhập vào lựa chọn: ')
                match select:
                    case '1':
                        music_name.sort()
                        print('sắp xếp bài hát mới thành công!')
                        break
                    case '2':
                        if len(music_name) == 0:
                            print('danh sách đang trống không có bài hát nào')
                            continue
                        else:
                            for i,vl in enumerate(music_name[:3],start=1):
                                print(f'bài hát {i}: {vl}')
                    case _:
                        print('chỉ được chọn 1 hoặc 2,chọn lại')
                        continue
        case _:
            print('chọn đúng dùm cái')
            continue
