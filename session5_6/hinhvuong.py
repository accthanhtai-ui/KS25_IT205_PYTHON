# canh =5 
# for i in range (canh):
#     for j in range(canh-i-1):
#         print(' ',end = ' ')
#     for k in range (i*2+1):
#         print('tài',end = ' ')
#     print()
# tìm số nguyên tố
import math
n = int(input('nhập số: '))
if n < 2:
    print('không phải số nguyên tố')
else:
    snt = True
    for i in range (2,math.sqrt(n)+1):
        if n % i == 0:
            snt = False
    if snt == True:
        print('là số nguyên tố')
    else:
        print('không phải snt')
#tìm 30 số đầu tiên mà bạn nhập vào