total_revenu = 0
count = 0
for i in range(1,8):
    revenue = int(input(f'nhập lương ngày{i}'))
    if revenue >= 5000000:
        count +=1
    total_revenu += revenue

avg_revenue = total_revenu/7
print('tổng lương là:',total_revenu)
print(f'lương trung bình trong 7 ngày {avg_revenue:.2f}')
print(f'lương ngày đạt chỉ tiêu có{count} ngày')

    