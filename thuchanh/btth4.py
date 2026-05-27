MAX_CHANGE = 5
SECRET_NUMBER = 27
flag = True
for i in range(1,MAX_CHANGE+1):
    your_choice = int(input(f'nhập số may mắn lần thứ {i}:'))
    if(your_choice == SECRET_NUMBER):
        print('chúc mừng bạn đã đoán đúng số may mắn nhe')
        break
    else:
        if your_choice > SECRET_NUMBER:
            print('số bạn lớn hơn số may mắn')
        else:
            print('số bạn nhỏ hơn số may mắn')
if not flag:
    print('bạn đã hết lượt')