playlist = []

while True:
    print("\n===== Playlist Management System =====")
    print("""1. Thêm bài hát vào danh sách phát
2. Xem danh sách phát
3. Xóa bài hát khỏi danh sách phát
4. Sắp xếp và Trích xuất danh sách
5. Thoát chương trình
    """)
    choice = input("Nhập vào lựa chọn của bạn: ")

    match choice:
        case "1":
            print("\n*** Thêm bài hát ***")
            print("1. Thêm vào cuối danh sách")
            print("2. Chèn vào vị trí bất kỳ")
            sub_choice = input("Nhập lựa chọn: ")
            song_name = input("Nhập tên bài hát: ")

            match sub_choice:
                case "1":
                    playlist.append(song_name)
                    print(f"Đã thêm thành công! Số lượng bài hát hiện tại: {len(playlist)}")
                case "2":
                    try:
                        index = int(input("Nhập vị trí muốn chèn (bắt đầu từ 1): ")) - 1
                        if 0 <= index <= len(playlist):
                            playlist.insert(index, song_name)
                            print(f"Đã thêm thành công! Số lượng bài hát hiện tại: {len(playlist)}")
                        else:
                            print("Vị trí không hợp lệ.")
                    except ValueError:
                        print("Vui lòng nhập số nguyên cho vị trí.")
                case _:
                    print("Lựa chọn không hợp lệ!")

        case "2":
            if not playlist:
                print("Danh sách phát hiện đang trống!")
            else:
                print("\n--- Danh sách phát ---")
                for i, song in enumerate(playlist, start=1):
                    print(f"{i}. {song}")

        case "3":
            if not playlist:
                print("Danh sách phát hiện đang trống!")
                continue
            print("\n*** Xóa bài hát ***")
            print("1. Xóa theo tên")
            print("2. Xóa theo số thứ tự")
            sub_choice = input("Nhập lựa chọn: ")

            match sub_choice:
                case "1":
                    song_name = input("Nhập tên bài hát cần xóa: ")
                    if song_name in playlist:
                        playlist.remove(song_name)
                        print(f"Đã xóa bài hát '{song_name}' khỏi danh sách.")
                    else:
                        print("Không tìm thấy bài hát trong danh sách phát.")
                case "2":
                    try:
                        index = int(input("Nhập số thứ tự bài hát cần xóa: ")) - 1
                        if 0 <= index < len(playlist):
                            removed_song = playlist.pop(index)
                            print(f"Đã xóa bài hát '{removed_song}' khỏi danh sách.")
                        else:
                            print("Vị trí không hợp lệ.")
                    except ValueError:
                        print("Vui lòng nhập số nguyên cho vị trí.")
                case _:
                    print("Lựa chọn không hợp lệ!")

        case "4":
            if not playlist:
                print("Danh sách phát hiện đang trống!")
                continue
            print("\n*** Sắp xếp & Trích xuất ***")
            print("1. Sắp xếp theo bảng chữ cái")
            print("2. Nghe thử 3 bài hát đầu tiên")
            sub_choice = input("Nhập lựa chọn: ")

            match sub_choice:
                case "1":
                    playlist.sort()
                    print("Danh sách đã được sắp xếp theo bảng chữ cái.")
                case "2":
                    print("\n--- 3 bài hát đầu tiên ---")
                    for i, song in enumerate(playlist[:3], start=1):
                        print(f"{i}. {song}")
                case _:
                    print("Lựa chọn không hợp lệ!")

        case "5":
            print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")
