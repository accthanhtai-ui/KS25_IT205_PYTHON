# vòng lặp for
# for i in range(1,5,2):
#    print(i, end= "")

# vòng lặp while
# i = 1
# while (i < 11):
#    print(i)
#    i += 1

# yêu cầu 3: In ra các số chẵn từ 1 tới 10, lưu ý bỏ qua số 4
#  i = 1
# while i <= 10:     
#    if i == 4:          
#       continue
#     if i % 2 == 0:     
#        print(i, end=" ")
#     i += 1

# yêu cầu 4: cho người dùng nhập vào 1 số, nếu như số đó không phải là số 
# nguyên dương, bắt nhập lại.và in ra số vừa nhập ra màn hình
# while True:  
#        n = int(input("Nhập vào một số nguyên dương: ")) 
#        if n > 0: 
#            print("Số vừa nhập là:", n)
#            break  
#        else:
#            print("Đây không phải số nguyên dương, hãy nhập lại!")
    

# yêu cầu 5: cho 2 số a b cho trước, tìm UCLN của 2 số
# b1: tìm ra số nhỏ hơn trong 2 số
# b2: lặp từ 1 đến min
# b3: kiểm tra nếu a và b đều chia hết cho số đó thì số đó là UCLN
# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# if a < b:
#    min_num = a
# elif b < a:
#    min_num = b
# ucln = 1
# for i in range(1, min_num + 1):
#    if a % i == 0 and b % i == 0:
#        ucln = i

# print("UCLN của", a, "và", b, "là:", ucln)

# yêu cầu: tìm bội chung nhỏ nhất của 2 số
# việc đầu tiên: tìm ra số lớn hơn trong 2 số(max)
